# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin

# 课程列表页
class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        
        # 课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|
                                             Q(desc__icontains=search_keywords)|
                                             Q(detail__icontains=search_keywords))
            
        # 课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-student')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')

        # 课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)
        
        
        return render(request, 'course-list.html', {
            'all_courses':courses,
            'sort': sort,
            'hot_courses':hot_courses
        })
    
    
# 课程详情页
class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        
        # 增加课程点击数
        course.click_nums += 1
        course.save()
        
        has_fav_course = False
        has_fav_org = False

        # 用户是否登录, 用户是否收藏
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
                
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag = tag)[:1]
        else:
            relate_courses = []
            
        return render(request, 'course-detail.html',{
        'course':course,
        'relate_courses':relate_courses,
        'has_fav_course':has_fav_course,
        'has_fav_org':has_fav_org
        })
 
    
# 课程章节信息
class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        
        # 查询用户是否关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
            
        user_cousers = UserCourse.objects.filter(course=course)
        user_ids = [user_couser.user.id for user_couser in user_cousers]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        
        # 取出所有课程ID
        course_ids = [user_couser.course.id for user_couser in user_cousers]
        
        # 获取学过该课程用户的其他课程
        relate_course = Course.objects.filter(id__in=course_ids).order_by('-click_nums')[:5]
        all_resources = CourseResource.objects.filter(course = course)
        
        return render(request, 'course-video.html', {
            'course': course,
            'all_resources':all_resources,
            'relate_course':relate_course
        })
    
    
# 课程评论
class CommentView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comment = CourseComments.objects.all()
        
        return render(request, 'course-video.html', {
            'course': course,
            'all_resources': all_resources,
            'all_comment':all_comment
        })
    

# 用户添加课程评论
class AddCommentView(View):
    def post(self, request):
        # 用户是否登录
        if request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        
        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        
        if course_id > 0 and comments:
            course_comment = CourseComments()
            course = Course.object.get(id = int(course_id))
            course_comment.course = course
            course_comment.comments = comments
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')
            
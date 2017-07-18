# -*- coding:utf-8 -*-

__author__ = "qyfl"
__date__ = "2017/7/16 15:23"

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_dispaly = ['name', 'desc', 'detail', 'degree', 'learn_times', 'student', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'student', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'student', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class LessonAdmin(object):
    list_dispaly = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_dispaly = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_dispaly = ['course', 'name', 'dowload', 'add_time']
    search_fields = ['course', 'dowload', 'name']
    list_filter = ['course', 'name', 'dowload', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
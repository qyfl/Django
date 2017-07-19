## Django note 2
---
### 建立与数据库的连接
开发第一步首先建立与数据库的连接，否则测试都用不了。
在 settings 中的 DATABASES ，代码如下：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'your_name',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
    }
}
```
然后点击 TOOLS--->Run manage.py Task 输入命令：
```
makemigrations
```
生成 Django 项目默认的数据表，然后使用命令：
```
migrate
```
将生成的数据表上传到数据库，这时候可以在数据库中看到那些表。

### 设计 app
#### 设计 user app
在 web 系统中，user 大多是首先被设计的，因为用户的属性在开发之前就很清楚。点击 Task 使用命令：
```
startapp users
```
在 settings 中的 INSTALLED_APPS 中添加新建的 app，只要是 app 就都要添加到 settings 中。Django 默认生成的数据表中有 user 表，但是大多情况下默认的表字段是不够用的，所以我们都需要在表中添加字段。进入 users 下的 models.py 中添加我的需要的字段。需要继承默认的 user 表。代码如下：

```
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", u'男'), ('female', u'女')), default='female', max_length=6)
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unciode__(self):
        return self.username

```
>A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.  
> - Each model is a Python class that subclasses django.db.models.Model.
> - Each attribute of the model represents a database field.    
>  -------------[Django官网文档](https://docs.djangoproject.com/en/1.11/topics/db/models/)

>模型是你的数据的唯一的、权威的信息源。它包含你所储存数据的必要字段和行为。通常，每个模型对应数据库中唯一的一张表。  
> - 每个模型都是 django.db.models.Model 的一个 Python 子类。
> - 模型的每个属性都表示为数据库中的一个字段。

根据官方文档，我们可以知道，models 可能就是数据库抽象，可以直接操作 models 从而改变数据库里的信息。

models 中有很多函数，文档的链接已经给出，这里就不一一列举了，后面的内容都是建立在看过文档中对于 models 描述的基础上。我还是贴出对于初学者有帮助的 Django1.8 版本的[中文文档](http://python.usyiyi.cn/translate/django_182/topics/db/models.html)。  

然后重载 settings 中的 AUTH_USER_MODEL，代码如下：
```
AUTH_USER_MODEL = 'users.UserProfile'
```
这时候可以使用生成数据表和提交数据表的命令，这时候可以在数据库的 user_profile 表中看到我们添加的字段和原有字段。  

验证码功能只会和 user 产生关系，所以放在 user 中实现。首页轮播图其实和 user 没有太大关系，但是因为功能非常独立，所以先放在 user 中实现。 代码和 UserProfile 类似，但是就无需继承 AbstractUser，因为数据库中没有默认的验证码和轮播图的表，所以继承 models.Model 新建表。

#### 设计 course app
因为在需求分析阶段 course 的属性就知道了。直接添加，注意，有的字段有外键，外键先实现，不然没法测试。

#### 设计 organization app
同上

#### 设计 operation app
operation 存在的意义是防止出现循环，比如课程评论有用户信息，用户可以添加评论。没有建立在课程和用户之上的 app 不好搞。

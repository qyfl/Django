## Django note 3
---
### 后台杀手级功能 xadmin
不介绍 xadmin 的功能了，[xadmin 官网](https://sshwsfc.github.io/xadmin/)(中文界面)。从官网给出的 github 中下载xadmin， 添加到 extra_apps 文件夹中。不使用 conda 或 pip 安装，github更新最快，功能最新。然后修改 urls 中的后台管理界面的 url，代码如下：
```
import xadmin
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #.....
]
```
这里注意，除了要在 settings 中添加 xadmin app，还要添加 crispy_forms app。因为依赖，
然后建立后台关系系统的雏形。

#### 为 apps 设计后台管理
在每个 app 的目录下新建 xadmin.py 文件，然后为每个 model 设计后台管理。user 下的 xadmin.py 部分代码如下：
```
from .models import EmailVerifyRecord

class EmailVerifyRecordAdmin(object):
    list_dispaly = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
```
对时间排序的 filed 不会做，先不做。然后与 models 中的同名 class 绑定，不然怎么到数据库中拿到数据。


### 配置 html
这个是我非常苦恼的部分，在此之前我不会 [js](https://www.javascript.com/) [css](https://www.w3.org/) [h5](https://www.w3.org/TR/html5/)，然后我就去看了下[基本语法](http://www.w3school.com.cn/index.html)(中文)，看完就好多了。  

然后把 html 复制到 templates 文件夹下，css、js 等样式复制到 static 文件夹下。然后将页面中的引用静态文件的路径全部替换掉，原来的代码如下：

```
<link rel="stylesheet" type="text/css" href="../css/reset.css">
```

替换成

```
{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
```

load staticfiles 只需要一次。然后去 settings 中添加静态文件搜索路径：

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

在 urls.py 中配置这个页面的 url，代码如下：

```
from django.views.generic import TemplateView
urlpatterns = [
    #......
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    #......
]
```
> A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.  
> \--------[官方文档](https://docs.djangoproject.com/en/1.11/topics/http/views/)

> 一个视图函数，简称视图，是一个简单的Python 函数，它接受Web请求并且返回Web响应。响应可以是一张网页的HTML内容，一个重定向，一个404错误，一个XML文档，或者一张图片. . . 是任何东西都可以。无论视图本身包含什么逻辑，都要返回响应。代码写在哪里也无所谓，只要它在你的Python目录下面。除此之外没有更多的要求了——可以说“没有什么神奇的地方”。为了将代码放在某处，约定是将视图放置在项目或应用程序目录中的名为views.py的文件中。

> View就是我们看到的网页，在网页上的操作都要在 app 下的 views.py 完成，View 与网页的关系就像 models 与数据库的关系。  
> \------来自qyfl的总结

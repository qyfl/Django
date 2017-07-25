## 项目与笔记的总结
---
说明：我的笔记书写方式比较奇怪，主要是为了备忘。可能会有人看我的笔记，我想给予这些人一些帮助，所有又有点像写书。
### 项目总结
这是一个使用 Django1.9 + Python2.7 + Mysql 搭建起来的教育网站。  
网站的组成部分是用户和教育机构。网站的功能有：
- 用户的登录注册
- 教育机构的添加
- 教育机构的讲师添加
- 讲师的课程添加
- 用户学习的课程
- 用户评论的课程
- 课程的排序
- 还有一些很零碎的功能，比如某一门课有多少人点击过

这个网站并没有完全做完，比如讲师的课程，那需要把视频资源放到云上，然后动态的加载。整个网站的课程信息也是我乱填的。

我所使用的web框架是 Django，因为我是一个人完成的，所以并没有才用前后端分离的开发方式。
Django 最经典的，也是我在项目中使用的模式是 MTV 模式。

#### Django 中的 MTV 模式
MTV 是 Django 中最重要的三个组成部分的缩写，分别是 Model, Template, View。

当一个请求过来的时候，首先就是去找 urls 有没有相对于的链接。找到的话，就对调用相对应的 view 来加载网页。在加载的过程中，大部分数据都要从数据库中拿，而不是直接写死，比如课程的点击数。这时候就需要 Model。

Model就是数据库的代理和抽象。我们可以直接操作 Model 来完成数据的提取。View 拿到数据之后就会交给 Template。 Template 其实就是 html 文件。但是其中数据的部分全部是空的，是 View 拿到数据以后动态添加的。比如课程的图片，名字，所属机构。

一个请求过来通过 urls 找到对应的 View，然后从 Model 中拿到数据，交给 Template 填充到 html 里。这就是 MTV 模式。

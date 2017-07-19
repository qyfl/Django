## Django笔记(一)

---
### 环境搭建
1. 去[python官网](https://www.python.org/)下载python，最好两个版本都下载。
2. 去[Pycharm官网](https://www.jetbrains.com/)下载Pycharm的专业版，开发必须用专业版，有些必须要用到的功能社区版没有。
3. 去[Anaconda官网](https://www.continuum.io/)下载适合的版本。下载Anaconda出于两个理由：要在同一台计算机上同时存在两个python版本。解决库的依赖关系。(win下安装时要选择添加PATH)

##### 开始前的准备工作：
- 修改Anaconda下载源  
使用命令 ```conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/``` 修改成清华大学的源。  
使用命令 ```conda config --set show_channel_urls yes``` 在下载过程中显示下载地址，也就是我们修改的源。

- 修改pip源  
在 ```C:\Users\Administrator\``` 下创建 pip 文件夹，在pip创建pip.ini文件，然后写入：  
    ```
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    ```

- 使用Anaconda创建虚拟环境  
虚拟环境的墓地是为了区分不同的工作环境特别是py2和py3的环境。使用命令 ```conda create -n your_name python=2.*``` 创建py2的环境，需要py3的环境就把 2.\* 换成 3.\* 就好了。虚拟环境之间是互不干扰的。

- 进入虚拟环境  
使用命令 ```activate your_name```

- 安装Django  
使用命令 ```pip install django==1.9.8``` 这里使用的版本是1.9.8, conda 库中没有

- 退出虚拟环境   
使用命令 ```deactivate your_name```

- Anaconda安装库  
使用命令 ```conda install your_name``` 使用Anaconda安装库要比pip安装的依赖检查的严格，但有些库pip中有Anaconda中没有的时候，就要使用pip来安装。

- pip安装库  
使用命令 ```pip install your_name```

### 创建项目
使用Pycharm中的Django模版，设置项目所在路径，设置项目虚拟环境路径(选择虚拟环境中的 python.exe)，点击 OK。

### 项目文件目录介绍

初始化的Django项目中的包含以下文件。

- settings.py  
  包括app注册、数据库设置、文件路径设置等

- urls.py  
  Django项目中所有的url都在urls.py中设置

- manage.py  
  Django启动文件，还不太了解

- init.py
  还不太了解

- wsgi.py  
  Django启动的wsgi文件，现在还不太了解它的作用

- templates(文件夹)  
  存放大多所有的html文件

### Pycharm文件夹设置

在pycharm中可以对文件夹的属性进行设置，但是在命令行下这些设置是不生效的。但真正部署的时候还是在命令行下部署。所以也需要在setting中设置。pycharm中的设置只是为了开发的方便。

pycharm中可以对文件夹进行mark，mark有4个选项。

1. Sources Root  
  此时在import该文件夹下的模块时，无需指明全路径。

2. Excluded  
  没用过

3. Rescource Root  
  没用过

4. Template Folder  
  与Django自动生成的templates一样的作用，Django会从该文件夹下去找html文件。

在Django项目初始化之后还应该建立以下文件夹

- apps  
  每个功能最好单独分出来成为一个app，存放在apps中。这样做有利于项目有对于整个项目中功能的理解，对以后的修改也是有好处的。但是要在 settings 中添加路径，代码如下：
  ```
  import sys
  sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
  ```

- extra_apps  
  有时候需要用到一些插件，但是pip库里没有。或者想要使用最新的功能pip库没有更新这样情况下就需要安装源码来使用，如果插件超过一个，最好单独放在一个文件夹下。同样要在 settings 中添加路径，代码如下：
  ```
  import sys
  sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
  ```

- static  
  存放css、js、图片等静态文件

- log  
  存放日志文件

- media  
  存放用户上传文件

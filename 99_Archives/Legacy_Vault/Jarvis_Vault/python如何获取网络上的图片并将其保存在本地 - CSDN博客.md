---
created: 2018-09-08 20:49:15
jarvis_ai_meta:
  key_people: []
  mood: 平静、务实
  summary: 用户测试并总结了两种使用Python从网络下载图片并保存到本地的技术方法。
  tagged_at: '2026-01-11 02:40:17'
  time_space:
    date: '2018-09-08'
    location: ''
source: https://blog.csdn.net/qq_28304687/article/details/76551196
tags:
- 图片下载
- PIL
- Python
- 网络爬虫
- urllib
updated: 2018-09-08 20:49:15
---

# python如何获取网络上的图片并将其保存在本地 - CSDN博客

<https://www.csdn.net/>
<https://blog.csdn.net/>

<http://so.csdn.net/so/?t=blog>
[登录](https://passport.csdn.net/account/login?ref=toolbar)
[![unknown_filename.gif](./_resources/python如何获取网络上的图片并将其保存在本地_-_CSDN博客.resources/unknown_filename.gif)](https://my.csdn.net/)

 [![unknown_filename.1.png](./_resources/python如何获取网络上的图片并将其保存在本地_-_CSDN博客.resources/unknown_filename.1.png) qq_28304687](https://blog.csdn.net/qq_28304687) 
关注

[访问量 8万+ 原创 25 博主更多文章>](https://blog.csdn.net/qq_28304687)

# 原 python如何获取网络上的图片并将其保存在本地

 [![unknown_filename.1.png](./_resources/python如何获取网络上的图片并将其保存在本地_-_CSDN博客.resources/unknown_filename.1.png) qq_28304687](https://blog.csdn.net/qq_28304687) 阅读数：15211 2017-08-01

版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/qq\_28304687/article/details/76551196

之前写爬虫大多是爬网页中的url，然后将url保存下来就可以了，倒还没有想过要获取真的图片到本地。

网络上有很多方法，但是很多都是本地，或者其他，亲测了两种方法：

方法一，使用urllib.urlretrieve()，之前其实偶尔看到这个函数，但一直记不住它是做什么的，主要是没在实战中用上，这是最简单的方法：

    import urllib
    
    # 网络上图片的地址
    img_src = 'http://img.my.csdn.net/uploads/201212/25/1356422284_1112.jpg'
    
    # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
    urllib.urlretrieve(img_src,'D:/1.jpg')
    

* 1

* 2
* 3
* 4
* 5
* 6
* 7
* 8

关于urllib.urlretrieve()的解释，我是在这看到的：<http://www.nowamagic.net/academy/detail/1302861>

方法二，使用PIL+requests：

    import requests
    from PIL import Image
    from io import BytesIO
    
    response = requests.get(img_src)
    image = Image.open(BytesIO(response.content))
    image.save('D:/9.jpg')

* 1
* 2
* 3
* 4
* 5
* 6
* 7

这种方法就是将url从网上get下来，然后利用PIL，通过open打开和save保存，之前看到大多就是image.show()，而并没有讲这么保存，这个我试了一下，就是会打开这个image的图片，后来看到这篇<http://www.jb51.net/article/102981.htm>的时候，看到原来只要save就可以了，参数就是你要保存的文件名。

注意，这个BytesIO是必须的，它是用来操作二进制数据的，图片就是二进制数据了，和它相对的自然是StringIO，这是用来存str的。他们的区别就好似python读写普通文件和二进制文件。

其他方法我没有测，因为最近在尝试弄读取验证码，所以用到了PIL，这个相对来说，还是没有第一种方法简单，只需要一句代码，并且库是本身自带的，PIL可能还需要去下。个人觉得这两种方法已经足够简单，其他也没有必要尝试了。

当前没有评论 [点击发表评论](https://blog.csdn.net/qq_28304687/comment/post?id=76551196)

#### [_python_ 爬取网页中的_图片_到_本地_](https://blog.csdn.net/Jaster_wisdom/article/details/52825244)
#### [_Python_下载_图片_并保存_本地_的两种方式](https://blog.csdn.net/Pan_YT/article/details/79050961)

#### [_python_爬虫-下载_图片_到_本地_目录](https://blog.csdn.net/a735311619/article/details/77488576)
#### [_python_ 简单的_图片_下载到_本地_](https://blog.csdn.net/DuanKun7323/article/details/79135795)
#### [_python_把爬取到的_图片_保存到_本地_](https://blog.csdn.net/qq_41314248/article/details/80289609)
#### [_python_下载_图片_到_本地_](https://blog.csdn.net/qq_22222499/article/details/58608003)
#### [从程序员到CTO其实你只差一步](https://click.hm.baidu.com/clk?b2d9fcc07e40dbfa8372fd31502ac094)
#### [使用_python_做爬虫时保存_图片_的方法大全以及需要注意的地方](https://blog.csdn.net/weixin_41931602/article/details/80605229)

#### [利用_Python_抓取_网络__图片_](https://blog.csdn.net/m0_37938791/article/details/72849679)
#### [_Python__网络__图片_爬虫—神经_网络_训练数据_获取_方法](https://blog.csdn.net/weixin_36913190/article/details/80556986)
#### [_python_----打开 显示 保存_图片_](https://blog.csdn.net/Bear_Kai/article/details/78395090)

点赞 7
评论
收藏

<https://blog.csdn.net/qq_28304687/article/details/76551196#><https://blog.csdn.net/qq_28304687/article/details/76551196#>

文章收藏成功
---
created: 2017-10-28 08:51:48
jarvis_ai_meta:
  key_people: []
  mood: 自信、乐于分享
  summary: 作者（码星人）在简书发布了一篇关于在Ubuntu系统上配置Shadowsocks(SS)和Privoxy以实现翻墙的详细技术教程。
  tagged_at: '2026-01-11 02:42:03'
  time_space:
    date: '2016-12-04'
    location: 简书平台
source: http://www.jianshu.com/p/4c95d10b898b
tags:
- Shadowsocks
- Privoxy
- 技术教程
- 翻墙
- Ubuntu
updated: 2017-10-30 10:10:50
---

# Ubuntu下SS搭建 - 码星人 - 简书

[![unknown_filename.10.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.10.png)

创作你的创作

免费下载](http://www.jianshu.com/apps/download?utm_medium=top-download-banner&utm_source=mobile)

# Ubuntu下SS搭建

[![180](http://upload.jianshu.io/users/upload_avatars/2754933/4f5d8d30-6cdf-4cad-8b67-6fb6f923c0f3.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/180/h/180)
码星人
简书作者](http://www.jianshu.com/u/f042e3046f44?utm_medium=note-author-link&utm_source=mobile)
2016.12.04 23:59 打开App

![unknown_filename.8.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.8.png)
Fuchsia

作为一个程序员，**翻墙**可谓是手到擒来，自己租个服务器，当然也有免费的服务器可以用，可能网速稍差。然后再搭个PPTP或者SS，接着就可以看看外面的世界了，刷刷Twitter、FB，看看Youtube，当然更重要的是获取外面的源码。

Windows下的翻墙就不必赘述了，各种VPN软件很放方便。但是Linux下如果不会的话还要折腾一番。今天就来教大家**Ubuntu**下怎么使用**SS**翻墙，主要是因为我用的是SS没有用VPN，所以VPN的使用就由大家自己去研究了。

#### 安装SS

1. 首先需要保证你的网络是畅通的，然后更新软件源，用下面的命令
	`sudo apt-get update`

* 然后安装**python-pip**
	`sudo apt-get install python-pip`
* 安装SS
	`sudo pip install shadowsocks`
* 配置SS
	`sudo vim /etc/shadowsocks.json`
	输入以下代码
	
	    {
	     "server": "你的服务器ip",
	     "server_port": 你的服务器端口,
	     "local_address": "127.0.0.1",
	     "local_port": 1080,
	     "password": "你的SS密码",
	     "method": "aes-256-cfb",
	     "fast_open": true,
	     "timeout":300
	    }
	
* 启动SS
	`sudo sslocal -c /etc/shadowsocks.json`
* 开机自动启动SS
	将上面的代码加入到`/etc/rc.local`文件中的`exit 0`这句代码之前。

以上就是SS的搭建了，这个时候我们发现上网时并不可以翻墙，原因是需要将sock5代理映射为http代理。代理的软件很多，我选择了推荐度比较高的privoxy，下面是privoxy的配置。

#### 安装privoxy

1. 安装privoxy
	`sudo apt-get install privoxy`
2. 配置privoxy
	打开`/etc/privoxy/config`
	找到其中的4.1节，看一下有没有一句`listen-address localhost:8118`的代码，如果被注释了，取消注释。因为版本不一样这句的状态可能会不一样。
	![unknown_filename.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.png)
	4.1节
	
	接着找到5.2节，在本节末尾加入下面代码
	`forward-socks5 / 127.0.0.1:1080 .`
	![unknown_filename.2.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.2.png)
	5.2节
	
3. 重启privoxy服务
	`sudo /etc/init.d/privoxy restart`
4. 开机自启privoxy服务
	将`sudo /etc/init.d/privoxy start`代码加入到`/etc/rc.local`文件中的`exit 0`这句代码之前。

配置后的rc.local如下

![unknown_filename.9.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.9.png)
rc.local

以上就是privoxy的配置了，接着需要配置终端和Firefox浏览器的代理。

#### 代理配置

1. 终端代理
	将以下代码追加到`/etc/profile`中或者`~/.bashrc`中
	
	    export http_proxy="127.0.0.1:8118"
	    export https_proxy="127.0.0.1:8118"
	    export ftp_proxy="127.0.0.1:8118"
	
	接着执行`source /etc/profile`或者`source ~/.bashrc`，这样就完成了终端翻墙的配置，执行`wget google.com`测试一下。
	![unknown_filename.6.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.6.png)
	测试
	
2. Firefox浏览器的配置，打开**设置**\->**高级**\->**网络**\->**连接**，配置如下
	![unknown_filename.4.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.4.png)
	Firefox配置
	
	注意需要将那个勾打上哦～
	测试一下Twitter
	![unknown_filename.5.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.5.png)
	Twitter喜欢的可以关注哦～
	

经过以上的配置以后，我们就可以愉快的看外面的世界了，至于可以访问的网页就需要看你的SS设置的规则了。可能是我之前用server版的Linux用多了，代理就想着往文件里面加 0.0。当我用Chrome的时候，提示我它的代理用的就是系统代理，我才想起来还有个系统代理。如果想全部使用代理的话，系统代理就这样配置。**系统设置**\->**网络**

![unknown_filename.1.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.1.png)
系统代理

当不想使用全局代理的时候将**Manual**选为**None**就好了。

好了，以上就是Ubuntu下的SS配置了，后续可能会更新一些dart和flutter的学习经验，感兴趣的朋友可以关注一下呦呦呦～

如果觉得我的文章对您有用，请随意赞赏。您的支持将鼓励我继续创作！

[赞赏支持](http://www.jianshu.com/p/4c95d10b898b)

© 著作权归作者所有

简书作者
 [![180](http://upload.jianshu.io/users/upload_avatars/2754933/4f5d8d30-6cdf-4cad-8b67-6fb6f923c0f3.jpg?imageMogr2/auto-orient/strip%7CimageView2/1/w/180/h/180)](http://www.jianshu.com/u/f042e3046f44?utm_medium=note-author-link&utm_source=mobile) 

码星人
写了 953 字，获得了 8 个喜欢

你的失败从来都是你自己造成的。

[关注](http://www.jianshu.com/p/4c95d10b898b) [作者个人主页](http://www.jianshu.com/u/f042e3046f44?utm_medium=note-author-link&utm_source=mobile)

推荐阅读 [更多精彩内容](http://www.jianshu.com/?utm_medium=note-recommendation-link-index&utm_source=mobile)
[下载简书App
随时随地发现和创作内容](http://www.jianshu.com/apps/download?utm_medium=bottom-download-banner&utm_source=mobile)
<http://www.jianshu.com/apps/download?utm_medium=bottom-download-banner&utm_source=mobile>

![unknown_filename.3.png](./_resources/Ubuntu下SS搭建_-_码星人_-_简书.resources/unknown_filename.3.png)

创作你的创作，
接受世界的赞赏

[登录](http://www.jianshu.com/p/4c95d10b898b) **|** [打开App](http://www.jianshu.com/p/4c95d10b898b) **|** [热门文章](http://www.jianshu.com/?utm_medium=bottom-link-index&utm_source=mobile)
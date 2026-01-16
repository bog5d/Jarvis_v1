---
created: 2019-01-07 14:30:54
jarvis_ai_meta:
  key_people: []
  mood: 探索、满意
  summary: 作者探索了通过Python实现微信消息推送的三种方法，最终推荐使用ServerChan和PushBear服务。
  tagged_at: '2026-01-11 01:35:35'
  time_space:
    date: '2018-08-22'
    location: ''
source: https://hoxis.github.io/python-serverchan.html
tags:
- 自动化
- ServerChan
- PushBear
- Python
- 微信推送
updated: 2019-01-07 14:30:54
---

# 1 行代码，实现微信消息发送 | pushbear

<https://github.com/hoxis>

[_hoxis' blog_](https://hoxis.github.io/)
__

# 生命在于折腾

__

__

* [首页](https://hoxis.github.io/)

* [阅读排行](https://hoxis.github.io/top/)__
__* [分类](https://hoxis.github.io/categories/)__
__* [标签](https://hoxis.github.io/tags/)__
__* [归档](https://hoxis.github.io/archives/)__
__* [资源](https://hoxis.github.io/resources/)
* 搜索

## 1 行代码，实现微信消息发送

发表于
2018-08-22
| 分类于 [Python](https://hoxis.github.io/categories/Python/) | [0](https://hoxis.github.io/python-serverchan.html#comments) | 阅读次数: 248
字数统计: 1,244 | 阅读时长 ≈ 4

还是接食行生鲜签到的问题，之前我们讲到，将签到结果通过短信发送到手机，但是我发现 twilio 有些不稳定，为了防止漏签，我在服务器上设置了两次定时任务，通常情况下第一个收不到短信，第二个才会收到。

看到最近好多大神写操作微信的文章，于是，我又想，是不是可以将消息发送到微信上？

<https://hoxis.github.io/python-serverchan.html>

微信发送消息有如下几个思路：

1. itchat 模块
2. 使用个人公众号
3. 使用其他公众号封装好的发送消息的功能；

# [itchat](https://hoxis.github.io/python-serverchan.html#itchat)

[大部分人操作个人微信都是使用这个模块。](https://hoxis.github.io/python-serverchan.html#itchat)

[itchat 是一个开源的微信个人接口，它可以模拟网页端的微信登陆，从而用 Python 脚本或命令行模式来使用个人微信号，达到推送各种通知到微信上的目的。](https://hoxis.github.io/python-serverchan.html#itchat)

[项目主页：](https://hoxis.github.io/python-serverchan.html#itchat)<https://github.com/littlecodersh/ItChat>

其实是基于网页版微信，通过 HTTP 交互来实现微信的一些操作，被封的风险其实在于，当检测到账号异常时，账号的网页版登录权限会被腾讯禁掉，这种情况下 itchat 就不好使了。另外，据说新申请的账号直接没有网页版登录权限了。

itchat 的使用已经有其他很多大神讲了，网上也有很多教程，这里我们不再赘述，有兴趣的自行 Google，也可以后台找我，一起来研究下~

[![unknown_filename.6.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.6.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140229.png)

# [个人公众号接口](https://hoxis.github.io/python-serverchan.html#%E4%B8%AA%E4%BA%BA%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%A5%E5%8F%A3)

[微信提供了丰富的公众号接口，可以实现消息收发、关注用户信息获取等等。](https://hoxis.github.io/python-serverchan.html#%E4%B8%AA%E4%BA%BA%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%A5%E5%8F%A3)

[BUT！大部分接口（包括发送消息接口）只开放给认证用户，而个人号又无法认证，所以这条路断了！](https://hoxis.github.io/python-serverchan.html#%E4%B8%AA%E4%BA%BA%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%A5%E5%8F%A3)

<https://hoxis.github.io/python-serverchan.html#%E4%B8%AA%E4%BA%BA%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%A5%E5%8F%A3>[![unknown_filename.11.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.11.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140244.png)

[![unknown_filename.1.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.1.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140254.png)

据说以前个人是可以认证的，反正权限的口子越来越小了。

[![unknown_filename.10.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.10.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140303.png)

# [别人家的公众号](https://hoxis.github.io/python-serverchan.html#%E5%88%AB%E4%BA%BA%E5%AE%B6%E7%9A%84%E5%85%AC%E4%BC%97%E5%8F%B7)

[正所谓「它山之石，可以攻玉」，此处不留爷，爷就去他处！今天的主角登场！](https://hoxis.github.io/python-serverchan.html#%E5%88%AB%E4%BA%BA%E5%AE%B6%E7%9A%84%E5%85%AC%E4%BC%97%E5%8F%B7)

[还好我们找到了提供收发消息功能的公众号 API，我们只要集成他们的接口即可。

它就是「**Server酱**」！](https://hoxis.github.io/python-serverchan.html#%E5%88%AB%E4%BA%BA%E5%AE%B6%E7%9A%84%E5%85%AC%E4%BC%97%E5%8F%B7)

## <https://hoxis.github.io/python-serverchan.html#%E5%88%AB%E4%BA%BA%E5%AE%B6%E7%9A%84%E5%85%AC%E4%BC%97%E5%8F%B7>[Server 酱](https://hoxis.github.io/python-serverchan.html#Server-%E9%85%B1)

[Server 酱，英文名字 ServerChan，地址：](https://hoxis.github.io/python-serverchan.html#Server-%E9%85%B1)[http://sc.ftqq.com](http://sc.ftqq.com/)

使用方法：

1. 登入：用 GitHub 账号登入网站，就能获得一个 SCKEY（在「发送消息」页面）；
2. 绑定：点击「微信推送」，扫码关注同时即可完成绑定；
3. 发消息：往 <http://sc.ftqq.com/SCKEY.send> 发 GET 请求，就可以在微信里收到消息啦；

来个示意图：

[![unknown_filename.gif](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.gif)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/2018-8-22-59bdc111f5d7df399b5f86a20163dfa0.gif)

代码示例：

|     |     |
| --- | --- |
| 1<br>2 | \>>> import requests<br>\>>> requests.get("https://sc.ftqq.com/your-SCKEY.send?text={}&desp={}".format('测试标题','哈哈')) |

微信端效果：

[![unknown_filename.9.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.9.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140344.png)

是不是很简单！1 行代码就搞定了微信消息推送，再也不用其他任何复杂的步骤！

另外，显示发现发件人是Server酱，另外点进去有推广，毕竟是免费的接口，还要啥自行车！

还有就是发送消息是有一些限制的：

> 每人每天发送上限 500 条，相同内容 5 分钟内不能重复发送，不同内容一分钟只能发送 30 条。主要是防止程序出错的情况。

对于我这种需求肯定够了。

## [PushBear](https://hoxis.github.io/python-serverchan.html#PushBear)

[ServerChan 只能推送到一个微信上，若果想一对多发送信息，并且向自定义发件人，那么可以使用 PushBear。](https://hoxis.github.io/python-serverchan.html#PushBear)

<https://hoxis.github.io/python-serverchan.html#PushBear>

[PushBear 地址：](https://hoxis.github.io/python-serverchan.html#PushBear)[https://pushbear.ftqq.com](https://pushbear.ftqq.com/)

1. 无需注册，直接扫码登入；
2. 创建消息通道，获得订阅二维码；
3. 通过 [API](http://pushbear.ftqq.com/admin/#/api) 向关注了该二维码的用户推送消息；

PushBear 可以自定义发件人信息，通过微信登录后，创建一个通道，会生成一个 sendkey 和一个订阅二维码， 可以通过「订阅消息API」发送微信给所有扫描过此二维码的人。

[![unknown_filename.3.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.3.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140358.png)

代码示例：

|     |     |
| --- | --- |
| 1<br>2 | import requests<br>requests.get("https://pushbear.ftqq.com/sub?sendkey=your-sendkey&text={}&desp={}".format('pushbear', '哈哈')) |

微信端效果：

[![unknown_filename.2.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.2.png)](https://blog-1254259578.cos.ap-shanghai.myqcloud.com/picgo/20180906140411.png)

发现发件人是我们自己设置的「不正经程序员」了！

使用限制：

> 推送消息存储 72 小时、5 分钟内不可发布重复消息、普通用户每天 1000 条上限、请勿用于发送广告和有害信息。

综上，若要完成签到成功后的通知，我们只要使用 ServerChan 或者 PushBear 的接口封装成发送消息的函数即可！

食行生鲜签到系列也可以到此结束了，回复【食行生鲜】可以获取最终代码。

# [总结](https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93)

[也许还有其他微信的使用方法，但是 ServerChan 是我找到的最简单的一个了，1 行代码搞定，简单高效，很 **pythonic**！](https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93)

[当然，作为个人发送一些通知 ServerChan 是绰绰有余的，但是，若是企业级的应用还是用自己的微信订阅号来开发接口吧~](https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93)
<https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93>
<https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93>
<https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93>[![unknown_filename.5.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.5.png)](https://hoxis.github.io/uploads/wechat-qcode.png)
提供 CSDN 资料免费下载服务，欢迎来撩~

赞赏一杯咖啡
打赏

* **本文作者：** hoxis | 微信公众号【不正经程序员】
* **本文链接：** <https://hoxis.github.io/python-serverchan.html>
* **版权声明：** 本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 许可协议。转载请注明出处！
* 并保留本声明和上方二维码。感谢您的阅读和支持！

[微信](https://hoxis.github.io/tags/%E5%BE%AE%E4%BF%A1/)

[hexo next 配置 DaoVoice 实现在线聊天功能](https://hoxis.github.io/hexo-next-daovoice.html)
[Ansible 实现批量建立互信](https://hoxis.github.io/ansible-ssh-copy.html)

Emoji | Preview

<https://segmentfault.com/markdown>
回复

快来做第一个评论的人吧~

Powered By [Valine](https://valine.js.org/)
v1.3.4

* 文章目录

* 站点概览

![unknown_filename.7.png](./_resources/1_行代码，实现微信消息发送___pushbear.resources/unknown_filename.7.png)

hoxis

[171 日志](https://hoxis.github.io/archives/)
[19 分类](https://hoxis.github.io/categories/index.html)
[82 标签](https://hoxis.github.io/tags/index.html)

[RSS](https://hoxis.github.io/atom.xml)
[GitHub](https://github.com/hoxis) [知乎](https://www.zhihu.com/people/mobi/posts)

近期文章

* [你应该知道的关于Ansible的15件事](https://hoxis.github.io/15-things-about-ansible.html)
* [Ansible：如何穿过跳板机？](https://hoxis.github.io/ansible-jump-server.html)
* [从URL输入到页面展现到底发生什么？](https://hoxis.github.io/what-happend-when-a-url-input-in-browser.html)
* [Java/Spring使用IPv6地址连接到MySQL服务器](https://hoxis.github.io/ipv6-mysql.html)
* [HAproxy配置IPv6和IPv4的互相代理实验](https://hoxis.github.io/ipv6-haproxy-ipv4.html)

1. [itchat](https://hoxis.github.io/python-serverchan.html#itchat)

* [个人公众号接口](https://hoxis.github.io/python-serverchan.html#%E4%B8%AA%E4%BA%BA%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%A5%E5%8F%A3)

1. [Server 酱](https://hoxis.github.io/python-serverchan.html#Server-%E9%85%B1)

* [PushBear](https://hoxis.github.io/python-serverchan.html#PushBear)

* [总结](https://hoxis.github.io/python-serverchan.html#%E6%80%BB%E7%BB%93)

													
© 2015 — 2019 hoxis
本站已有 15313 位访客 30765 人阅读

0%

0

<https://hoxis.github.io/python-serverchan.html>
[0](https://hoxis.github.io/python-serverchan.html)
**hoxis**
新消息
<https://hoxis.github.io/python-serverchan.html>
<https://hoxis.github.io/python-serverchan.html>

最大上传文档大小：40MB

[_一分钟了解 <u>DaoVoice</u>_](http://blog.daovoice.io/daovocie_manhua/?utm_source=hoxis&utm_campaign=39_campaign&utm_medium=daovoice_widget&utm_term=footer_link&utm_content=one_min) 

_

**hoxis**
<https://hoxis.github.io/python-serverchan.html>
<https://hoxis.github.io/python-serverchan.html>

无对话

[_新信息_](https://hoxis.github.io/python-serverchan.html)

_

**加载中...**
<https://hoxis.github.io/python-serverchan.html>
<https://hoxis.github.io/python-serverchan.html>



_

_





__
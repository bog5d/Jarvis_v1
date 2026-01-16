---
created: 2017-10-27 16:24:19
jarvis_ai_meta:
  key_people:
  - NxnXgpuPSfsIT(itchat作者/发布者)
  - littlecodersh(itchat作者/维护者)
  mood: 关注
  summary: 用户收藏了一篇关于开源微信个人号接口 itchat 的技术文章，介绍了其功能和使用方法。
  tagged_at: '2026-01-11 04:20:45'
  time_space:
    date: '2017-10-27'
    location: V2EX
source: https://www.v2ex.com/t/306804
tags:
- 微信机器人
- 开源项目
- Python
- 技术工具
- itchat
updated: 2017-10-27 16:24:19
---

# 有了 itchat， python 调用微信个人号从未如此简单（新增 py3 支持） - V2EX

# 有了 itchat， python 调用微信个人号从未如此简单（新增 py3 支持）

  [NxnXgpuPSfsIT](https://www.v2ex.com/member/NxnXgpuPSfsIT) · 2016-09-17 20:43:43 +08:00 · 21777 次点击
这是一个创建于 404 天前的主题，其中的信息可能已经有所发展或是发生改变。

itchat 是一个开源的微信个人号接口。

近期完成了 py3 与文档的完善，欢迎各位使用与测试。

使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。

当然，该 api 的使用远不止一个机器人，更多的功能等着你来发现。

如今微信已经成为了个人社交的很大一部分，希望这个项目能够帮助你扩展你的个人的微信号、方便自己的生活。

## Installation

可以通过本命令安装 itchat ：

    pip install itchat
    

## Simple uses

有了 itchat ，如果你想要回复发给自己的文本消息，只需要这样：

    import itchat
    
    @itcaht.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        itchat.send(msg['Text'], msg['FromUserName'])
    
    itchat.auto_login()
    itchat.run()
    

一些进阶应用可以在 Advanced uses 中看到，或者你也可以阅览[文档](https://itchat.readthedocs.org/zh/latest/)。

## Have a try

这是一个基于这一项目的[开源小机器人](https://gist.github.com/littlecodersh/ec8ddab12364323c97d4e36459174f0d)，百闻不如一见，有兴趣可以尝试一下。

![200.jpg](./_resources/有了_itchat，_python_调用微信个人号从未如此简单（新增_py3_支持）_-_V2EX.resources/200.jpg)

## Advanced uses

### 各类型消息的注册

通过如下代码，微信已经可以就日常的各种信息进行获取与回复。

    #coding=utf8
    import itchat, time
    from itchat.content import *
    
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
    def text_reply(msg):
        itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    
    @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
    def download_files(msg):
        msg['Text'](msg['FileName'])
        return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
    
    @itchat.msg_register(FRIENDS)
    def add_friend(msg):
        itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
        itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])
    
    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        if msg['isAt']:
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
    
    itchat.auto_login(True)
    itchat.run()
    

### 命令行二维码

通过以下命令可以在登陆的时候使用命令行显示二维码：

    itchat.auto_login(enableCmdQR=True)
    

部分系统可能字幅宽度有出入，可以通过将 enableCmdQR 赋值为特定的倍数进行调整：

    # 如部分的 linux 系统，块字符的宽度为一个字符（正常应为两字符），故赋值为 2
    itchat.auto_login(enableCmdQR=2)
    

默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将 enableCmdQR 赋值为负值：

    itchat.auto_login(enableCmdQR=-1)
    

### 退出程序后暂存登陆状态

通过如下命令登陆，即使程序关闭，一定时间内重新开启也可以不用重新扫码。

    itchat.auto_login(hotReload=True)
    

### 用户搜索

使用`get_friends`方法可以搜索用户，有四种搜索方式：

1. 仅获取自己的用户信息
2. 获取特定`UserName`的用户信息
3. 获取备注、微信号、昵称中的任何一项等于`name`键值的用户
4. 获取备注、微信号、昵称分别等于相应键值的用户

其中三、四项可以一同使用，下面是示例程序：

    # 获取自己的用户信息，返回自己的属性字典
    itchat.get_friends()
    # 获取特定 UserName 的用户信息
    itchat.get_friends(userName='@abcdefg1234567')
    # 获取任何一项等于 name 键值的用户
    itchat.get_friends(name='littlecodersh')
    # 获取分别对应相应键值的用户
    itchat.get_friends(wechatAccount='littlecodersh')
    # 三、四项功能可以一同使用
    itchat.get_friends(name='LittleCoder 机器人', wechatAccount='littlecodersh')
    

### 附件的下载与发送

itchat 的附件下载方法存储在 msg 的 Text 键中。

发送的文件的文件名（图片给出的默认文件名）都存储在 msg 的 FileName 键中。

下载方法接受一个可用的位置参数（包括文件名），并将文件相应的存储。

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        msg['Text'](msg['FileName'])
        itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
        return '%s received'%msg['Type']
    

如果你不需要下载到本地，仅想要读取二进制串进行进一步处理可以不传入参数，方法将会返回图片的二进制串。

    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
    def download_files(msg):
        with open(msg['FileName'], 'wb') as f:
            f.write(msg['Text']())
    

## FAQ

Q: 为什么中文的文件没有办法上传？

A: 这是由于`requests`的编码问题导致的。若需要支持中文文件传输，将[fields.py](https://gist.github.com/littlecodersh/9a0c5466f442d67d910f877744011705)(py3 版本见[这里](https://gist.github.com/littlecodersh/e93532d5e7ddf0ec56c336499165c4dc))文件放入 requests 包的 packages/urllib3 下即可

Q: 为什么我在设定了`itchat.auto_login()`的`enableCmdQR`为`True`后还是没有办法在命令行显示二维码？

A: 这是由于没有安装可选的包`pillow`，可以使用右边的命令安装：`pip install pillow`

Q: 如何通过这个包将自己的微信号变为控制器？

A: 有两种方式：发送、接受自己 UserName 的消息；发送接收文件传输助手（ filehelper ）的消息

## Comments

如果有什么问题或者建议都可以在这个[Issue](https://github.com/littlecodersh/ItChat/issues/1)和我讨论

或者也可以在 gitter 上交流：
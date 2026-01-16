---
created: 2014-10-20 13:22:44
jarvis_ai_meta:
  key_people: []
  mood: 分享与成就感
  summary: 作者在草榴社区发布原创帖，系统分析并分享了电脑与手机的多种WiFi破解方法及工具。
  tagged_at: '2026-01-11 03:26:05'
  time_space:
    date: '2014-10-20'
    location: 网络论坛（草榴社区）
source: http://1024tg.org/htm_data/7/1409/1217986.html
tags:
- WiFi破解
- 技术分享
- 网络安全
updated: 2014-10-20 13:22:44
---

# [原创]wifi破解方法汇总分析&教程工具分享 草榴社區 - powered by phpwind.net

|     |     |
| --- | --- |
| [**草榴社區**](http://1024tg.org/) |     |

[資料](http://1024tg.org/profile.php) | [短信](http://1024tg.org/message.php) | [搜索](http://1024tg.org/search.php)

|     |     |
| --- | --- |
| .:. **[草榴社區](http://1024tg.org/index.php) » [技術討論區](http://1024tg.org/thread0806.php?fid=7) » \[原创\]wifi破解方法汇总分析&教程工具分享** | **[轉到動態網頁](http://1024tg.org/read.php?fid=7&tid=1217986&toread=1)** |
|     |     |

|     |     |
| --- | --- |
| [＜](http://1024tg.org/read.php?tid=1217986&page=1) **1** [2](http://1024tg.org/read.php?tid=1217986&page=2)[3](http://1024tg.org/read.php?tid=1217986&page=3)[4](http://1024tg.org/read.php?tid=1217986&page=4)[6](http://1024tg.org/read.php?tid=1217986&page=6)[下一頁](http://1024tg.org/read.php?tid=1217986&page=2)[＞](http://1024tg.org/read.php?tid=1217986&page=6) | [回帖](http://1024tg.org/post.php?action=reply&fid=7&tid=1217986) [發布主題](http://1024tg.org/post.php?fid=7) |

|     |     |
| --- | --- |
| \--> **本頁主題:** \[原创\]wifi破解方法汇总分析&教程工具分享 |     |
|     |
|     |     |
|     |

**someshare**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **88**
威望: **11 點**
金錢: **76 USD**
貢獻值: **303 點**
註冊時間:2014-09-05
[資料](http://1024tg.org/profile.php?action=show&uid=307514) [短信](http://1024tg.org/message.php?action=write&touid=307514) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=tpc&article=0) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=tpc&article=0)

#### \[原创\]wifi破解方法汇总分析&教程工具分享

|     |     |
| --- | --- |
| #### 同城学生妹裸聊，线上裸聊，线下做爱<br><br>同城学生妹，丰满性感，脱衣网上做爱，支持线下一夜情，免费注册，立即口爆，爽死你。<br>www.studentshow.com | #### 阿斯顿维拉官方俱乐部主赞助商<br><br>8月12日来自内蒙古包头市的玩家Z\*\*7创纪录的在大发娱乐场累积老虎机游戏Funky Fruits中赢取CNY7,449,761累积大奖；时不与我莫强求，时若来时定珍惜<br>www.dafacasino.com |

<u>论坛里注册了几天了一直想发个帖子，但第一帖怎么也要有点质量才行，今天小狼就来发一个破解wifi的大整理版本（包括手机和电脑破解）</u>
论坛里已经有人分享了一些，破解方法和软件，但是都比较单一，首先我来分析一下破解的总体思路（此处都是个人理解，技术达人有更专业的角度和其他方法欢迎补充）：
先说<u>**电脑破解**</u>，电脑破解有两种思路一种是拦截对方路由器和客户端的数据包，对其进行密码的穷举破解，第二种方法就是用穷举PIN码的方式对路由器进行QSS连接尝试同时得到PIN码和密码；<u>**手机破解**</u>现在也主要有两种方法，一种是wifi万能钥匙的共享方法，使用时你需要打开gprs软件搜索到你附近wifi后在其服务器中匹配是否已经有人共享密码；第二种方法是使用密码穷举的方法对wifi热点进行尝试连接，如幻影wifi
<u>电脑破解破解要求及流程：</u>
**硬件：**需要要一台电脑和一套包括天线、网卡、数据线在内的8187或3070网卡芯片的usb无线网卡套装（100元左右，去网上买）
Ps：有些笔记本内置无线网卡也可破解，主要是看CDLinux里有没有匹配的驱动，指的Linux版本的驱动，我是一点都不懂
**软件：**虚拟机（我用的VMware）、破解系统CDLinux镜像、网卡驱动
可能用到的软件：Inssider（帮助判断信号强弱，如果使用的定向天线和可以帮助调天线方向）、QSS连接工具（可直接输入PIN码连接路由）、U盘启动制作软件unetbootin、EWAS（在windows系统上运行的跑包软件）
**主体流程：**在电脑上安装虚拟机，然后在虚拟机上安装CDlinux系统并运行里边的破解软件进行破解（苹果系统自己找苹果版的虚拟机），具体流程见附件教程
Ps1：当然也可以将虚拟机装到U盘上，然后从U盘启动，但是破解是很费时间的，用虚拟机的话破解的时候你可以用电脑看看电影什么的
Ps2：如果想试下自己的笔记本无线网卡是否支持破解可以用U盘启动的方式，看看CDLinux能否识别网卡
手机破解就需要一台安卓智能机就行了（没玩过苹果），然后下载软件安装使用就行了
<u>下面对各种方法如何选择进行分析</u>
电脑
**跑包：**电脑跑包的速度是非常快的，能够每秒穷举上千个密码，专业跑包能达到每秒几十万的穷举速度，但wifi密码的可能性更是千变万化，而且跑包对电脑损耗较大散热要求高，建议只跑简单密码和有特殊意义的密码组合如生日、电话等
**跑PIN：**PIN码就是一列八位的数字组合，有些路由器为了保证路由器连接的安全，支持一键WPS连接或者Qss连接就是利用的PIN码，我们可以对开启了WPS功能的的路由在有限的八位数字组合中进行穷举连接；缺点：使用这种方法，破解就只是时间问题，所以很多路由器都开发了防PIN功能
手机
**wifi万能钥匙：**破解是很费时间的事，如果已经有人共享了当然是最好的，但使用安装软件是注意有个自动分享密码的选项要取消，否则你就要和邻居分享你自己的网速了
**幻影wifi：**用密码字典穷举进行连接尝试和电脑上对数据包进行破解尝试，幻影wifi每几秒穷举1个密码与电脑跑包速度速度相差甚远，但是手头没有电脑时，或者只想对一些最简单的密码进行尝试时也是一个方便便捷的好方法
ID验证：

![7159da20jw1ek5ynaen19j21kw23u4id.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/7159da20jw1ek5ynaen19j21kw23u4id.jpg) 

附件1：电脑破解大礼包
[http://pan.baidu.com/s/1dDrflM5](http://www.viidii.info/?http://pan______baidu______com/s/1dDrflM5&z)
附件2：幻影wifi最新版（2014.9.9）
[http://pan.baidu.com/s/1gdEHIdd](http://www.viidii.info/?http://pan______baidu______com/s/1gdEHIdd&z)
附件3：wifi万能钥匙最新版（2014.9.9）
[http://pan.baidu.com/s/1qWwOza0](http://www.viidii.info/?http://pan______baidu______com/s/1qWwOza0&z)
本文word下载：
[http://pan.baidu.com/s/1m1Dsq](http://www.viidii.info/?http://pan______baidu______com/s/1m1Dsq&z)
附件里的教程来源网络，从中整理的自己实测可行的部分，在使用过程中进行了修改和补充，有问题欢迎提醒
<u>新手上路第一帖，全文手打，各位大大多多支持，发现问题及时补充</u>

###### Quote:

> wifi万能钥匙 完全不能用了

我试了下我的还是能用

###### Quote:

> 唉，除非是遇到极其简单的密码，否则很难破解

确实是，但设置设置密码的人还是很多的，我手头破解了四个一个生日，一个12345678剩下两个分别是八位和九位的数字组合，而且我都是用跑pin的方法破解的，前期确认可以破解了，后边就是时间了，挂一晚上就ok了

###### Quote:

> 万能钥匙那个感觉就是骗人

就是一个有人共享就可以用的过程，有些人说不是这不是真正意义上的破解，恩，但是可以用（人流量比较大的城市，共享热点会多些）

###### Quote:

> 这个我觉得还是自己用自己的网好

我也是说，当初找破解时因为，要几个月房子，然后觉得就几个月去办宽带开户费都摊不掉；而且玩过破解之后才意识到局域网真的很可怕，只需要一个软件就可以 轻松检测局域网里客户端登陆的网站和账号密码，更不用说那些大神的手段

###### Quote:

> 技术帖，能详细点吗？

我写这个贴子的初衷就是给完全不懂的人做个完整的介绍（至少是我了解到的），至于具体的过程我附件里教程+工具都分享了，而且是我挑选过的，网上也是一搜一堆，完全不用在帖子中赘述

###### Quote:

> 草榴遇上某论坛的朋友，顶一个。之前也有人发过类似的。

我在发帖之前搜索了论坛里的帖子只看到了三个帖子，一个11年的破解wep加密的，一个分享wifi万能钥匙的，一个分享幻影wifi的。
至于本帖，完全手打，如有雷同，纯属巧合

###### Quote:

> 有那么容易破解的话，路由器厂商也能被你们玩死！！！

现在有些品牌的路由就不能跑PIN了，破解也是越来越难啊

###### Quote:

> 貌似都好困难的

个人觉得跑pin最单纯，只要身边信号多，完全可以找个可以跑的慢慢跑

###### Quote:

> 含金量少

上边说了，你说的含金量的东西，网上一大堆，我也在附件里分享了

###### Quote:

> 幻影几率太小，而且费时间！

确实是，现在有个幻影轻巧版，我觉得比正式版更有意义，等下分享在下边

###### Quote:

> 小弟， 你应该做个教程，一步一个图片，不是很多人都会用水滴来破的。跑pin的时候可以上个图

恩，此毒已解
<u>多谢以上大大的回复，第一帖发帖成功</u>
<u>9.10补充1</u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_
幻影wifi轻巧版：
[http://pan.baidu.com/s/1pJv48Q3](http://www.viidii.info/?http://pan______baidu______com/s/1pJv48Q3&z)
回复中说过幻影的轻巧版比正式版更有意义。手机的硬件条件决定，手机破解密码的速度永远无法和电脑相提并论，拿手机破解的意义就在于方便性、灵活性。
轻巧版的的破解形式与正式版的对着一个信号进行不停的穷举破解不同，轻巧版只内置了25个最常出现的简单密码，然后可以选择身边搜索到的信号进行批量破解，这样既增加了破解的几率也避免了手机低速破解所耗费的时间
<u>9.10补充2</u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_
增加一点平常在群里和贴吧里人们常问的问题？怎么看已经连接的wifi的密码？
先说电脑，我的win7系统
![005LGprmjw1ek7qskk5qxj307b02w3yl.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qskk5qxj307b02w3yl.jpg) 
![005LGprmjw1ek7qslc94fj30np0geq5r.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qslc94fj30np0geq5r.jpg) 
![005LGprmjw1ek7qslraamj30ah0bumy5.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qslraamj30ah0bumy5.jpg) 
![005LGprmjw1ek7qsmrx59j30at0d3gmj.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qsmrx59j30at0d3gmj.jpg) 
![005LGprmjw1ek7qsnq8yyj30at0d3wf8.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qsnq8yyj30at0d3wf8.jpg) 
![005LGprmjw1ek7qso4hdhj30at0d3dgr.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/005LGprmjw1ek7qso4hdhj30at0d3dgr.jpg) 
当然要找到密码页面有很多种操作流程，我只是选了我顺手的方法而已
如果你知道路由器的登陆密码，还可以登录路由器在“无线设置-无线安全设置”中找到PSK密码就可以了
手机查看密码首先要有root权限，然后下载一个密码查看器就可以了
\[ 此貼被someshare在2014-09-10 22:43重新編輯 \]
\------------------------
P
[TOP](#) Posted:2014-09-09 13:07 | 回覆 樓主

**yuexiu20081**

級別: 騎士 ( 10 )
精華: **0**
發帖: **3569**
威望: **368 點**
金錢: **0 USD**
貢獻值: **0 點**
註冊時間:2011-06-06
[資料](http://1024tg.org/profile.php?action=show&uid=187120) [短信](http://1024tg.org/message.php?action=write&touid=187120) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35129600&article=1) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35129600&article=1)

|     |     |
| --- | --- |
| #### 国内最大的裸聊室，千名主播等待一脱成名<br><br>一对一真人服务，满足你的一切需求，只需3秒注册即可千名主播中选择你心仪的女神，并且由你玩弄！<br>www.i9158.com | #### 性感可爱的爆乳女神视频裸聊<br><br>E奶绝美天使面孔性感女神只需十元钱就可以由你控制玩弄！淘宝淘女郎倾情加入女主播阵容！曼妙身姿不可不看！线上真人视频选MM！线下真人做爱玩咪咪！<br>www.sexba.com |

感谢发帖，支持一下喽！
[TOP](#) Posted:2014-09-09 13:10 | 回覆 1樓

**鲍鱼汤**
![b10e1cd8jw1ejp8kx0u56j209q08p0sq.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/b10e1cd8jw1ejp8kx0u56j209q08p0sq.jpg)
級別: 精靈王 ( 12 )
精華: **0**
發帖: **13567**
威望: **2206 點**
金錢: **13567 USD**
貢獻值: **7777 點**
註冊時間:2013-12-23
[資料](http://1024tg.org/profile.php?action=show&uid=286675) [短信](http://1024tg.org/message.php?action=write&touid=286675) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35129643&article=2) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35129643&article=2)

|     |     |
| --- | --- |
| #### 想做爱？上我吧！<br><br>想做爱？上我吧！看少妇学生妹疯狂裸聊做爱<br>想一夜情？带我回家吧！同城美女主播覆盖到全国各级乡镇<br>www.wsazx.info | #### 亚洲最大情色视频聊天平台--骚女脱光现场做爱<br><br>找美女裸聊，请到这里来！200名美女宝贝等你畅聊指挥，只有想不到，没有做不到！<br>7\*24小时无间断服务！更有同城一夜情服务！<br>www.newnet.info/gs |

支持
\------------------------
C
[TOP](#) Posted:2014-09-09 13:12 | 回覆 2樓

**cango**

級別: 騎士 ( 10 )
精華: **0**
發帖: **3368**
威望: **521 點**
金錢: **1376 USD**
貢獻值: **405 點**
註冊時間:2013-08-09
[資料](http://1024tg.org/profile.php?action=show&uid=281129) [短信](http://1024tg.org/message.php?action=write&touid=281129) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35129825&article=3) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35129825&article=3)

了解一下
[TOP](#) Posted:2014-09-09 13:19 | 回覆 3樓

**we2e**

級別: 俠客 ( 9 )
精華: **0**
發帖: **943**
威望: **119 點**
金錢: **239 USD**
貢獻值: **45 點**
註冊時間:2011-06-06
[資料](http://1024tg.org/profile.php?action=show&uid=200997) [短信](http://1024tg.org/message.php?action=write&touid=200997) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35129873&article=4) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35129873&article=4)

wifi万能钥匙 完全不能用了
[TOP](#) Posted:2014-09-09 13:20 | 回覆 4樓

**wddwddwdd79**
![49db32ed_36981.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/49db32ed_36981.jpg)
級別: 精靈王 ( 12 )
精華: **0**
發帖: **8056**
威望: **810 點**
金錢: **10 USD**
貢獻值: **17695 點**
註冊時間:2013-12-16
[資料](http://1024tg.org/profile.php?action=show&uid=286371) [短信](http://1024tg.org/message.php?action=write&touid=286371) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35129921&article=5) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35129921&article=5)

唉，除非是遇到极其简单的密码，否则很难破解
[TOP](#) Posted:2014-09-09 13:23 | 回覆 5樓

**Eternitylove**
![460.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/460.jpg)
級別: 精靈王 ( 12 )
精華: **0**
發帖: **18946**
威望: **1689 點**
金錢: **364 USD**
貢獻值: **697 點**
註冊時間:2012-04-15
[資料](http://1024tg.org/profile.php?action=show&uid=249395) [短信](http://1024tg.org/message.php?action=write&touid=249395) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130085&article=6) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130085&article=6)

万能钥匙那个感觉就是骗人
\------------------------
$
[TOP](#) Posted:2014-09-09 13:29 | 回覆 6樓

**白菜乐**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **279**
威望: **31 點**
金錢: **11 USD**
貢獻值: **14 點**
註冊時間:2012-05-21
[資料](http://1024tg.org/profile.php?action=show&uid=255182) [短信](http://1024tg.org/message.php?action=write&touid=255182) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130097&article=7) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130097&article=7)

1024
[TOP](#) Posted:2014-09-09 13:30 | 回覆 7樓

**坏小蛋**
![]()
級別: 禁止發言 ( 8 )
精華: **0**
發帖: **6870**
威望: **960 點**
金錢: **138 USD**
貢獻值: **941 點**
註冊時間:2011-06-06
[資料](http://1024tg.org/profile.php?action=show&uid=199108) [短信](http://1024tg.org/message.php?action=write&touid=199108) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130176&article=8) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130176&article=8)

谢谢分享
[TOP](#) Posted:2014-09-09 13:33 | 回覆 8樓

**洞态美**

級別: 俠客 ( 9 )
精華: **0**
發帖: **1094**
威望: **110 點**
金錢: **1 USD**
貢獻值: **0 點**
註冊時間:2012-02-21
[資料](http://1024tg.org/profile.php?action=show&uid=243824) [短信](http://1024tg.org/message.php?action=write&touid=243824) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130210&article=9) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130210&article=9)

感谢发帖，支持!
[TOP](#) Posted:2014-09-09 13:34 | 回覆 9樓

**长醉独眠**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **567**
威望: **57 點**
金錢: **63 USD**
貢獻值: **0 點**
註冊時間:2014-07-16
[資料](http://1024tg.org/profile.php?action=show&uid=302346) [短信](http://1024tg.org/message.php?action=write&touid=302346) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130287&article=10) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130287&article=10)

1024
[TOP](#) Posted:2014-09-09 13:37 | 回覆 10樓

**qc2t**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **809**
威望: **83 點**
金錢: **9 USD**
貢獻值: **351 點**
註冊時間:2014-06-02
[資料](http://1024tg.org/profile.php?action=show&uid=298370) [短信](http://1024tg.org/message.php?action=write&touid=298370) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130355&article=11) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130355&article=11)

|     |     |
| --- | --- |
| #### 全国上门援交服务-视频选妞！<br><br>上门援交服务升级啦！可以在线视频选妞，拒绝虚假照片，相当方便和贴心，VIP用户还可以全裸选妞，看完脸蛋看身材！<br>www.showgirl.cc | #### 名汇国际娱乐城→《国际品牌.玩家首选》<br><br>澳门合法赌场，最刺激的网上真人真钱赌博实心梅花(纸牌)实心方块(纸牌)＜百家乐 彩票 3D玉蒲团 金瓶梅 大型电玩＞名汇国际月月百万疯狂派送，现在注册下一个百万富翁就是您。<br>www.8377.com |

1024
[TOP](#) Posted:2014-09-09 13:40 | 回覆 11樓

**metalgrape**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **4**
威望: **1 點**
金錢: **4 USD**
貢獻值: **0 點**
註冊時間:2014-09-08
[資料](http://1024tg.org/profile.php?action=show&uid=308118) [短信](http://1024tg.org/message.php?action=write&touid=308118) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130362&article=12) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130362&article=12)

1024
[TOP](#) Posted:2014-09-09 13:40 | 回覆 12樓

**超级大太法师**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **225**
威望: **53 點**
金錢: **226 USD**
貢獻值: **0 點**
註冊時間:2014-07-25
[資料](http://1024tg.org/profile.php?action=show&uid=302927) [短信](http://1024tg.org/message.php?action=write&touid=302927) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130368&article=13) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130368&article=13)

1024

* * *

由Android客戶端發表 v1.5.2
[TOP](#) Posted:2014-09-09 13:40 | 回覆 13樓

**威猛先生**
![c1540e25jw1e4echdlsevg206o08wwi0.gif](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/c1540e25jw1e4echdlsevg206o08wwi0.gif)
級別: 聖騎士 ( 11 )
精華: **0**
發帖: **1551**
威望: **433 點**
金錢: **27 USD**
貢獻值: **16871 點**
註冊時間:2011-06-06
[資料](http://1024tg.org/profile.php?action=show&uid=86274) [短信](http://1024tg.org/message.php?action=write&touid=86274) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130372&article=14) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130372&article=14)

这个我觉得还是自己用自己的网好
[TOP](#) Posted:2014-09-09 13:41 | 回覆 14樓

**apple155148**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **142**
威望: **15 點**
金錢: **13 USD**
貢獻值: **0 點**
註冊時間:2014-06-27
[資料](http://1024tg.org/profile.php?action=show&uid=301004) [短信](http://1024tg.org/message.php?action=write&touid=301004) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130462&article=15) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130462&article=15)

技术帖，能详细点吗？
[TOP](#) Posted:2014-09-09 13:44 | 回覆 15樓

**sintian**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **3**
威望: **1 點**
金錢: **3 USD**
貢獻值: **0 點**
註冊時間:2014-07-17
[資料](http://1024tg.org/profile.php?action=show&uid=302409) [短信](http://1024tg.org/message.php?action=write&touid=302409) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130468&article=16) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130468&article=16)

草榴遇上某论坛的朋友，顶一个。之前也有人发过类似的。
[TOP](#) Posted:2014-09-09 13:45 | 回覆 16樓

**ljd356**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **60**
威望: **7 點**
金錢: **60 USD**
貢獻值: **0 點**
註冊時間:2014-06-18
[資料](http://1024tg.org/profile.php?action=show&uid=300062) [短信](http://1024tg.org/message.php?action=write&touid=300062) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130650&article=17) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130650&article=17)

|     |     |
| --- | --- |
| #### 大陆聊天室校花兼职，等你来约上床<br><br>各大高校校花兼职援交，免费注册后即可开始视频挑选，每天前2000名用户可以全裸选妞！你还等什么！赶快加入我们！<br>www.ixiaohua.com | #### 裸聊俱乐部会员招募中--赶紧行动吧<br><br>找刺激就来裸聊俱乐部，这里是男人的天堂，俱乐部里寂寞难耐的少妇、学生妹、制服空姐应有尽有<br>点击注册，即可面对面与美女视频裸聊……<br>www.micedy.info/bh |

1024
[TOP](#) Posted:2014-09-09 13:51 | 回覆 17樓

**冷面杀手**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **329**
威望: **35 點**
金錢: **47 USD**
貢獻值: **304 點**
註冊時間:2014-05-20
[資料](http://1024tg.org/profile.php?action=show&uid=297138) [短信](http://1024tg.org/message.php?action=write&touid=297138) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130745&article=18) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130745&article=18)

有那么容易破解的话，路由器厂商也能被你们玩死！！！
\------------------------
O
[TOP](#) Posted:2014-09-09 13:56 | 回覆 18樓

**成宇**
![6613738320121212213126070.jpg](./_resources/原创wifi破解方法汇总分析&教程工具分享_草榴社區_-_powered_by_phpwind.ne.resources/6613738320121212213126070.jpg)
級別: 精靈王 ( 12 )
精華: **0**
發帖: **9388**
威望: **1024 點**
金錢: **126 USD**
貢獻值: **17113 點**
註冊時間:2012-06-17
[資料](http://1024tg.org/profile.php?action=show&uid=258631) [短信](http://1024tg.org/message.php?action=write&touid=258631) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130747&article=19) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130747&article=19)

貌似都好困难的
\------------------------
D
[TOP](#) Posted:2014-09-09 13:56 | 回覆 19樓

**j173077chen**

級別: 騎士 ( 10 )
精華: **0**
發帖: **4536**
威望: **454 點**
金錢: **316 USD**
貢獻值: **33 點**
註冊時間:2014-02-19
[資料](http://1024tg.org/profile.php?action=show&uid=290441) [短信](http://1024tg.org/message.php?action=write&touid=290441) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130766&article=20) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130766&article=20)

支持原创

* * *

由Android客戶端發表 v1.5.2
[TOP](#) Posted:2014-09-09 13:57 | 回覆 20樓

**八两爱半斤姐**

級別: 騎士 ( 10 )
精華: **0**
發帖: **5740**
威望: **585 點**
金錢: **116 USD**
貢獻值: **0 點**
註冊時間:2011-09-22
[資料](http://1024tg.org/profile.php?action=show&uid=228130) [短信](http://1024tg.org/message.php?action=write&touid=228130) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35130936&article=21) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35130936&article=21)

含金量少
[TOP](#) Posted:2014-09-09 14:03 | 回覆 21樓

**方圓盛世**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **193**
威望: **20 點**
金錢: **52 USD**
貢獻值: **9 點**
註冊時間:2010-02-21
[資料](http://1024tg.org/profile.php?action=show&uid=79546) [短信](http://1024tg.org/message.php?action=write&touid=79546) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35131272&article=22) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35131272&article=22)

1024
[TOP](#) Posted:2014-09-09 14:14 | 回覆 22樓

**yaok79930**

級別: 新手上路 ( 8 )
精華: **0**
發帖: **132**
威望: **14 點**
金錢: **2 USD**
貢獻值: **1 點**
註冊時間:2011-06-06
[資料](http://1024tg.org/profile.php?action=show&uid=124295) [短信](http://1024tg.org/message.php?action=write&touid=124295) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35131353&article=23) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35131353&article=23)

|     |     |
| --- | --- |
| #### 【凤凰国际】老品牌高品质值得信赖<br><br>国际品牌 信誉保证，真人真钱赌博，百家乐，轮盘，龙虎斗，温州牌九，21点等，百万提款1分钟到账，视讯直播，真人娱乐，在线美女荷官，打造顶级线上博彩娱乐城！<br>www.87n.com | #### 线上娱乐城第一品牌，真人美女荷官与您相约<br><br>首存注册充值即送高额奖金，世界杯，五大联赛体育赛事投注。结算飞快！真人美女百家乐,轮盘,龙虎斗，温州牌九，21点等。高赔率，信誉好，取款快！！<br>www.8757.com |

1024
[TOP](#) Posted:2014-09-09 14:18 | 回覆 23樓

**lllxkiss**

級別: 俠客 ( 9 )
精華: **0**
發帖: **2137**
威望: **222 點**
金錢: **432 USD**
貢獻值: **1380 點**
註冊時間:2014-05-29
[資料](http://1024tg.org/profile.php?action=show&uid=297953) [短信](http://1024tg.org/message.php?action=write&touid=297953) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1217986&pid=35131452&article=24) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1217986) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1217986&pid=35131452&article=24)

支持了
[TOP](#) Posted:2014-09-09 14:21 | 回覆 24樓

|     |     |
| --- | --- |
| [＜](http://1024tg.org/read.php?tid=1217986&page=1) **1** [2](http://1024tg.org/read.php?tid=1217986&page=2)[3](http://1024tg.org/read.php?tid=1217986&page=3)[4](http://1024tg.org/read.php?tid=1217986&page=4)[6](http://1024tg.org/read.php?tid=1217986&page=6)[下一頁](http://1024tg.org/read.php?tid=1217986&page=2)[＞](http://1024tg.org/read.php?tid=1217986&page=6) |     |
| .:. **[草榴社區](http://1024tg.org/htm_data/7/1409/index.php) -> [技術討論區](http://1024tg.org/thread0806.php?fid=7)** |

|     |     |     |
| --- | --- | --- |
| **快速發帖** |     | [__頂端__](#) |
| **內容**：<br>HTML 代碼不可用<br>使用簽名<br>Wind Code自動轉換 | 按 Ctrl+Enter 直接提交 |     |

|     |     |
| --- | --- |
| #### 台湾裸聊+一夜情 先裸聊后做爱！<br><br>新到20位七星级主播，明星脸，馒头B，F罩杯， 水多B紧！速配同城主播 能裸聊能出台能搞，VIP会员火爆招募中，可免费试玩！<br>www.aifei.info | #### 台湾甜心优质美女全裸服务<br><br>预约上门，7X24小时在线视频选台妹，肤白爆乳，天使面孔，选择属于你的私人定制。<br>www.twshow.tw |

Powered by **PHPWind** **v5.3** Code © 2003-07
This is html template view this page faster
[站长统计](http://www.cnzz.com/stat/website.php?web_id=950900)\-[当前在线40464](http://www.cnzz.com/stat/website.php?web_id=950900&method=online)
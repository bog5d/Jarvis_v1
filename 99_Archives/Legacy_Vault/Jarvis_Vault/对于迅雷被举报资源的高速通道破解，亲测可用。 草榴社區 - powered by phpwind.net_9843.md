---
created: 2014-10-06 21:42:17
jarvis_ai_meta:
  key_people: []
  mood: 好奇、兴奋、成就感
  summary: 用户通过分析迅雷本地数据库文件，成功破解了被举报资源无法使用高速通道的限制。
  tagged_at: '2026-01-11 03:45:10'
  time_space:
    date: '2014-09-24'
    location: ''
source: http://1024tg.org/htm_data/7/1409/1230208.html
tags:
- SQLite
- 技术分析
- 迅雷
- 破解
- 高速通道
updated: 2014-10-06 21:42:17
---

# 对于迅雷被举报资源的高速通道破解，亲测可用。 草榴社區 - powered by phpwind.net

**头文字D**

級別: 禁止發言 ( 8 )
精華: **0**
發帖: **63**
威望: **45 點**
金錢: **441 USD**
貢獻值: **0 點**
註冊時間:2014-03-31
[資料](http://1024tg.org/profile.php?action=show&uid=292833) [短信](http://1024tg.org/message.php?action=write&touid=292833) [引用](http://1024tg.org/post.php?action=quote&fid=7&tid=1230208&pid=tpc&article=0) [推薦](http://1024tg.org/sendemail.php?action=tofriend&tid=1230208) [編輯](http://1024tg.org/post.php?action=modify&fid=7&tid=1230208&pid=tpc&article=0)

#### 对于迅雷被举报资源的高速通道破解，亲测可用。

|     |     |
| --- | --- |
| #### 阿斯顿维拉官方俱乐部主赞助商<br><br>8月12日来自内蒙古包头市的玩家Z\*\*7创纪录的在大发娱乐场累积老虎机游戏Funky Fruits中赢取CNY7,449,761累积大奖；时不与我莫强求，时若来时定珍惜<br>www.dafacasino.com | #### 全国上门援交服务-视频选妞！<br><br>上门援交服务升级啦！可以在线视频选妞，拒绝虚假照片，相当方便和贴心，VIP用户还可以全裸选妞，看完脸蛋看身材！<br>www.showgirl.cc |

破解思路：有一次下资源的时候开高速通道发现被举报了，于是出于对于早已续费3年会员而不能得到服务的愤慨我就点了“重试”近十来次
突然就进高速通道了（当然破解方法不会这么靠概率），即便是暂停或者重启迅雷，仍然可以继续加速。
恩，于是我就好奇的整了整，结果喜闻乐见。
 [![20140923143333rz62h.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143333rz62h.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143333rz62h______jpegg4______html&z) 
因为重启或者暂停之后高速通道的显示是这样的，我就想会不会是迅雷把已经成功进入通道的加入了某个列表（保证不会重复扣流量）。
我就屁颠屁颠的去找这个东西了，结果找到了。
位于迅雷主文件夹Thunder Network\\Thunder\\Profile的这里。
有一个叫TaskDb.dat的文件，用ultraedit打开后基本上是乱码，开始略沮丧，想看看是不是有别的办法（修改句柄之类的）
不过突然我瞄到了这个东西 [![20140923143335bwko9.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143335bwko9.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143335bwko9______jpegg4______html&z) SQLite format 3，便会心一笑
于是从我混乱的桌面上瞬间找到了这个东西（还正好就在迅雷的边上，真心巧。。。。之前怎么就没发现呢）
 [![20140923143338lxev6.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143338lxev6.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143338lxev6______jpegg4______html&z) 
正文：
Step 1.
添加任务→点击（一定要点）进入高速通道
会出现两种情况
→成功进入高速通道→加速完毕
→该资源被举报，无法添加……，服务器忙，请…… 等诸如此类的，暂停任务后关闭迅雷，转Step 2
Step 2.
用SQLite Expert Professional打开位于X:\\Program Files (x86)\\Thunder Network\\Thunder\\Profiles目录下的TaskDb.dat文件 （X为你迅雷的安装分区）
 [![20140923143340rmvm1.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143340rmvm1.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143340rmvm1______jpegg4______html&z) 
Step 3.
找到左边SQL表中 AcclerateTaskMapxxxxsuperspeed 一项
 [![20140923143342qpa7k.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143342qpa7k.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143342qpa7k______jpegg4______html&z) 
此时右边栏会出现你已经 进入高速通道，或者进入失败的任务列表
Step 4.
右键单击UserData列下的数据，选择Text Editor进行编辑
 [![20140923143344hgphc.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143344hgphc.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143344hgphc______jpegg4______html&z) 
Step 5.
此时会弹出一个窗口，我们将Result后面的508或者500等其它结果改成0，点击OK保存即可。
 [![20140923143346122g2.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143346122g2.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143346122g2______jpegg4______html&z) 
 [![201409231433485ks5b.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/201409231433485ks5b.jpeg)](http://www.viidii.info/?http://ipoock______com/view/201409231433485ks5b______jpegg4______html&z) 
Step 6.
重新启动迅雷，你会发现原来任务显示的被举报已经变成了这个 [![2014092314361320gw6.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/2014092314361320gw6.jpeg)](http://www.viidii.info/?http://ipoock______com/view/2014092314361320gw6______jpegg4______html&z)  
把暂停的任务直接继续即可，你会发现高速通道已经用上了。
 [![20140923143611ykuxg.jpeg](./_resources/对于迅雷被举报资源的高速通道破解，亲测可用。_草榴社區_-_powered_by_phpwind.n.resources/20140923143611ykuxg.jpeg)](http://www.viidii.info/?http://ipoock______com/view/20140923143611ykuxg______jpegg4______html&z) 
注：非BT任务需要启动任务之后 再暂停→再继续即可
[TOP](#) Posted:2014-09-24 09:33 | 回覆 樓主
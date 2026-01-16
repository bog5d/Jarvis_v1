---
created: 2018-03-02 07:38:06
jarvis_ai_meta:
  key_people: []
  mood: 平静
  summary: 作者（东围居士）在博客中分享了使用pandas的isin()方法筛选DataFrame特定行，并介绍了如何间接实现排除特定行的技巧。
  tagged_at: '2026-01-11 02:36:35'
  time_space:
    date: '2016-11-29'
    location: ''
source: https://www.cnblogs.com/wuzhiblog/p/python_pandas.html
tags:
- DataFrame
- 数据处理
- 数据分析
- Python
- pandas
updated: 2018-03-02 07:38:06
---

# isin可以用来找特定行列

<https://www.cnblogs.com/wuzhiblog/p/python_pandas.html>

[![unknown_filename.2.gif](./_resources/isin可以用来找特定行列.resources/unknown_filename.2.gif)](http://www.cnblogs.com/wuzhiblog/)

# [青冥绿水](http://www.cnblogs.com/wuzhiblog/)

## 无冥冥之志者无昭昭之明，无惛惛之事者无赫赫之功

* [博客园](http://www.cnblogs.com/)

* [首页](http://www.cnblogs.com/wuzhiblog/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E4%B8%9C%E5%9B%B4%E5%B1%85%E5%A3%AB)
* [订阅](http://www.cnblogs.com/wuzhiblog/rss)
* [管理](https://i.cnblogs.com/)

随笔 - 34 文章 - 0 评论 - 5

# [pandas.DataFrame排除特定行](http://www.cnblogs.com/wuzhiblog/p/python_pandas.html)

使用Python进行数据分析时，经常要使用到的一个数据结构就是pandas的DataFrame

如果我们想要像Excel的筛选那样，只要其中的一行或某几行，可以使用`isin()`方法，将需要的行的值以列表方式传入，还可以传入字典，指定列进行筛选。

但是如果我们只想要所有内容中不包含特定行的内容，却并没有一个_isnotin()_方法。我今天的工作就遇到了这样的需求，经常查找之后，发现只能换种方式使用`isin()`来实现这个需求。

示例如下：

    In [3]: df = pd.DataFrame([['GD', 'GX', 'FJ'], ['SD', 'SX', 'BJ'], ['HN', 'HB'
       ...: , 'AH'], ['HEN', 'HEN', 'HLJ'], ['SH', 'TJ', 'CQ']], columns=['p1', 'p2
       ...: ', 'p3'])
    
    In [4]: df
    Out[4]:
        p1   p2   p3
    0   GD   GX   FJ
    1   SD   SX   BJ
    2   HN   HB   AH
    3  HEN  HEN  HLJ
    4   SH   TJ   CQ

如果只想要p1为GD和HN的两行，可以这么做：

    In [8]: df[df.p1.isin(['GD', 'HN'])]
    Out[8]:
       p1  p2  p3
    0  GD  GX  FJ
    2  HN  HB  AH

但是如果我们想要除了这两行之外的数据，就需要绕点路了。
原理是先把p1取出并转换为列表，然后再从列表中去不需要的行（值）去除，然后再在DataFrame中使用isin()

    In [9]: ex_list = list(df.p1)
    
    In [10]: ex_list.remove('GD')
    
    In [11]: ex_list.remove('HN')
    
    In [12]: ex_list
    Out[12]: ['SD', 'HEN', 'SH']
    
    In [13]: df[df.p1.isin(ex_list)]
    Out[13]:
        p1   p2   p3
    1   SD   SX   BJ
    3  HEN  HEN  HLJ
    4   SH   TJ   CQ

（本文完）
\--------------------------------------------------------------------------------------------------------------------------
致虚极，守静笃
使用我的阿里云幸运券，购买阿里云ECS有优惠：[阿里云幸运券](https://promotion.aliyun.com/ntms/act/ambassador/sharetouser.html?userCode=6m0isjjt&utm_source=6m0isjjt)

分类: [Python](http://www.cnblogs.com/wuzhiblog/category/915862.html)
标签: [pandas](http://www.cnblogs.com/wuzhiblog/tag/pandas/), [python](http://www.cnblogs.com/wuzhiblog/tag/python/), [数据分析](http://www.cnblogs.com/wuzhiblog/tag/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/), [数据处理](http://www.cnblogs.com/wuzhiblog/tag/%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86/), [DataFrame](http://www.cnblogs.com/wuzhiblog/tag/DataFrame/), [isin()](http://www.cnblogs.com/wuzhiblog/tag/isin()/)

好文要顶 关注我 收藏该文 ![unknown_filename.5.png](./_resources/isin可以用来找特定行列.resources/unknown_filename.5.png) ![unknown_filename.1.png](./_resources/isin可以用来找特定行列.resources/unknown_filename.1.png)

[![unknown_filename.jpeg](./_resources/isin可以用来找特定行列.resources/unknown_filename.jpeg)](http://home.cnblogs.com/u/wuzhiblog/)
[东围居士](http://home.cnblogs.com/u/wuzhiblog/)
[关注 - 1](http://home.cnblogs.com/u/wuzhiblog/followees)
[粉丝 - 6](http://home.cnblogs.com/u/wuzhiblog/followers)

+加关注

0
0

[«](http://www.cnblogs.com/wuzhiblog/p/pythonexcel.html) 上一篇：[Python 操作 MS Excel 文件](http://www.cnblogs.com/wuzhiblog/p/pythonexcel.html)
[»](http://www.cnblogs.com/wuzhiblog/p/python_new_row_or_col.html) 下一篇：[pandas.DataFrame对行和列求和及添加新行和列](http://www.cnblogs.com/wuzhiblog/p/python_new_row_or_col.html)

posted @ 2016-11-29 10:40 [东围居士](http://www.cnblogs.com/wuzhiblog/) 阅读(11602) 评论(2) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=6112614) [收藏](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#)

<https://www.cnblogs.com/wuzhiblog/p/python_pandas.html>
[评论列表](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html)
<https://www.cnblogs.com/wuzhiblog/p/python_pandas.html>
 <https://www.cnblogs.com/wuzhiblog/p/python_pandas.html> [#1楼](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#3819364) [2017-10-23 21:32](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html) [画檐蛛网](http://home.cnblogs.com/u/1041143/) <http://msg.cnblogs.com/send/%E7%94%BB%E6%AA%90%E8%9B%9B%E7%BD%91> 

如果要查找的是包含‘G’的行呢？请赐教
支持(0)反对(0)

[#2楼](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#3823488)[楼主 2017-10-27 13:42](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html) [东围居士](http://www.cnblogs.com/wuzhiblog/) <http://msg.cnblogs.com/send/%E4%B8%9C%E5%9B%B4%E5%B1%85%E5%A3%AB> 

[@](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#3819364) 画檐蛛网
用Series.str.contains("G")
支持(0)反对(0)

<https://www.cnblogs.com/wuzhiblog/p/python_pandas.html>
<https://www.cnblogs.com/wuzhiblog/p/python_pandas.html>刷新评论[刷新页面](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#)[返回顶部](https://www.cnblogs.com/wuzhiblog/p/python_pandas.html#top)

注册用户登录后才能发表评论，请 登录 或 注册，[访问](http://www.cnblogs.com/)网站首页。

[【推荐】超50万VC++源码: 大型工控、组态仿真、建模CAD源码2018！](http://www.ucancode.com/index.htm)
[【活动】杭州云栖·2050大会-全世界年青人因科技而团聚-源点](https://www.cnblogs.com/cmt/p/8462669.html)
[【抢购】新注册用户域名抢购1元起](https://dnspod.cloud.tencent.com/act/yearendsales?from=IT&fromSource=gwzcw.781137.781137.781137)

[![unknown_filename.3.jpeg](./_resources/isin可以用来找特定行列.resources/unknown_filename.3.jpeg)](https://dnspod.cloud.tencent.com/act/weapp?fromSource=gwzcw.781158.781158.781158)

**最新IT新闻**:
· [雷军最新单曲上线：如此鬼畜 境界无敌](https://news.cnblogs.com/n/590817/)
· [乐视网：贾跃亭所有股票质押式回购交易均已违约](https://news.cnblogs.com/n/590806/)
· [Spotify未来靠何生存？ 或需涉足硬件业务推智能音箱](https://news.cnblogs.com/n/590811/)
· [股东大会下周二召开 高通和博通发起股东争夺战](https://news.cnblogs.com/n/590810/)
· [区块链公司密集注册 2月份共55家公司名称获预先核准](https://news.cnblogs.com/n/590809/)
» [更多新闻...](http://news.cnblogs.com/)

[![unknown_filename.4.jpeg](./_resources/isin可以用来找特定行列.resources/unknown_filename.4.jpeg)](http://click.aliyun.com/m/34770/)

**最新知识库文章**:
· [写给自学者的入门指南](http://kb.cnblogs.com/page/575255/)
· [和程序员谈恋爱](http://kb.cnblogs.com/page/578690/)
· [学会学习](http://kb.cnblogs.com/page/585734/)
· [优秀技术人的管理陷阱](http://kb.cnblogs.com/page/588938/)
· [作为一个程序员，数学对你到底有多重要](http://kb.cnblogs.com/page/590141/)

» [更多知识库文章...](http://kb.cnblogs.com/)

### 公告

[<u>>>>>> 阿里云优惠 <<<<<</u>](https://promotion.aliyun.com/ntms/act/ambassador/sharetouser.html?userCode=6m0isjjt&utm_source=6m0isjjt)
昵称：[东围居士](https://home.cnblogs.com/u/wuzhiblog/)
园龄：[1年8个月](https://home.cnblogs.com/u/wuzhiblog/)
粉丝：[6](https://home.cnblogs.com/u/wuzhiblog/followers/)
关注：[1](https://home.cnblogs.com/u/wuzhiblog/followees/)
+加关注

|     |     |     |
| --- | --- | --- |
| <   | 2018年3月 | >   |

日一二三四五六25262728123456789101112131415161718192021222324252627282930311234567

### 搜索

### 常用链接

* [我的随笔](http://www.cnblogs.com/wuzhiblog/p/)

* [我的评论](http://www.cnblogs.com/wuzhiblog/MyComments.html)
* [我的参与](http://www.cnblogs.com/wuzhiblog/OtherPosts.html)
* [最新评论](http://www.cnblogs.com/wuzhiblog/RecentComments.html)
* [我的标签](http://www.cnblogs.com/wuzhiblog/tag/)

### 我的标签

* [python](http://www.cnblogs.com/wuzhiblog/tag/python/)(14)

* [excel](http://www.cnblogs.com/wuzhiblog/tag/excel/)(12)
* [VBA](http://www.cnblogs.com/wuzhiblog/tag/VBA/)(12)
* [office](http://www.cnblogs.com/wuzhiblog/tag/office/)(6)
* [fedora](http://www.cnblogs.com/wuzhiblog/tag/fedora/)(4)
* [linux](http://www.cnblogs.com/wuzhiblog/tag/linux/)(4)
* [MySQL](http://www.cnblogs.com/wuzhiblog/tag/MySQL/)(2)
* [pandas](http://www.cnblogs.com/wuzhiblog/tag/pandas/)(2)
* [DataFrame](http://www.cnblogs.com/wuzhiblog/tag/DataFrame/)(2)
* [scrapy](http://www.cnblogs.com/wuzhiblog/tag/scrapy/)(2)
* [更多](http://www.cnblogs.com/wuzhiblog/tag/)

### 随笔分类

* [Git(1)](http://www.cnblogs.com/wuzhiblog/category/1027399.html)

* [Office(12)](http://www.cnblogs.com/wuzhiblog/category/939333.html)
* [Python(14)](http://www.cnblogs.com/wuzhiblog/category/915862.html)
* [R(1)](http://www.cnblogs.com/wuzhiblog/category/1016890.html)
* [使用技巧(3)](http://www.cnblogs.com/wuzhiblog/category/1056421.html)

### 随笔档案

* [2018年2月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2018/02.html)

* [2018年1月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2018/01.html)
* [2017年12月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2017/12.html)
* [2017年11月 (9)](http://www.cnblogs.com/wuzhiblog/archive/2017/11.html)
* [2017年10月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2017/10.html)
* [2017年9月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2017/09.html)
* [2017年8月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2017/08.html)
* [2017年7月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2017/07.html)
* [2017年6月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2017/06.html)
* [2017年5月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2017/05.html)
* [2017年3月 (3)](http://www.cnblogs.com/wuzhiblog/archive/2017/03.html)
* [2017年2月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2017/02.html)
* [2017年1月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2017/01.html)
* [2016年12月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2016/12.html)
* [2016年11月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2016/11.html)
* [2016年7月 (1)](http://www.cnblogs.com/wuzhiblog/archive/2016/07.html)
* [2016年6月 (2)](http://www.cnblogs.com/wuzhiblog/archive/2016/06.html)

### 最新评论

* [1. Re:Excel VBA入门（二）数组和字典](http://www.cnblogs.com/wuzhiblog/p/vba_two.html#3908273)

* 谢博主，简单明了。
* \--AutoDev
* [2. Re:pandas.DataFrame排除特定行](http://www.cnblogs.com/wuzhiblog/p/python_pandas.html#3823488)
* @画檐蛛网用Series.str.contains("G")...
* \--吴志
* [3. Re:pandas.DataFrame排除特定行](http://www.cnblogs.com/wuzhiblog/p/python_pandas.html#3819364)
* 如果要查找的是包含‘G’的行呢？请赐教
* \--画檐蛛网
* [4. Re:U盘安装Fedora 24时出现的几个问题及解决办法](http://www.cnblogs.com/wuzhiblog/p/7345913.html#3755713)
* @Untitled多谢提醒。下次重装的时候我再试试。主要是我之前用的也是24，装时刚出来不久。然后在使用时（包括启动和关闭）会出现各种错误警告，虽然不影响正常使用，但还是觉得有点不爽。所以怕是因为版本......
* \--吴志
* [5. Re:U盘安装Fedora 24时出现的几个问题及解决办法](http://www.cnblogs.com/wuzhiblog/p/7345913.html#3755703)
* 1\. USB用dd来做
	2\. Fedora 24已经不再支持了，26都发布了
* \--Untitled

### 阅读排行榜

* [1. pandas.DataFrame对行和列求和及添加新行和列(26152)](http://www.cnblogs.com/wuzhiblog/p/python_new_row_or_col.html)

* [2. pandas.DataFrame排除特定行(11601)](http://www.cnblogs.com/wuzhiblog/p/python_pandas.html)
* [3. Excel、VBA与MySQL交互(5706)](http://www.cnblogs.com/wuzhiblog/p/VBA_Excel_Mysql.html)
* [4. QQ空间动态爬虫(2992)](http://www.cnblogs.com/wuzhiblog/p/qqzone_crawler.html)
* [5. Excel VBA入门（二）数组和字典(2833)](http://www.cnblogs.com/wuzhiblog/p/vba_two.html)

### 评论排行榜

* [1. pandas.DataFrame排除特定行(2)](http://www.cnblogs.com/wuzhiblog/p/python_pandas.html)

* [2. U盘安装Fedora 24时出现的几个问题及解决办法(2)](http://www.cnblogs.com/wuzhiblog/p/7345913.html)
* [3. Excel VBA入门（二）数组和字典(1)](http://www.cnblogs.com/wuzhiblog/p/vba_two.html)

### 推荐排行榜

* [1. QQ空间动态爬虫(2)](http://www.cnblogs.com/wuzhiblog/p/qqzone_crawler.html)

* [2. pandas.DataFrame对行和列求和及添加新行和列(1)](http://www.cnblogs.com/wuzhiblog/p/python_new_row_or_col.html)
* [3. SMTPSenderRefused: (530, ‘5.5.1 Authentication Required. Learn more at n5.5.1(1)](http://www.cnblogs.com/wuzhiblog/p/6535535.html)

Copyright ©2018 东围居士
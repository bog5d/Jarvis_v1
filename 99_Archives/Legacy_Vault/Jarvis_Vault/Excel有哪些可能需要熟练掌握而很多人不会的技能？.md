---
created: 2015-04-26 18:22:14
jarvis_ai_meta:
  key_people:
  - 刘万祥(ExcelPro博主)
  mood: 自信、分享、热情
  summary: 作者分享Excel高级图表制作技巧，通过详细案例演示如何将Excel元素融入图表设计。
  tagged_at: '2026-01-11 02:35:49'
  time_space:
    date: '2015-04-26'
    location: ''
tags:
- 数据可视化
- 图表设计
- Excel
- 商务图表
- VBA
updated: 2015-05-05 17:09:55
---

# Excel有哪些可能需要熟练掌握而很多人不会的技能？

分享我新建的Blog， 会以思维导图的方式分享一些读书笔记，欢迎访问并关注。
[MindMapSharing_新浪博客](http://blog.sina.com.cn/chasedream27)
\--------------
回答有些长，为节约大家的时间，我选取了一个经典案例，辅以详细的说明（中文版Excel2013）放在开头，没时间看全部回答的品一下这个案例就好了。
这个案例充分体现了“**将Excel的元素融入图表**”的技巧。以下商业杂志图表均利用了这一技巧。

![unknown_filename.115.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.115.jpeg)

![unknown_filename.36.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.36.jpeg)

下图是我参照上图制作的图表。看完详细的绘制步骤后，你将深刻体会到这一技巧的奥妙所在。

![unknown_filename.116.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.116.jpeg)

首先选中源数据，A到F列

![unknown_filename.74.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.74.jpeg)

绘制散点图，得到经典的Excel风格图表

![unknown_filename.131.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.131.jpeg)

将利润率设为次坐标：选中橙色那根线，右键-设置数据系列格式-次坐标轴

![unknown_filename.103.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.103.jpeg)

删去图表标题、图例，调节横坐标、两个纵坐标的上下限，删去纵网格线，删去两个纵坐标的轴线，得到这样一张图

![unknown_filename.91.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.91.jpeg)

下一步称为“**锚定**”，鼠标光标移动到下图所示的图表左上角的顶点处，按住Alt，随后按住鼠标进行拖动，发现这样调节图表的尺寸，限定于Excel的网格点。

![unknown_filename.34.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.34.jpeg)

四个角都这样进行调节，分别“锚定”于N7, V7, N15, V15

![unknown_filename.127.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.127.jpeg)

选中图表区域，右键-设置图表区域格式，在属性中选择“大小固定，位置随单元格而变”，这样，在调整Excel行距和列宽时，图表就不会随之而动。

![unknown_filename.143.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.143.jpeg)

在第4~6行输入内容，设置填充色

![unknown_filename.155.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.155.jpeg)

**调节7~15行行距，使得Excel网格线与我们做的图表的横向网格线一一重叠；**

**调节O列和U列列宽**，使得**O列左侧网格线**恰好经过**图表横网格线的起点**，**U列右侧网格线**也是一样的道理，如下图所示。

![unknown_filename.46.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.46.jpeg)

选中图表区，填充色改为无色，外轮廓也删去，这样图表就变成“透明”的了

![unknown_filename.94.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.94.jpeg)

随后对N7:V15这个区域的单元格进行填充色。

（选中这些单元格的方法：

先选中图表区域外的一个单元格，如M7，按键盘的→键，移动到N7，然后按住Shift，再按→键或↓键调节即可，选中后进行单元格填充。）

![unknown_filename.118.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.118.jpeg)

在Excel“视图”中取消勾选网格线

![unknown_filename.19.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.19.jpeg)

最后添加一些图例即可

![unknown_filename.102.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.102.jpeg)

怎么样？相信你已体会到了如何将Excel的元素融入图表设计中。
\======================原回答=========================
我曾在大三寒假闭关三周，自学Excel, PowerPoint和Word，一年后又花了一个月的时间研习VBA。楼上关于函数和操作技巧已经分享很多了，我在这分享一些图表设计的技巧。

图表的重要性不言而喻，再好的数据，如果不能有效地呈现出来也是白费功夫。

我相信看完这个回答后，你再也不会将图做成这样。

![unknown_filename.13.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.13.jpeg)

好奇商业杂志上的这些高端大气的图是用什么特殊软件做出来的吗？

![unknown_filename.36.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.36.jpeg)

答案就是Excel。

滑珠图、子弹图、瀑布图……一切都可以用Excel最基本的操作搞定。

![unknown_filename.76.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.76.jpeg)

我会先介绍一些设计的核心理念和方法，然后列举16个“商务范”图表制作实例，包含详细的制作步骤，最后分享一些配色方案。

\==================================================================

目录

**一、商务图表制作核心理念和方法**

1. 突破Excel的图表元素
	
2. 突破Excel的图表类型
	
3. 布局与细节

**二、“商务范”图表制作实例**

1. 日期坐标轴妙用
	
2. 堆积柱形图妙用
	
3. 漏斗图-利用辅助列占位
	
4. 自定义Y轴刻度间距
	
5. 含加粗边缘的面积图
	
6. 图表覆盖妙用 - 横网格线覆盖于图表之上
7. 为Pie图加背景图片
	
8. 仪表盘
	
9. 多数量级的几组数据同时比较
	
10. 手风琴式折叠bar图
	
11. Water Fall 瀑布图
	
12. 不等宽柱形图
	
13. 滑珠图
	
14. 动态图表1
	
15. 动态图表2
	
16. Bullet图-竖直

**三、配色方案**

1. Nordri设计公司分享的配色方案
	
2. ExcelPro分享的方案

**四、自学参考书目和资料**

\==================================================================

正文

**一、商务图表制作核心理念和方法**

(这一章节的笔记整理自刘万祥老师的博客[ExcelPro的图表博客](http://excelpro.blog.sohu.com/))

**1\. 突破Excel的图表元素**

不要仅用“图表”做图表，而是用“图表＋所有Excel元素（如单元格，填充色，文本框）”去做图表。

（在我开头举的案例中有详尽的说明）

![unknown_filename.148.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.148.jpeg)

　　左上图，只有B4单元格是图表区域，标题利用的是B2；B3－B5填充浅色，"index"和"data"分别在B3、B5。

　　右上图，B2为图表序号，C2为图表标题，填深绿色，B3为副标题，图例放在C4，图表在C5，B2到C5填充淡色，B6、C6合并填写注释。

![unknown_filename.51.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.51.jpeg)

　　左上图，标题在C2－H2居中，图表在C3－H3，利用Excel单元格的数据表在C6－H8。

　　右上图，B2填红色装饰，标题和副标题分别在B2、B3，图表在D4－F4，数据来源在D5，标号2为矩形框，整个区域有边框。

**2\. 突破Excel的图表类型**

![unknown_filename.21.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.21.jpeg)

　　左上图，先用所有数据做曲线图或柱形图，然后选中相应的序列，更改图表类型，有时还需要用到次坐标轴。

　　右上图，先做好面积图，然后将该数据序列再次加入图表，修改新序列的图表类型为曲线图，调粗线型。

**3\. 布局与细节**

* **布局**

　　下图从上到下可以分为5个部分：**主标题区、副标题区、图例图、绘图区、脚注区**。

　　特点有：**完整的图表要素；突出的标题区；从上到下的阅读顺序**。

**标题区**非常突出，占到整个图表面积1/3以上，其中主标题用大号字和强烈对比效果，副标题提供详细信息。

![unknown_filename.126.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.126.jpeg)

* **竖向构图方式**
	

　　整个图表外围高宽比例在2:1到1:1之间，图例一般在绘图区上部或融入绘图区里面

* **使用更为简洁醒目的字体**
	

　　商业图表多选用**无衬线类字体**

　　图表和表格的数字中使用**Arial****字体、****8~10****磅大小，中文使用黑体**

* **注意图表的细节处理**
* 1\. 脚注区写上数据来源
	2\. 图标注释：对于图表中需要特别说明的地方，如指标解释、数据口径、异常数据等，使用上标或\*等进行标记，在脚注区说明
	3\. 坐标轴截断标识
	4\. 四舍五入：在脚注区写明：由于四舍五入，各数据之和可能不等于总额(或100%)
	5\. 简洁的坐标轴标签：如2003、’04、’05
	6\. 让Line图从y轴开始：双击x轴，Axis Options-最下-Position Axis-on tick marks
	7\. 作图数据的组织技巧: 原始数据不等于作图数据；作图前先数据排序；将数据分离为多个序列，每个序列单独格式化
	8\. 其他: 去除绘图区的外框线，去除纵坐标轴的线条色，将网格线使用淡灰色予以弱化，bar间距小于bar宽度，饼图分块用的白色线
	

—————————————————————————————————————

**二、“商务范”图表制作实例**

（这一章节的16个案例均出自刘万祥老师的[Excel图表之道 (豆瓣)](http://book.douban.com/subject/4326057/)，该书基于Excel2003）
最初回答中，这部分整理自我的笔记，基于英文版Excel2010。为了知友阅读方便，我以Excel 2013中文版操作了一遍，将操作步骤逐条改为了中文。
如果你使用的是其他版本，具体操作方法会不同（我的回答中以【】注出），但“【”前面的步骤说明和思路是没有问题的。
仪表盘、滑珠图、子弹图、瀑布图、动态图表我有自作的模板。有需要的请至 [Excel templ_免费高速下载](http://pan.baidu.com/s/1c0zXVXI)
**1\. 日期坐标轴妙用**

利率（y轴）随时间（x轴）的变化，我们希望得到下图所示的柱状图，横坐标的间隔按月份（3月、6月、12月、24月）分布。

![unknown_filename.140.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.140.jpeg)

原始数据与辅助列(A列为月份，B列为利率，C列是辅助列）

![unknown_filename.159.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.159.jpeg)

绘制方法

1) 选中A2:B5，做柱状图，发现应是横坐标的A列值也成了柱子

![unknown_filename.106.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.106.jpeg)

2) 删除系列1

方法1【选中图表 --> Excel标题栏图表工具 --> 设计 --> 选择数据 --> 系列1 --> 删除】

方法2【直接点击蓝色柱子 --> 按Delete键删除】

![unknown_filename.152.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.152.jpeg)

3) 将横坐标转化为我们希望的A列的值

【选中图表 --> Excel标题栏图表工具 --> 设计 --> 选择数据 --> 水平(分类)轴标签 编辑 --> 选择区域A2:A5】

![unknown_filename.105.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.105.jpeg)

4) 将横坐标转化为日期坐标轴 【双击横坐标 -->如下左图所示选择“日期坐标轴”】

得到下右图

![unknown_filename.107.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.107.jpeg)

5) 删去横坐标【选中横坐标 --> 按Delete键删除】

![unknown_filename.109.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.109.jpeg)

6) 将辅助列添加进去【选中辅助列C2:C5 --> 复制 --> 选中图表 --> 粘贴】

蓝色的“系列2”就是我们的辅助序列，因为值为0，所以看不到

![unknown_filename.60.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.60.jpeg)

7) 将蓝色“系列2”转化为折线图

【选中图表 --> Excel标题栏图表工具 --> 格式 --> 最左侧下拉菜单选择最后一项“系列2” --> Excel标题栏图表工具 --> 设计 --> 更改图表类型 --> 如下图所示将蓝色系列1的类型改为折线图】

![unknown_filename.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.jpeg)

得到

![unknown_filename.7.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.7.jpeg)

8) 让蓝色折线图的数据标签显示出来 【选中蓝色折线 --> 右击鼠标 --> 下图所示勾选数据标签“下方”】

![unknown_filename.47.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.47.jpeg)

9) 隐藏蓝色折线 【选中蓝色折线 --> 右击鼠标 --> 轮廓选择“无轮廓”】

![unknown_filename.82.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.82.jpeg)

得到

![unknown_filename.58.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.58.jpeg)

10) 逐个修改横坐标 【点击选中横坐标，发现四个都选中了(下左图所示) --> 再点击第一个0，将其选中(下右图所示) --> 鼠标点击公式输入栏，输入“=”，鼠标点击A2单元格 -->回车】依次修改即可
注意：在选中第一个0后，不要直接输入“=”，而是要在公式输入栏里输入

![unknown_filename.79.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.79.jpeg)

\*\*点评：该案例妙在利用辅助列，做出了柱状图的坐标值。当然，也有万能的办法，即不用辅助列，在完成5)之后，添加文本框作为坐标值。用本例所示的方法好处在于，源数据3、6、12、24修改之后，柱子、坐标值都会随之而动。

**2.** **堆积柱形图妙用**

效果如图，看似是簇状和堆积柱形图合用，实际呢？

![unknown_filename.120.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.120.jpeg)

一步即可，只需在源数据上下些功夫

【选中下图所示B9:E20单元格 --> 绘制堆积柱形图】

![unknown_filename.48.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.48.jpeg)

\*\*点评：利用错行和空行，奇妙无穷。

**3.** **漏斗图-****利用辅助列占位**

效果如图，形似漏斗。

![unknown_filename.117.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.117.jpeg)

原始数据 （指标需排序好，从大大小）

![unknown_filename.77.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.77.jpeg)

添加辅助列 【C3单元格公式=($D$3-D3)/2，然后拉至C8】

![unknown_filename.38.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.38.jpeg)

绘制方法

1) 选中B3:D8，绘制堆积条形图

![unknown_filename.62.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.62.jpeg)

2) 把漏斗倒过来，即反转纵坐标 【双击纵坐标 --> 勾选“逆序类别”】

![unknown_filename.54.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.54.jpeg)

3) 将绿色系列1隐去【选中绿色条 --> 右键 --> 填充 --> 无填充颜色】

![unknown_filename.88.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.88.jpeg)

\*\*点评：辅助列永远是好帮手。

**4.** **自定义Y****轴刻度间距**

以股价随时间变化为例，重要的是涨跌幅度，且幅度很大，这里我们采用**自定义Y轴**间距，并以常用的**对数坐标**为例。

最终效果图

![unknown_filename.145.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.145.jpeg)

原始数据

![unknown_filename.113.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.113.jpeg)

通过观测原始数据最小值和最大值，我们希望以20、30、50、100、400、600为刻度作为纵坐标，

将数据处理如下

* C列是B列值的对数值 C2单元格公式为 =Log(B2) ，拉至C12
	
* F列即我们希望的刻度
	
* G列同理，是F列的Log值
	

![unknown_filename.65.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.65.jpeg)

绘制方法

1)选中C2:C12 绘制折线图

![unknown_filename.37.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.37.jpeg)

2) 将G2:G7加入到图表中 【选中辅助列G2:G7 --> 复制 --> 选中图表 --> 粘贴】

![unknown_filename.151.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.151.jpeg)

3) 将新加入的蓝色折线改为散点图

【点击蓝色折线 --> Excel标题栏图表工具 --> 设计 --> 更改图表类型 --> 如下图所示将蓝色系列2的改为“带直线和数据标记的散点图”】

![unknown_filename.137.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.137.jpeg)

得到

![unknown_filename.153.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.153.jpeg)

4) 设置纵轴下限为1 【双击纵轴 --> 在坐标轴选项里将最小值调节为1】

5) 删去纵坐标轴，删去水平网格线；

6) 设置坐标轴在刻度线上【双击横坐标轴 --> 如下左图所示勾选“在刻度线上”】

得到右下图

![unknown_filename.123.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.123.jpeg)

7) 将蓝色折线的横坐标设置为E2:E7【点击蓝色折线 --> Excel标题栏图表工具 --> 设计 --> 选择数据 --> 如左下图所示选择“系列2” --> 点击“编辑” --> 如右下图所示，X轴系列值选为E2:E7 --> 确定】

![unknown_filename.122.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.122.jpeg)

得到

![unknown_filename.6.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.6.jpeg)

8) 让蓝色数据点的数据值显示出来 【点击蓝色直线 --> 右侧选择数据标签-左】

![unknown_filename.41.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.41.jpeg)

缩小一下绘图区

![unknown_filename.27.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.27.jpeg)

9) 添加误差线 【点击蓝色直线 --> 右侧选择误差线-更多选项】

![unknown_filename.108.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.108.jpeg)

此时，横纵误差线都出来了

10) 删除纵误差线 【点击下左图所示的位置选中纵误差线 --> 按Delete键删除】

得到又下图

![unknown_filename.23.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.23.jpeg)

11) 调节横误差线参数 【双击横误差线 --> 在右侧弹窗里勾选“正偏差”，“固定值”改为10】

缩小一下绘图区，得到右下图

![unknown_filename.96.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.96.jpeg)

12) 隐藏蓝色线 【右键蓝色直线 --> 选择无填充，无轮廓】

13) 调节误差线的颜色、线形 【双击误差线 --> 右侧弹窗中修改(下左图所示)】

得到右下图

![unknown_filename.59.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.59.jpeg)

13) 与本回答的案例1类似，逐个修改纵坐标数据值【以2.78这个数据为例：选中纵坐标(6个数据一下子都选中了) --> 再点击2.78这个数据(如下图所示，只有2.78选中了) --> 鼠标点击公式输入栏，输入“=”，然后鼠标点击600(F7单元格) --> 回车】

![unknown_filename.28.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.28.jpeg)

依次逐个修改，大功告成。

\*\*点评：本例极其巧妙地借助误差线，实现横向网格线。误差线在后续案例中会多次提及。当然，有人会说完全可以不用误差线，插入几个直线拖动就好了。但是，本例方法的好处是，修改20、50、400等坐标值，网格线也会跟着移动。

**5\. 含加粗边缘****面积图**

最终效果与源数据

![unknown_filename.5.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.5.jpeg)

绘制方法

1) 选中数据做折线图

![unknown_filename.9.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.9.jpeg)

2) 将源数据再次添加进图表中【选中源数据 --> 复制 --> 选中图表 --> 粘贴】

发现系列2覆盖住了系列1

![unknown_filename.43.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.43.jpeg)

3) 将系列2改为面积图【点击选中蓝色折线 --> Excel标题栏图表工具 --> 设计 --> 更改图表类型 --> 如下左图所示将改为面积图】

得到下右图

![unknown_filename.75.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.75.jpeg)

4) 调节坐标轴位置 【双击横坐标轴 --> 右侧弹窗中勾选“在刻度线上”】

得到右下图

![unknown_filename.142.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.142.jpeg)

调节颜色就好了

下面这个图是我做的~

![unknown_filename.86.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.86.jpeg)

\*\*点评：两种或多种图表类型合用的方法一定要掌握，活学活用。

**6\. 图表覆盖妙用 -** **横网格线覆盖于图表****之上**

最终效果

![unknown_filename.52.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.52.jpeg)

绘制方法

以柱状图为例 （其他类型的图都一样）

源数据

![unknown_filename.156.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.156.jpeg)

1) 绘制柱形图

![unknown_filename.125.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.125.jpeg)

2) 将其锚定 【鼠标光标移动到下图所示的图表左上角的顶点处，按住Alt，随后按住鼠标进行拖动，发现这样调节图表的尺寸，限定于Excel的网格点。】

![unknown_filename.17.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.17.jpeg)

如下图所示，将四个角分别锚定于D2，G2，D9， G9

![unknown_filename.4.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.4.jpeg)

3) 复制图表【选中图表 --> 复制 --> 鼠标点击任意一个单元格 --> 粘贴】

得到左右两个一模一样的图表

![unknown_filename.3.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.3.jpeg)

4) 对右边的图表

* 图表区背景色设为无色【右键图表区 --> 填充和轮廓都设为无】
	
* 柱子设为无色【右键柱子 --> 填充和轮廓都设为无】
	

对左边的图表

* 删去左网格线【选中网格线 --> Delete键删除】
	
* 横轴直线隐去【选中横轴 --> 右键 --> 无轮廓】
	
* 横坐标和纵坐标都的字体都设为白色 【分别选中横纵左边 --> 菜单栏中将字体颜色设为白色】
	

![unknown_filename.25.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.25.jpeg)

5) 按住Alt移动第二张图覆盖于第一张图之上。一定要按住Alt进行拖动！！！！！！

![unknown_filename.73.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.73.jpeg)

6) 自行设计网格线颜色即可

![unknown_filename.14.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.14.jpeg)

\*\*点评：此案例巧妙地利用了图表覆盖。
**7\. 为Pie****图加背景图片**

最终效果

![unknown_filename.50.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.50.jpeg)

原始数据

![unknown_filename.85.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.85.jpeg)

绘制方法

1) 先用A1:A5做饼图，为系列1

![unknown_filename.119.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.119.jpeg)

2) 选中源数据中任意一个值 (如A3) 添加到图表中 【选中A3 --> 复制 --> 选中图表 --> 粘贴】
为系列2

此时无法看到也无法选择系列2，看到的仍然是上图的样子

3) 将系列1改为次坐标轴【选中图表 --> Excel标题栏图表工具 --> 设计 --> 更改图表类型 --> 将系列1改为次坐标轴(下图所示)】

![unknown_filename.83.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.83.jpeg)

看到的仍然是上图的样子

4) 将系列设为无填充【右击大饼 --> 设置填充色为无填充】

![unknown_filename.80.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.80.jpeg)

此时看到的正是系列2，如下图

![unknown_filename.10.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.10.jpeg)

5) 为系列2加背景图片 【双击图表，右侧出现弹窗 -->Excel标题栏图表工具 --> 格式 --> 左侧下拉菜单选择“系列2” --> 右侧弹窗中选择插入图片 】

![unknown_filename.141.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.141.jpeg)

![unknown_filename.35.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.35.jpeg)

![unknown_filename.50.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.50.jpeg)

\*\*点评：如果不用本案例的方法，直接给饼图加背景图，得到的是...

![unknown_filename.97.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.97.jpeg)

**8\. 仪表盘**

最终效果

在某个单元格中输入数值（0-100），红色的指针会随之而动

![unknown_filename.157.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.157.jpeg)

该案例不是很切题，应用也很局限，所以删去了操作步骤。该例成品可至前面提到的网盘地址中下载。若有兴趣研究详细做法，请私信。

**9\. 多数量级的几组数据同时比较**

最终效果

![unknown_filename.69.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.69.jpeg)

原始数据

![unknown_filename.154.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.154.jpeg)

处理数据

![unknown_filename.89.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.89.jpeg)

F3单元格 =B3/MAX($B$3:$B$8)\*0.8，拉至F8

G3单元格 =1-F3，拉至G8

H3单元格 =C3/MAX($C$3:$C$8)\*0.8，拉至H8

I3单元格 =1-H3，拉至I8

J3单元格 =D3/MAX($D$3:$D$8)\*0.8，拉至J8

绘制方法

1) F3:J8作堆积条形图，删去网格线、横坐标轴

![unknown_filename.63.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.63.jpeg)

2) 纵坐标逆序【双击纵坐标 --> 左侧弹窗中勾选“逆序类别”】

![unknown_filename.12.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.12.jpeg)

3) 把占位条设为白色 【在需要调成白色的条上右键 --> 填充色设为无色】

![unknown_filename.16.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.16.jpeg)

添加三个文本框，得到

![unknown_filename.69.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.69.jpeg)

\*\*点评：0.8是可调节的，根据需要而定，可以是0.7，也可以是0.9

这个案例在2014年终汇报中用到了！特别适合不同数量级的数据对比。

**10\. 手风琴式折叠bar图**

最终效果（突出前三个和后三个数据，中间的数据弱化显示）

![unknown_filename.78.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.78.jpeg)

原始数据 （假设前后各有三个数据需要强调）

![unknown_filename.2.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.2.jpeg)

作图数据注意：

* 第一列 ：若前后各有n个数据需要强调，那么中间就空n个；
	
* 第二列：中间的数据若有m个，则前后各留m-1个；
	
* 两列首行要对齐
	

如下图所示

![unknown_filename.87.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.87.jpeg)

绘制方法

1) 以第一列做堆积条形图（上图第一列黑色框内的数据，E2:E10）

![unknown_filename.20.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.20.jpeg)

2) 将第二列数据添加到图表中【选中上上图中第二列黑色框内的数据(F2:F17) --> 复制 --> 选中图表 --> 粘贴】

![unknown_filename.32.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.32.jpeg)

3) 将蓝色条形图改为次坐标轴 【单击选中蓝色条 --> Excel标题栏图表工具 --> 设计 --> 更改图表类型 --> 将系列2的“次坐标轴”勾选】

![unknown_filename.44.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.44.jpeg)

得到

![unknown_filename.70.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.70.jpeg)

4) 将上下两个横坐标轴的上限值改为一致，这里改为100【双击横坐标轴 --> 在右侧弹窗中调节最大值为100】

![unknown_filename.135.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.135.jpeg)

5) 让次纵坐标轴显示出来【点击图表区 --> 下图所示勾选次要纵轴】

![unknown_filename.150.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.150.jpeg)

此时四根轴都出来了(上左图所示)

6) 将左右两根纵轴反转【双击纵轴 --> 右侧弹窗中勾选“逆序系列” --> 另一根纵轴一样处理】

得到右下图

![unknown_filename.136.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.136.jpeg)

7) 删去下面和右边的两根轴，然后可设置填充色等

![unknown_filename.139.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.139.jpeg)

\*\*点评：你可以尝试一下其他情况，如前后各突出5个，或前突出2两个，后突出4个。其实利用的都是空格占位。

**11\. Water Fall** **瀑布图**

最终效果

![unknown_filename.45.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.45.jpeg)

原始数据

![unknown_filename.138.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.138.jpeg)

作图数据

![unknown_filename.90.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.90.jpeg)

D3 =B3

D4 =SUM($B$3:B4) ，拉至D9

E3 =B3

E10 =B10

F4 =IF(B4<0,D4,D3) ，拉至F9

G4 =IF(B4>=0,B4,0) ， 拉至G9

H4 =IF(B4>=0,0,ABS(B4)) ， 拉至H9

作图方法

1) 选中蓝色框内的值 (E3: H10)，做堆积柱形图

![unknown_filename.33.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.33.jpeg)

2) 蓝色柱形图设置为无色【右击蓝色柱 --> 无填充色】

![unknown_filename.95.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.95.jpeg)

再稍作调节

![unknown_filename.45.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.45.jpeg)

**12.** **不等宽柱形图**

最终效果1 - 方法1制得

![unknown_filename.144.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.144.jpeg)

（高度反映ARPU值，宽度反映用户规模，四个柱子依次是四种产品）

原始数据

![unknown_filename.56.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.56.jpeg)

最终效果2 - 方法2制得

![unknown_filename.128.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.128.jpeg)

绘制方法1 - 分组细分法 - 柱形图

将数据处理如下 \[每个ARPU数据重复次数为“用户规模”（柱子宽度）数\]

![unknown_filename.147.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.147.jpeg)

1) 选中B7:E26，做柱形图，删去无关元素

![unknown_filename.149.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.149.jpeg)

2) 选中任意一根柱子，在右侧“设置数据系列格式”中将“系列重叠”改为100%，将“分类间距”改为0%

![unknown_filename.84.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.84.jpeg)

就得到了我们想要的图表

![unknown_filename.124.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.124.jpeg)

绘制方法2- 时间刻度法 - 面积图

原始数据依旧

![unknown_filename.114.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.114.jpeg)

作图数据要花一些功夫

首先看A列，A1的内容是0，A2到A4是“产品1”的“用户规模”，为8，A5到A7是“产品1”和“产品2”的“用户规模”之和8+4=12，同理A8到A10是14，而最后一个单元格A11是8+4+2+6=20

注意，如果是5个产品，8个产品呢？A1永远是0，A1下面每一组依旧是3个，而最后一个单元格仍是所有用户规模之和

B列到E列就不用多说了，两两分别是ARPU值

![unknown_filename.57.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.57.jpeg)

1) 选中A1:E11，做面积图，删去无用的信息，但注意要留着横坐标

![unknown_filename.134.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.134.jpeg)

2) 将横轴改为A1:A11 【选中图表 --> Excel标题栏 图表工具 --> 设计 -- > 选择数据 --> 单击下图所示的水平轴标签 编辑按钮 --> 在弹窗中选择为A1:A11 --> 确定】

![unknown_filename.42.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.42.jpeg)

3) 删去多余图形，如下图所示，在红圈位置处单击，按Delete键删除

![unknown_filename.53.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.53.jpeg)

得到

![unknown_filename.112.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.112.jpeg)

4) 将横轴改为时间刻度 【选中横坐标 - 右侧设置坐标轴格式中选为日期坐标轴】

![unknown_filename.104.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.104.jpeg)

然后删去横坐标，得到

![unknown_filename.132.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.132.jpeg)

5) 依次更改这4个柱子的轮廓为白色，并调节轮廓线宽

![unknown_filename.98.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.98.jpeg)

得到最终的图表

![unknown_filename.128.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.128.jpeg)

\*点评：方法1简单易行，但方法2做出来的图更美观。两者都是巧妙地构造作图数据，值得一品。

**13.** **滑珠图**

最终效果 （右图是我仿照原图画的）

蓝色奥巴马支持率，红色麦凯恩支持率。纵坐标为不同人群

两种滑珠为散点图，横梁为条形图

![unknown_filename.133.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.133.jpeg)

绘制方法

数据（左下） E列为散点图Y轴数据

1)选中A2:A10和D2:D10，作簇状条形图，并将纵轴逆序排列，将横坐标最大值定为100，得到右下图

![unknown_filename.26.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.26.jpeg)

2) 选中B2:B10，复制，粘贴入图表，然后将这个新系列改为改为散点图（左下）

将红色散点图的横坐标改为B2:B10，纵坐标改E2:E10，得到右下图

![unknown_filename.110.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.110.jpeg)

3) 用同样的方法处理C2:C10
4) 调节柱形图、散点图的颜色、填充等，完工。
\*点评：乍一看摸不着头脑的图，其实就是条形图和散点图的巧妙叠加。我的工作中就用到了这一案例，纵坐标是10个人，而散点是每个人的两项指标（0~100），真是形象而明了。本例用到的步骤在之前均多次使用，所以没有详细展开。

**14\. 动态图表1**

B3单元格 =INDEX(B8:B13,$B$5) 横向拉到N3

（这样当在右下角的List Box里选择时，B5单元格灰显示选择结果，B3:N3就会跟着显示选择结果对应各月的数值）

以B3:N3作图即可

![unknown_filename.100.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.100.jpeg)

辅助阅读：List box是怎么出来的？
【也可不用List box，直接在B5里输入数值（1~5）就好】
List box的调出方法：

**File-Options-Customize Ribbon**\-右边框内勾选**Developer** 这样面板就有Developer栏，单击**Developer-Controls-Insert**\-第一排第五个 **List Box** 添加到工作表中

右击该List Box， **Format Control-Input range** $B$8:$B$13

**Cell link** $B$5

B5就会显示在List Box里选择了第几个数值

**15.** **动态图表2**

以下图为例。B5设置数据有效性只可选择07年、08年或09年

B7单元格 =CHOOSE(IF(B5="08年",2,IF(B5="07年",1,3)),1,2,3)

B8单元格 =INDEX(B1:B3,$B$7) 拉到F8

![unknown_filename.121.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.121.jpeg)

先以B1:F3作Line图，选择B8:F8 Ctrl+C Ctrl+V到图表中即可

![unknown_filename.92.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.92.jpeg)

![unknown_filename.66.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.66.jpeg)

**16\. Bullet****图-****竖直**

最终效果 与原始数据

![unknown_filename.30.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.30.jpeg)

绘制方法

1) 以A2:F6做堆积柱形图（左下），转换横纵坐标（右下）

![unknown_filename.40.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.40.jpeg)

2) 更改最下蓝色柱子（实际）为次坐标轴并适当将其变窄，得到左下图

3) 更改最下红色柱子（目标）为次坐标轴，并更改为折线图，得到右下图

![unknown_filename.24.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.24.jpeg)

去掉红色连线并将方块改为红短线

然后设置其他颜色等，大功告成

![unknown_filename.49.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.49.jpeg)

\*点评： 子弹图看起来蛮高端的，但若不辅以说明，别人还是很难看懂的，所以子弹图要慎用。同样，每步操作方法在前面都多次详细说明，在这就写的简洁一点。

—————————————————————————————————————

**三、配色方案**

配色主题设置方法 （以Excel2013做示范，其他版本大同小异）
Step1. <页面布局 - 颜色- 自定义颜色>

![unknown_filename.71.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.71.jpeg)

Step2. 总共12个颜色可自定义，单击任意一个颜色下拉菜单，选择“其他颜色”，输入RGB值，全部完后命名，保存即可。这样，在<页面布局 - 颜色>下拉菜单中就可以选择自定义的主题。

![unknown_filename.67.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.67.jpeg)

以下每个配色方案都提供了这12种颜色的RGB值

**1\. Nordri设计公司分享的配色方案**

[Nordri 商业演示设计](http://www.nordridesign.com/)
每种配色方案的12个着色的RGB值下载请移步 [Nordri合集_免费高速下载](http://pan.baidu.com/s/1bnGpaiz)

1-碧海蓝天

![unknown_filename.22.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.22.jpeg)

2-达芬奇的左手

![unknown_filename.111.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.111.jpeg)

3-老男孩也有春天

![unknown_filename.39.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.39.jpeg)

4-路人甲的秘密

![unknown_filename.72.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.72.jpeg)

5-旅人的脚步

![unknown_filename.15.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.15.jpeg)

6-那拉提草原的天空

![unknown_filename.8.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.8.jpeg)

7-香柠青草

![unknown_filename.81.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.81.jpeg)

8-热季风

![unknown_filename.130.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.130.jpeg)

9-软件人生

![unknown_filename.1.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.1.jpeg)

10-商务素雅

![unknown_filename.68.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.68.jpeg)

11-商务现代

![unknown_filename.11.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.11.jpeg)

12-数据时代

![unknown_filename.146.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.146.jpeg)

13-素食主义

![unknown_filename.29.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.29.jpeg)

14-岁月经典红

![unknown_filename.93.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.93.jpeg)

15-夏日嬷嬷茶

![unknown_filename.101.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.101.jpeg)

16-邮递员的假期

![unknown_filename.31.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.31.jpeg)

17-毡房里的夏天夏天

![unknown_filename.55.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.55.jpeg)

**2\. ExcelPro分享的方案**

![unknown_filename.129.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.129.jpeg)

![unknown_filename.61.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.61.jpeg)

![unknown_filename.18.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.18.jpeg)

![unknown_filename.64.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.64.jpeg)

![unknown_filename.158.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.158.jpeg)

![unknown_filename.99.jpeg](./_resources/Excel有哪些可能需要熟练掌握而很多人不会的技能？.resources/unknown_filename.99.jpeg)

**四、自学参考书目和资料**

[ExcelPro的图表博客](http://excelpro.blog.sohu.com/)

[Excel图表之道 (豆瓣)](http://book.douban.com/subject/4326057/)

[Nordri 商业演示设计](http://www.nordridesign.com/)

[用地图说话 (豆瓣)](http://book.douban.com/subject/10435804/)

[演说之禅 (豆瓣)](http://book.douban.com/subject/3313363/)

[说服力 让你的PPT会说话 (豆瓣)](http://book.douban.com/subject/4604592/)

[别怕，Excel VBA其实很简单 (豆瓣)](http://book.douban.com/subject/19952184/)

更多详情: <http://www.zhihu.com/question/21758700/answer/34705774>
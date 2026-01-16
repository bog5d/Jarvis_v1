---
created: 2018-01-20 22:29:39
jarvis_ai_meta:
  key_people: []
  mood: 平静
  summary: 王霞客整理并记录了Python Seaborn绘图库的核心概念、分类及常用函数用法。
  tagged_at: '2026-01-11 02:39:52'
  time_space:
    date: '2018-01-20'
    location: ''
tags:
- 数据分析
- Seaborn
- 数据可视化
- Python
- 绘图函数
updated: 2018-01-29 13:09:21
---

# python seaborn画图

python seaborn画图

以前觉得用markdown写图文混排的文字应该很麻烦，后来发现CSDN的markdown真是好用的。

在做分析时候，有时需要画几个图看看数据分布情况，但总记不住python的绘图函数。今天有空顺便整理下python的seaborn绘图函数库。 
Seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，在大多数情况下使用seaborn就能做出很具有吸引力的图，而使用matplotlib能制作具有更多特色的图。应该把Seaborn视为matplotlib的补充，而不是替代物。

seaborns是针对统计绘图的，方便啊。

一般来说，seaborn能满足数据分析90%的绘图需求，够用了，如果需要复杂的自定义图形，还是要matplotlit。这里也只是对seaborn官网的绘图API简单翻译整理下，对很多参数使用方法都没有说到，如果需要精细绘图，还是需要参照其seaborn的文档的。

这里简要介绍常用的图形，常用的参数，其精美程度不足以当做报告绘图，算是做笔记吧。

# 1.几个概念

如果使用过R语言的ggplot2绘图包，对分组分面，统计绘图等概念应该很熟悉，这里也介绍下。

## 1.1.分组绘图

比如说需要在一张图上绘制两条曲线，分别是南方和北方的气温变化，分别用不同的颜色加以区分。在seaborn中用**hue**参数控制分组绘图。

## 1.2.分面绘图

其实就是在一张纸上划分不同的区域，比如2\*2的子区域，在不同的子区域上绘制不同的图形，在matplotlib中就是 add\_subplot(2,2,1)，在seaborn中用col参数控制，col的全称是columns，不是color，如果辅助col\_wrap参数会更好些。后来发现，col可以控制columns的子图，那么row可以控制rows的子图排列。 
如果需要分面绘图，应该使用seaborn的**FacetGrid**对象，seaborn的一般的绘图函数是没有分面这个参数的。

## 1.3.统计函数

分组绘图的时候，会对分组变量先要用统计函数，然后绘图，比如先计算变量的均值，然后绘制该均值的直方图。统计绘图参数是 **estimator**，很多情况下默认是**numpy.mean**。在ggplot2中就大量使用了这种方法。如果不适用统计绘图，就需要先用pandas进行groupby分组汇总，然后用seaborn绘图，多此一举了。

# 2.图形分类

在seaborn中图形大概分这么几类，因子变量绘图，数值变量绘图，两变量关系绘图，时间序列图，热力图，分面绘图等。

**因子变量绘图**

1. 箱线图boxplot

* 小提琴图violinplot
* 散点图striplot
* 带分布的散点图swarmplot
* 直方图barplot
* 计数的直方图countplot
* 两变量关系图factorplot

**回归图** 
回归图只要探讨两连续数值变量的变化趋势情况，绘制x-y的散点图和回归曲线。

1. 线性回归图lmplot
2. 线性回归图regplot

**分布图** 
包括单变量核密度曲线，直方图，双变量多变量的联合直方图，和密度图

**热力图** 
1\. 热力图heatmap

**聚类图** 
1\. 聚类图clustermap

**时间序列图** 
1\. 时间序列图tsplot 
2\. 我的时序图plot\_ts\_d , plot\_ts\_m

**分面绘图** 
1.分面绘图FacetGrid

# 3.因子变量绘图

## 3.1.boxplot箱线图

    import seaborn as sns
    sns.set_style("whitegrid")
    tips = sns.load_dataset("tips")
    # 绘制箱线图
    ax = sns.boxplot(x=tips["total_bill"])
    # 竖着放的箱线图，也就是将x换成y
    ax = sns.boxplot(y=tips["total_bill"])

* 1234567

![SouthEast](http://img.blog.csdn.net/20170403204612499?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组绘制箱线图，分组因子是day，在x轴不同位置绘制
    ax = sns.boxplot(x="day", y="total_bill", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170403205436724?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组箱线图，分子因子是smoker，不同的因子用不同颜色区分
    # 相当于分组之后又分组
    ax = sns.boxplot(x="day", y="total_bill", hue="smoker",
                        data=tips, palette="Set3")

* 1234

![SouthEast](http://img.blog.csdn.net/20170403205527115?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 改变线宽，linewidth参数
    ax = sns.boxplot(x="day", y="total_bill", hue="time",
                        data=tips, linewidth=2.5)
    
    # 改变x轴顺序，order参数
    ax = sns.boxplot(x="time", y="tip", data=tips,
                        order=["Dinner", "Lunch"])

* 1234567

    # 对dataframe的每个变量都绘制一个箱线图，水平放置
    iris = sns.load_dataset("iris")
    ax = sns.boxplot(data=iris, orient="h", palette="Set2")

* 123

![SouthEast](http://img.blog.csdn.net/20170403205641560?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

**箱线图+有分布趋势的散点图–>的组合图**

    # 箱线图+有分布趋势的散点图
    # 图形组合也就是两条绘图语句一起运行就可以了，相当于图形覆盖了
    ax = sns.boxplot(x="day", y="total_bill", data=tips)
    ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

* 1234

![SouthEast](http://img.blog.csdn.net/20170403205820929?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3.2.violinplot小提琴图

**小提琴图**其实是**箱线图**与**核密度图**的结合，箱线图展示了分位数的位置，小提琴图则展示了任意位置的密度，通过小提琴图可以知道哪些位置的密度较高。在图中，白点是中位数，黑色盒型的范围是下四分位点到上四分位点，细黑线表示须。外部形状即为核密度估计（在概率论中用来估计未知的密度函数，属于非参数检验方法之一）。

    import seaborn as sns
    sns.set_style("whitegrid")
    tips = sns.load_dataset("tips")
    # 绘制小提琴图
    ax = sns.violinplot(x=tips["total_bill"])

* 12345

![SouthEast](http://img.blog.csdn.net/20170403212245377?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的小提琴图，同上面的箱线图一样通过X轴分组
    ax = sns.violinplot(x="day", y="total_bill", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170403212402613?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 通过hue分组的小提琴图，相当于分组之后又分组
    ax = sns.violinplot(x="day", y="total_bill", hue="smoker",
                            data=tips, palette="muted")

* 123

![SouthEast](http://img.blog.csdn.net/20170403212608943?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组组合的小提琴图，其实就是hue分组后，各取一半组成一个小提琴图
    ax = sns.violinplot(x="day", y="total_bill", hue="smoker",
                            data=tips, palette="muted", split=True)

* 123

![SouthEast](http://img.blog.csdn.net/20170403212821758?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 调整x轴顺序，同样通过order参数
    ax = sns.violinplot(x="time", y="tip", data=tips,
                        order=["Dinner", "Lunch"])

* 123

![SouthEast](http://img.blog.csdn.net/20170403213005636?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

其他的样式不常用，就不贴上来了。

## 3.3.stripplot散点图

需要注意的是，seaborn中有两个散点图，一个是普通的散点图，另一个是可以看出分布密度的散点图。下面把它们花在一起就明白了。

    # 普通的散点图
    ax1 = sns.stripplot(x=tips["total_bill"])
    # 带分布密度的散点图
    ax2 = sns.swarmplot(x=tips["total_bill"])

* 1234

![SouthEast](http://img.blog.csdn.net/20170403213713038?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的散点图
    ax = sns.stripplot(x="day", y="total_bill", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170403213844212?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 添加抖动项的散点图，jitter可以是0.1,0.2...这样的小数，表示抖动的程度大小
    ax = sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

* 12

![SouthEast](http://img.blog.csdn.net/20170403214036339?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 是不是想横着放呢，很简单的，x-y顺序换一下就好了
    ax = sns.stripplot(x="total_bill", y="day", data=tips,jitter=True)

* 12

![SouthEast](http://img.blog.csdn.net/20170403214202028?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 重点来了，分组绘制，而且是分组后分开绘制，在柱状图中，跟分组柱状图类似的。
    # 通过 hue, split 参数控制
    # 1.分组
    ax = sns.stripplot(x="sex", y="total_bill", hue="day",
                        data=tips, jitter=True)
    # 2.分开绘制
    ax = sns.stripplot(x="day", y="total_bill", hue="smoker",
                    data=tips, jitter=True,palette="Set2", split=True)

* 12345678

![SouthEast](http://img.blog.csdn.net/20170403214525967?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170403214556185?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 散点图+小提起图
    # 两条命令一起运行就行了
    ax = sns.violinplot(x="day", y="total_bill", data=tips,inner=None, color=".8")
    ax = sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)

* 1234

![SouthEast](http://img.blog.csdn.net/20170403214726145?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3.4.swarmplot带分布的散点图

swarmplt的参数和用法和stripplot的用法是一样的，只是表现形式不一样而已。

    import seaborn as sns
    sns.set_style("whitegrid")
    tips = sns.load_dataset("tips")
    ax = sns.swarmplot(x=tips["total_bill"])

* 1234

![SouthEast](http://img.blog.csdn.net/20170403215108260?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的散点图
    ax = sns.swarmplot(x="day", y="total_bill", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170403215206871?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 箱线图+散点图
    # whis 参数设定是否显示箱线图的离群点，whis=np.inf 表示不显示
    ax = sns.boxplot(x="tip", y="day", data=tips, whis=np.inf)
    ax = sns.swarmplot(x="tip", y="day", data=tips)

* 1234

![SouthEast](http://img.blog.csdn.net/20170403215507281?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 小提琴图+散点图
    ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
    ax = sns.swarmplot(x="day", y="total_bill", data=tips,
                        color="white", edgecolor="gray")

* 1234

![SouthEast](http://img.blog.csdn.net/20170403215617237?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3.5.pointplot

Show point estimates and confidence intervals using scatter plot glyphs. 
使用散点图符号显示点估计和置信区间。

这个我不知道在什么地方用到，不太明白。就先写这个了。

## 3.6.barplot直方图

我不喜欢显示直方图上面的置信度线，难看，所以下面的图形我都设置ci=0.(Size of confidence intervals to draw around estimated values)

直方图的统计函数，绘制的是变量的均值 estimator=np.mean

    # 注意看看Y轴，看到没，统计函数默认是 mean，
    import seaborn as sns
    sns.set_style("whitegrid")
    tips = sns.load_dataset("tips")
    ax = sns.barplot(x="day", y="total_bill", data=tips,ci=0)

* 12345

![SouthEast](http://img.blog.csdn.net/20170403220112305?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的柱状图
    ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips,ci=0)

* 12

![SouthEast](http://img.blog.csdn.net/20170403220400069?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 绘制变量中位数的直方图，estimator指定统计函数
    from numpy import median
    ax = sns.barplot(x="day", y="tip", data=tips, 
                        estimator=median, ci=0)

* 1234

![SouthEast](http://img.blog.csdn.net/20170403220813876?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 改变主题颜色
    # palette="Blues_d"
    ax = sns.barplot("size", y="total_bill", data=tips, 
                        palette="Blues_d")

* 1234

![SouthEast](http://img.blog.csdn.net/20170403221020619?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3.7.countplot计数统计图

这个很重要，对因子变量计数，然后绘制条形图

    import seaborn as sns
    sns.set(style="darkgrid")
    titanic = sns.load_dataset("titanic")
    ax = sns.countplot(x="class", data=titanic)

* 1234

![SouthEast](http://img.blog.csdn.net/20170403221313087?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组绘图
    ax = sns.countplot(x="class", hue="who", data=titanic)
    
    # 如果是横着放，x用y替代
    ax = sns.countplot(y="class", hue="who", data=titanic)

* 12345

![SouthEast](http://img.blog.csdn.net/20170403221356543?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 3.8.factorplot

这是一类重要的变量联合绘图。 
绘制 因子变量-数值变量 的分布情况图。

    # 用小提琴图 反应 time-pulse 两变量的分布情形
    import seaborn as sns
    sns.set(style="ticks")
    exercise = sns.load_dataset("exercise")
    g = sns.factorplot(x="time", y="pulse", hue="kind",
                        data=exercise, kind="violin")

* 123456

![SouthEast](http://img.blog.csdn.net/20170403222040859?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 不同的deck（因子）绘制不同的alive（数值），col为分子图绘制，col_wrap每行画4个子图
    titanic = sns.load_dataset("titanic")
    g = sns.factorplot(x="alive", col="deck", col_wrap=4,
                        data=titanic[titanic.deck.notnull()],
                        kind="count", size=2.5, aspect=.8)

* 12345

![SouthEast](http://img.blog.csdn.net/20170403222401446?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

# 4.回归图

回归图有两个，我暂时没有看出他们有什么区别，从函数说明来看看吧。 
**lmplot**： Plot data and regression model fits across a FacetGrid. 
**regplot**：Plot data and a linear regression model fit.

## 4.1.回归图lmplot

    # 线性回归图
    import seaborn as sns; sns.set(color_codes=True)
    tips = sns.load_dataset("tips")
    g = sns.lmplot(x="total_bill", y="tip", data=tips)

* 1234

![SouthEast](http://img.blog.csdn.net/20170404092040681?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的线性回归图，通过hue参数控制
    g = sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170404092151635?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组绘图，不同的组用不同的形状标记
    g = sns.lmplot(x="total_bill", y="tip", hue="smoker", 
                    data=tips,markers=["o", "x"])

* 123

![SouthEast](http://img.blog.csdn.net/20170404092318746?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 不仅分组，还分开不同的子图绘制，用col参数控制
    g = sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips)

* 12

![SouthEast](http://img.blog.csdn.net/20170404093829907?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # col+hue 双分组参数，既分组，又分子图绘制，jitter控制散点抖动程度
    g = sns.lmplot(x="size", y="total_bill", hue="day", 
                    col="day",data=tips, aspect=.4, x_jitter=.1)

* 123

![SouthEast](http://img.blog.csdn.net/20170404094231489?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组绘制，控制size尺寸
    g = sns.lmplot(x="total_bill", y="tip", col="day", hue="day",
                    data=tips, col_wrap=2, size=3)

* 123

![SouthEast](http://img.blog.csdn.net/20170404094349053?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 既然col可以控制分组子图的，那么row也是可以控制分组子图的
    g = sns.lmplot(x="total_bill", y="tip", row="sex", 
                    col="time", data=tips, size=3)

* 123

![SouthEast](http://img.blog.csdn.net/20170404094714889?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 4.2.回归图regplot

Plot the relationship between two variables in a DataFrame:

    import seaborn as sns; sns.set(color_codes=True)
    tips = sns.load_dataset("tips")
    ax = sns.regplot(x="total_bill", y="tip", data=tips)

* 123

![SouthEast](http://img.blog.csdn.net/20170404094957196?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 控制散点的形状和颜色
    import numpy as np; np.random.seed(8)
    mean, cov = [4, 6], [(1.5, .7), (.7, 1)]
    x, y = np.random.multivariate_normal(mean, cov, 80).T
    ax = sns.regplot(x=x, y=y, color="g", marker="+")

* 12345

![SouthEast](http://img.blog.csdn.net/20170404095359587?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 控制回归的置信度，你会看到拟合直线的外面的面积的有变化的
    ax = sns.regplot(x=x, y=y, ci=68)

* 12

![SouthEast](http://img.blog.csdn.net/20170404095646747?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 上面的都是拟合一次曲线，拟合二次曲线通过order=2设置，
    # 拟合一次曲线相当于 order=1
    ans = sns.load_dataset("anscombe")
    ax = sns.regplot(x="x", y="y", data=ans.loc[ans.dataset == "II"],
                    scatter_kws={"s": 80},order=2, ci=None, truncate=True)

* 12345

![SouthEast](http://img.blog.csdn.net/20170404100017983?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

# 5.数值分布绘图

## 5.1.直方图histplot

直方图hist=True，核密度曲线rug=True

    # 绘制数值变量的密度分布图
    # 默认既绘制核密度曲线，也绘制直方图
    import seaborn as sns, numpy as np
    sns.set(rc={"figure.figsize": (8, 4)}); np.random.seed(0)
    x = np.random.randn(100)
    ax = sns.distplot(x)

* 123456

![SouthEast](http://img.blog.csdn.net/20170404100426548?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 只绘制核密度曲线，不绘制直返图
    ax = sns.distplot(x, rug=True, hist=False)

* 12

![SouthEast](http://img.blog.csdn.net/20170404100653996?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 横着放
    ax = sns.distplot(x, vertical=True)

* 12

![SouthEast](http://img.blog.csdn.net/20170404100737028?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 5.2.核密度图kdeplot

    # 绘制核密度图
    import numpy as np; np.random.seed(10)
    import seaborn as sns; sns.set(color_codes=True)
    mean, cov = [0, 2], [(1, .5), (.5, 1)]
    x, y = np.random.multivariate_normal(mean, cov, size=50).T
    ax = sns.kdeplot(x)

* 123456

![SouthEast](http://img.blog.csdn.net/20170404101032610?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # shade参数决定是否填充曲线下面积
    ax = sns.kdeplot(x, shade=True, color="r")

* 12

![SouthEast](http://img.blog.csdn.net/20170404101116924?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 双变量密度图，相当于等高线图了
    # shade 参数改用颜色深浅表示密度的大小，不过不用，就真的是等高线了
    ax = sns.kdeplot(x, y, shade=True)

* 123

![SouthEast](http://img.blog.csdn.net/20170404101326802?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组绘制双变量的核密度图
    # 相当于绘制两个核密度图，通过图可以看到密度中心
    # 类似于挖掘算法中聚类中心绘图
    iris = sns.load_dataset("iris")
    setosa = iris.loc[iris.species == "setosa"]  # 组1
    virginica = iris.loc[iris.species == "virginica"]  # 组2
    
    ax = sns.kdeplot(setosa.sepal_width, setosa.sepal_length, 
                        cmap="Reds", shade=True, shade_lowest=False)
    
    ax = sns.kdeplot(virginica.sepal_width, virginica.sepal_length, 
                        cmap="Blues", shade=True, shade_lowest=False)

* 123456789101112

![SouthEast](http://img.blog.csdn.net/20170404102034514?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 5.3.双变量关系图jointplot

joint，顾名思义，就是联合呀。 
Draw a plot of two variables with bivariate and univariate graphs.

kind参数可以使用不同的图形反应两变量的关系，比如点图，线图，核密度图。

    # 默认绘制双变量的散点图，计算两个变量的直方图，计算两个变量的相关系数和置信度
    import numpy as np, pandas as pd; np.random.seed(0)
    import seaborn as sns; sns.set(style="white", color_codes=True)
    tips = sns.load_dataset("tips")
    g = sns.jointplot(x="total_bill", y="tip", data=tips)

* 12345

![SouthEast](http://img.blog.csdn.net/20170404102734588?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 通过kind参数，除了绘制散点图，还要绘制拟合的直线，拟合的核密度图
     g = sns.jointplot("total_bill", "tip", data=tips, kind="reg")

* 12

![SouthEast](http://img.blog.csdn.net/20170404103140921?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 使用六角形代替点图图
    g = sns.jointplot("total_bill", "tip", data=tips, kind="hex")

* 12

![SouthEast](http://img.blog.csdn.net/20170404103256233?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 绘制核密度图
    iris = sns.load_dataset("iris")
    g = sns.jointplot("sepal_width", "petal_length", data=iris, 
                        kind="kde", space=0, color="g")

* 1234

![SouthEast](http://img.blog.csdn.net/20170404103534051?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 控制图形的大小和颜色
    g = sns.jointplot("total_bill", "tip", data=tips, 
                        size=5, ratio=3, color="g")

* 123

![SouthEast](http://img.blog.csdn.net/20170404103743502?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 5.4.变量关系组图pairplot

就是绘制dataframe中各个变量两两之间的关系图。 
在变量关系图中，最常见的就是 x-y的线图，x-y的散点图，x-y的回归图。其实这三者都可以通过lmplot绘制，只是控制不同的参数而已。x-y的线图，其实就是时间序列图，这里就不说了。 
这里又说一遍散点图，是为了和前面的因子变量散点图相区分，前面的因子变量散点图，讲的是不同因子水平的值绘制的散点图，而这里是两个数值变量值散点图关系。为什么要用lmplot呢，说白了就是，先将这些散点画出来，然后在根据散点的分布情况拟合出一条直线。但是用lmplot总觉得不好，没有用scatter来得合适。

    # x-y 的散点图，不画回归线，fit_reg=False
    
    tips = sns.load_dataset("tips")
    g = sns.lmplot(x="total_bill", y="tip", data=tips,
                    fit_reg=False,hue='smoker',scatter=True)
    
    # 只画回归线，不画散点图，scatter=False
    g = sns.lmplot(x="total_bill", y="tip", data=tips,
                    fit_reg=True,hue='smoker',scatter=False)

* 123456789

![SouthEast](http://img.blog.csdn.net/20170414231737873?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170414231750088?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    import seaborn as sns; sns.set(style="ticks", color_codes=True)
    iris = sns.load_dataset("iris")
    g = sns.pairplot(iris)

* 123

![SouthEast](http://img.blog.csdn.net/20170404104048122?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 分组的变量关系图，似乎很厉害啊
    g = sns.pairplot(iris, hue="species")

* 12

![SouthEast](http://img.blog.csdn.net/20170404104141373?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # hue 分组后，不同的组用不同的形状标记
    g = sns.pairplot(iris, hue="species", markers=["o", "s", "D"])

* 12

![SouthEast](http://img.blog.csdn.net/20170404104308599?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 当然也可以只取dataframe中的一部分变量绘图
    g = sns.pairplot(iris, vars=["sepal_width", "sepal_length"])

* 12

![SouthEast](http://img.blog.csdn.net/20170404104607347?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 对角线默认绘制直方图，当然也可以绘制核密度图
    g = sns.pairplot(iris, diag_kind="kde")
    # 相应的，两变量关系图，也可以绘制线性回归图

* 123

![SouthEast](http://img.blog.csdn.net/20170404104809632?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

![SouthEast](http://img.blog.csdn.net/20170404105022805?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

# 6.热力图

## 6.1.热力图heatmap

    import numpy as np; np.random.seed(0)
    import seaborn as sns; sns.set()
    uniform_data = np.random.rand(10, 12)
    ax = sns.heatmap(uniform_data)

* 1234

![SouthEast](http://img.blog.csdn.net/20170404110803282?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 改变颜色映射的值范围
    ax = sns.heatmap(uniform_data, vmin=0, vmax=1)

* 12

![SouthEast](http://img.blog.csdn.net/20170404110931345?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    Plot a dataframe with meaningful row and column labels:
    # 绘制x-y-z的热力图，比如 年-月-销量 的热力图
    flights = sns.load_dataset("flights")
    flights = flights.pivot("month", "year", "passengers")
    ax = sns.heatmap(flights)

* 12345

![SouthEast](http://img.blog.csdn.net/20170404111337246?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 绘制热力图，还要将数值写到热力图上
    ax = sns.heatmap(flights, annot=True, fmt="d")

* 12

![SouthEast](http://img.blog.csdn.net/20170404111610703?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 这个图在绘制缺失值分布有用，但是不知道怎么样。
    # Plot every other column label and don’t plot row labels 
    data = np.random.randn(50, 20)
    ax = sns.heatmap(data, xticklabels=2, yticklabels=False)

* 1234

![SouthEast](http://img.blog.csdn.net/20170404111836710?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

# 7.聚类图clustermap

暂时不知道怎么用，先这样吧。

# 8.时间序列图

tsplot函数说是绘制时间序列图，还不如说是绘制简单的线图更加合适吧，因为我在绘制带timestap时间索引的pandas.Series时，并没有自动升采样绘图，只是数据有有什么数据就画什么，这在时间序列上应该是不对的。

因为我遇到这样一种情况，一个产品只在上半年卖，从数据库中取出数据只有每年上半年的数据，下半年没有数据也应该填充为0才对啊，但是seaborn的tsplot没有这个功能。

下面先介绍tsplot绘制线图吧，传入一个list或者series，直接绘制线图。

## 8.1.tsplot时序图

    # Plot a trace with translucent confidence bands:
    # 绘制带有半透明置信带的轨迹：
    # data是多组list的组合，这时候应该绘制多条曲线才对啊，其实不是的，是多组list的均值的序列图（默认）
    import numpy as np; np.random.seed(22)
    import seaborn as sns; sns.set(color_codes=True)
    x = np.linspace(0, 15, 31)
    data = np.sin(x) + np.random.rand(10, 31) + np.random.randn(10, 1)
    ax = sns.tsplot(data=data)

* 12345678

![SouthEast](http://img.blog.csdn.net/20170404113042568?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # tsplot的参数不太懂，直接上图吧
    gammas = sns.load_dataset("gammas")
    ax = sns.tsplot(time="timepoint", value="BOLD signal", 
                    unit="subject", condition="ROI", data=gammas)

* 1234

![SouthEast](http://img.blog.csdn.net/20170404113306212?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 绘制不同的置信度拟合图，这个好用
    ax = sns.tsplot(data=data, ci=[68, 95], color="m")

* 12

![SouthEast](http://img.blog.csdn.net/20170404113410250?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    # 使用不同的统计函数，默认的是均值，这里是中位数
    ax = sns.tsplot(data=data, estimator=np.median)

* 12

![SouthEast](http://img.blog.csdn.net/20170404113647091?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 8.2.panda线图

pandas的dataframe本身也有绘图函数，对于常见的分析图形还是很方便的，而且可以在plot函数中指定title等

    sale4.loc[sale4['sku']=='SKU412946',['month','salecount']]\
         .plot(x='month',y='salecount',title='SKU412946')

* 12

![SouthEast](http://img.blog.csdn.net/20171130175655432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 8.3.采样的时序图

这里重点讲一下。如果时序中每天的数据都有还好说，如果没有，就需要采样了。

    def plot_ts_day(x,y):
        """绘制每天的时间序列图。
        需要注意的是，序列是不是连续的，也就是说某天的数据是没有的,因此需要采样至每天都有记录，原来数据没有的就填充0
        x:时间轴，string或者time类型,是一个seires
        y:值
        """
        # x转成时间类型Timestamp，y也转成list
        x=[pd.to_datetime(str(i)) for i in x]
        y=[i for i in y]
        s=pd.Series(y,index=x)
        s = s.resample(rule='D',fill_method='ffill') # 生采样没有的会被填充
        # 原来没有的就填充为0
        s[s.index]=0
        s[x]=y
        # 重建索引，画出来的图好看点
        x2 = [i.strftime('%Y-%m-%d') for i in s.index]
        s.index = x2
        # 画图，这里使用series的plot函数，而不是seaborn.tsplot函数
        s.plot()

* 12345678910111213141516171819

![SouthEast](http://img.blog.csdn.net/20170404115248271?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

    def plot_ts_month(x,y):
        """绘制月的时间序列图，每月一个数据点，而不是每天一个"""
        # 将x转成时间类型timestamp,y也转成list
        try:
            x = [pd.to_datetime(str(i)) for i in x]
        except:
            x=[pd.to_datetime(str(i)+'01') for i in x]
        y=[i for i in y]
        #
        s=pd.Series(y,index=x)
        # 降采样至月
        s = s.resample('M', label='right').sum().fillna(0)
        # 重建索引，这样画出来的图好看点
        s.index=[i.strftime('%Y%m') for i in s.index]
        s.plot()

* 123456789101112131415

![SouthEast](http://img.blog.csdn.net/20170404114959601?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 8.4.pandas分组的线图

说实话，到现在还没搞懂怎么用sns.tsplot绘制分组线图，但是任务紧急，就用pandas的dataframe自带方法plot来绘图了，其实也挺简单的。 
主要注意的是，尽量给dataframe或者series建立时间索引，不然x轴很难看的。

    # 绘制月销量图
    # 数据如下
    # year  month2  salecount
    # 2014       1        531
    # 2014       2        505
    
    # 建立索引，'201601'
    data.index = data['year'].map(str)+data['month2'].map(lambda x: str(x) if x>=10 else '0'+str(x))
    # 绘图，其实也就是和8.3的方法一致了
    data['salecount'].plot()

* 12345678910

分组的线图，比如seaborn中的hue参数，方法是，先将dataframe长表格式转成宽表格式（透视表），每列是不同的年。

    # 分组的线图
    # 转成透视表后，绘图
    data.pivot(index='month2',columns='year',values='salecount').plot(title='销量')
    
    # 当数据很大的时候，你想绘制分组的统计图，比如将不同产品，相同的年月的销量进行加或者均值后在绘制线图
    # 使用 aggfunc 参数即可，默认是mean
    data.pivot_table(index='month2',columns='year',values='salecount',aggfunc='sum') \
        .plot(title='销量',style='o-')

* 12345678

![SouthEast](http://img.blog.csdn.net/20170414153301654?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

图形格式选项

`# 图形参数
# style
# 图形的属性
# 1.color:颜色
# 1.1 r：红色
# 1.2 b：蓝色
# 1.3 g：绿色
# 1.3 y：黄色
#
# 2.数据标记markder
# 2.1 o：圆圈
# 2.2 .：圆点
# 2.2 d：棱形
#
# 3.线型linestyle
# 3.1 没有参数的话就是默认画点图
# 3.2 --：虚线
# 3.3 -：实线
#
# 4.透明度
# alpha
#
# 5.大小
# size`

* 123456789101112131415161712345

效果如下图： 
![SouthEast](http://img.blog.csdn.net/20170817172928585?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170817172937997?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170817172951341?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170817173002878?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast) 
![SouthEast](http://img.blog.csdn.net/20170817173012634?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc3V6eXUxMjM0NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

# 13.后话

这里只是简单说说seaborn常用的绘图函数而已，看seaborn官网上面有很多好看的图形样例，而这里的函数画出来的哪里有官网的好看啊。 
而且这里也没有说到具体的布局控制，颜色主题等，要想绘制精美的图形，还需要学习具体的参数设定啊。

不过这里提到的这些简要图形，对于普通的分析快速绘图足够用了。

使用心得以后补充吧。
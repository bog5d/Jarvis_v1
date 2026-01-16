---
created: 2018-01-30 13:58:04
jarvis_ai_meta:
  key_people:
  - 艾凌风(翻译)
  - Daetalus(校稿)
  mood: 平静
  summary: 王霞客阅读了一篇关于使用Pandas替代Excel完成常见数据处理任务的翻译文章。
  tagged_at: '2026-01-11 04:35:09'
  time_space:
    date: '2018-01-30'
    location: ''
source: http://python.jobbole.com/80870/
tags:
- 数据处理
- Excel
- Pandas
- Python
- 数据转换
updated: 2018-01-30 13:58:04
---

# 用Pandas完成Excel中常见的任务 - Python - 伯乐在线

# 用Pandas完成Excel中常见的任务

本文由 [伯乐在线](http://python.jobbole.com/) - [艾凌风](http://www.jobbole.com/members/hanxiaomax) 翻译，[Daetalus](http://www.jobbole.com/members/daetalus) 校稿。未经许可，禁止转载！
英文出处：[pbpython.com](http://pbpython.com/excel-pandas-comp.html)。欢迎加入[翻译组](http://group.jobbole.com/category/feedback/trans-team/)。

引言

本文的目的，是向您展示如何使用[pandas](http://pandas.pydata.org/) 来执行一些常见的Excel任务。有些例子比较琐碎，但我觉得展示这些简单的东西与那些你可以在其他地方找到的复杂功能同等重要。作为额外的福利，我将会进行一些模糊字符串匹配，以此来展示一些小花样，以及展示pandas是如何利用完整的Python模块系统去做一些在Python中是简单，但在Excel中却很复杂的事情的。

有道理吧？让我们开始吧。

### 为某行添加求和项

我要介绍的第一项任务是把某几列相加然后添加一个总和栏。

首先我们将[excel 数据](http://pbpython.com/extras/excel-comp-data.xlsx) 导入到pandas数据框架中。

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4 | importpandas aspd<br>importnumpy asnp<br>df=pd.read\_excel("excel-comp-data.xlsx")<br>df.head() |

![7cc829d3gw1enwrjfna2wj20sf0a2q77.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjfna2wj20sf0a2q77.jpg)
我们想要添加一个总和栏来显示Jan、Feb和Mar三个月的销售总额。

在Excel和pandas中这都是简单直接的。对于Excel，我在J列中添加了公式`sum(G2:I2)`。在Excel中看上去是这样的：

![7cc829d3gw1enwrjgcyasj20uk09edon.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjgcyasj20uk09edon.jpg)

下面，我们是这样在pandas中操作的：

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\["total"\]=df\["Jan"\]+df\["Feb"\]+df\["Mar"\]<br>df.head() |

![7cc829d3gw1enwrjh171jj20sg0dhn27.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjh171jj20sg0dhn27.jpg)

接下来，让我们对各列计算一些汇总信息以及其他值。如下Excel表所示，我们要做这些工作：

![7cc829d3gw1enwrjht6v7j20uv09l47l.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjht6v7j20uv09l47l.jpg)

如你所见，我们在表示月份的列的第17行添加了`SUM(G2:G16)`，来取得每月的总和。

进行在pandas中进行列级别的分析很简单。下面是一些例子：

Python

|     |     |
| --- | --- |
| 1   | ;html-script:false\]df\["Jan"\].sum(),df\["Jan"\].mean(),df\["Jan"\].min(),df\["Jan"\].max() |

Python

|     |     |
| --- | --- |
| 1   | ;html-script:false\](1462000,97466.666666666672,10000,162000) |

现在我们要把每月的总和相加得到它们的和。这里pandas和Excel有点不同。在Excel的单元格里把每个月的总和相加很简单。由于pandas需要维护整个DataFrame的完整性，所以需要一些额外的步骤。

首先，建立所有列的总和栏

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]sum\_row=df\[\["Jan","Feb","Mar","total"\]\].sum()<br>sum\_row |

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | ;html-script:false\]Jan1462000<br>Feb1507000<br>Mar717000<br>total3686000<br>dtype:int64 |

这很符合直觉，不过如果你希望将总和值显示为表格中的单独一行，你还需要做一些微调。

我们需要把数据进行变换，把这一系列数字转换为DataFrame，这样才能更加容易的把它合并进已经存在的数据中。`T` 函数可以让我们把按行排列的数据变换为按列排列。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_sum=pd.DataFrame(data=sum\_row).T<br>df\_sum |

![7cc829d3gw1enwrjit91jj2085021q34.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjit91jj2085021q34.jpg)

在计算总和之前我们要做的最后一件事情是添加丢失的列。我们使用`reindex`来帮助我们完成。技巧是添加全部的列然后让pandas去添加所有缺失的数据。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_sum=df\_sum.reindex(columns=df.columns)<br>df\_sum |

![7cc829d3gw1enwrjjck37j20hq024mxw.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjjck37j20hq024mxw.jpg)

现在我们已经有了一个格式良好的DataFrame，我们可以使用`append`来把它加入到已有的内容中。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_final=df.append(df\_sum,ignore\_index=True)<br>df\_final.tail() |

![7cc829d3gw1enwrjlgamyj20sg0a8gpo.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjlgamyj20sg0a8gpo.jpg)

### 额外的数据变换

另外一个例子，让我们尝试给数据集添加状态的缩写。

对于Excel，最简单的方式是添加一个新的列，对州名使用vlookup函数并填充缩写栏。

我进行了这样的操作，下面是其结果的截图：

![7cc829d3gw1enwrjkpgztj20wj09n129.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjkpgztj20wj09n129.jpg)

你可以注意到，在进行了vlookup后，有一些数值并没有被正确的取得。这是因为我们拼错了一些州的名字。在Excel中处理这一问题是一个巨大的挑战（对于大型数据集而言）

幸运的是，使用pandas我们可以利用强大的python生态系统。考虑如何解决这类麻烦的数据问题，我考虑进行一些模糊文本匹配来决定正确的值。

幸运的是其他人已经做了很多这方面的工作。[fuzzy wuzzy](http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/)库包含一些非常有用的函数来解决这类问题。首先要确保你安装了他。

我们需要的另外一段代码是州名与其缩写的映射表。而不是亲自去输入它们，谷歌一下你就能找到这段代码[code](http://www.cmmichael.com/blog/2006/12/29/state-code-mappings-for-python)。

首先导入合适的fuzzywuzzy函数并且定义我们的州名映射表。

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | ;html-script:false\]fromfuzzywuzzy importfuzz<br>fromfuzzywuzzy importprocess<br>state\_to\_code={"VERMONT":"VT","GEORGIA":"GA","IOWA":"IA","Armed Forces Pacific":"AP","GUAM":"GU",<br>"KANSAS":"KS","FLORIDA":"FL","AMERICAN SAMOA":"AS","NORTH CAROLINA":"NC","HAWAII":"HI",<br>"NEW YORK":"NY","CALIFORNIA":"CA","ALABAMA":"AL","IDAHO":"ID","FEDERATED STATES OF MICRONESIA":"FM",<br>"Armed Forces Americas":"AA","DELAWARE":"DE","ALASKA":"AK","ILLINOIS":"IL",<br>"Armed Forces Africa":"AE","SOUTH DAKOTA":"SD","CONNECTICUT":"CT","MONTANA":"MT","MASSACHUSETTS":"MA",<br>"PUERTO RICO":"PR","Armed Forces Canada":"AE","NEW HAMPSHIRE":"NH","MARYLAND":"MD","NEW MEXICO":"NM",<br>"MISSISSIPPI":"MS","TENNESSEE":"TN","PALAU":"PW","COLORADO":"CO","Armed Forces Middle East":"AE",<br>"NEW JERSEY":"NJ","UTAH":"UT","MICHIGAN":"MI","WEST VIRGINIA":"WV","WASHINGTON":"WA",<br>"MINNESOTA":"MN","OREGON":"OR","VIRGINIA":"VA","VIRGIN ISLANDS":"VI","MARSHALL ISLANDS":"MH",<br>"WYOMING":"WY","OHIO":"OH","SOUTH CAROLINA":"SC","INDIANA":"IN","NEVADA":"NV","LOUISIANA":"LA",<br>"NORTHERN MARIANA ISLANDS":"MP","NEBRASKA":"NE","ARIZONA":"AZ","WISCONSIN":"WI","NORTH DAKOTA":"ND",<br>"Armed Forces Europe":"AE","PENNSYLVANIA":"PA","OKLAHOMA":"OK","KENTUCKY":"KY","RHODE ISLAND":"RI",<br>"DISTRICT OF COLUMBIA":"DC","ARKANSAS":"AR","MISSOURI":"MO","TEXAS":"TX","MAINE":"ME"} |

这里有些介绍模糊文本匹配函数如何工作的例子。

Python

|     |     |
| --- | --- |
| 1   | ;html-script:false\]process.extractOne("Minnesotta",choices=state\_to\_code.keys()) |

Python

|     |     |
| --- | --- |
| 1   | ;html-script:false\]('MINNESOTA',95) |

Python

|     |     |
| --- | --- |
| 1   | ;html-script:false\]process.extractOne("AlaBAMMazzz",choices=state\_to\_code.keys(),score\_cutoff=80) |

现在我知道它是如何工作的了，我们创建自己的函数来接受州名这一列的数据然后把他转换为一个有效的缩写。这里我们使用score\_cutoff的值为80。你可以做一些调整，看看哪个值对你的数据来说比较好。你会注意到，返回值要么是一个有效的缩写，要么是一个`np.nan` 所以域中会有一些有效的值。

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | ;html-script:false\]defconvert\_state(row):<br>abbrev=process.extractOne(row\["state"\],choices=state\_to\_code.keys(),score\_cutoff=80)<br>ifabbrev:<br>returnstate\_to\_code\[abbrev\[0\]\]<br>returnnp.nan |

把这列添加到我们想要填充的单元格，然后用NaN填充它

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_final.insert(6,"abbrev",np.nan)<br>df\_final.head() |

![7cc829d3gw1enwrjlgamyj20sg0a8gpo.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjlgamyj20sg0a8gpo.jpg)

我们使用`apply` 来把缩写添加到合适的列中。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_final\['abbrev'\]=df\_final.apply(convert\_state,axis=1)<br>df\_final.tail() |

![7cc829d3gw1enwrjm47syj20sq0czdkd.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjm47syj20sq0czdkd.jpg)
我觉的这很酷。我们已经开发出了一个非常简单的流程来智能的清理数据。显然，当你只有15行左右数据的时候这没什么了不起的。但是如果是15000行呢？在Excel中你就必须进行一些人工清理了。

### 分类汇总

在本文的最后一节中，让我们按州来做一些分类汇总（subtotal）。

在Excel中，我们会用`subtotal` 工具来完成。

![7cc829d3gw1enwrjmx3zxj20wr0b211b.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjmx3zxj20wr0b211b.jpg)

输出如下：

![7cc829d3gw1enwrjni3fbj20di07z41y.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjni3fbj20di07z41y.jpg)
在pandas中创建分类汇总，是使用`groupby` 来完成的。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]df\_sub=df\_final\[\["abbrev","Jan","Feb","Mar","total"\]\].groupby('abbrev').sum()<br>df\_sub |

![7cc829d3gw1enwrjo6l1zj208h0dy0vr.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjo6l1zj208h0dy0vr.jpg)

然后，我们想要通过对data frame中所有的值使用 `applymap` 来把数据单位格式化为货币。

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | ;html-script:false\]defmoney(x):<br>return"${:,.0f}".format(x)<br>formatted\_df=df\_sub.applymap(money)<br>formatted\_df |

![7cc829d3gw1enwrjouzwoj20a30dwadw.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjouzwoj20a30dwadw.jpg)

格式化看上去进行的很顺利，现在我们可以像之前那样获取总和了。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]sum\_row=df\_sub\[\["Jan","Feb","Mar","total"\]\].sum()<br>sum\_row |

Python

|     |     |
| --- | --- |
| 1<br>2<br>3<br>4<br>5 | ;html-script:false\]Jan1462000<br>Feb1507000<br>Mar717000<br>total3686000<br>dtype:int64 |

把值变换为列然后进行格式化。

Python

|     |     |
| --- | --- |
| 1<br>2<br>3 | ;html-script:false\]df\_sub\_sum=pd.DataFrame(data=sum\_row).T<br>df\_sub\_sum=df\_sub\_sum.applymap(money)<br>df\_sub\_sum |

![7cc829d3gw1enwrjpdqfcj20a3023mxf.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjpdqfcj20a3023mxf.jpg)

最后，把总和添加到DataFrame中。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]final\_table=formatted\_df.append(df\_sub\_sum)<br>final\_table |

![7cc829d3gw1enwrjq3bpvj20am0e1gps.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjq3bpvj20am0e1gps.jpg)

你可以注意到总和行的索引号是‘0’。我们想要使用`rename` 来重命名它。

Python

|     |     |
| --- | --- |
| 1<br>2 | ;html-script:false\]final\_table=final\_table.rename(index={0:"Total"})<br>final\_table |

![7cc829d3gw1enwrjqtu68j20aw0dyq73.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/7cc829d3gw1enwrjqtu68j20aw0dyq73.jpg)

### 结论

到目前为止，大部分人都已经知道使用pandas可以对数据做很多复杂的操作——就如同Excel一样。因为我一直在学习pandas，但我发现我还是会尝试记忆我是如何在Excel中完成这些操作的而不是在pandas中。我意识到把它俩作对比似乎不是很公平——它们是完全不同的工具。但是，我希望能接触到哪些了解Excel并且想要学习一些可以满足分析他们数据需求的其他替代工具的那些人。我希望这些例子可以帮助到其他人，让他们有信心认为他们可以使用pandas来替换他们零碎复杂的Excel，进行数据操作。

我发现这个练习会帮助我加强记忆。我希望这对你来说同样有帮助。如果你有一些其他的Excel任务想知道如何用pandas来完成它，请通过评论来告诉我，我会尽力帮助你。

> **打赏支持我翻译更多好文章，谢谢！**
> 
> [打赏译者](http://python.jobbole.com/80870/#rewardbox)

1 赞 6 收藏 [评论](http://python.jobbole.com/80870/#article-comment)

### 关于作者：[艾凌风](http://www.jobbole.com/members/hanxiaomax)

翻译组的勤务员（联系此人请微博私信或hanxiaomax@qq.com [个人主页](http://www.jobbole.com/members/hanxiaomax) · [我的文章](http://python.jobbole.com/author/hanxiaomax/) · [95](http://www.jobbole.com/members/hanxiaomax/reputation/) ·    

<http://group.jobbole.com/22945/>

[![bfdcef89gy1fknwaqrq59j20h803caau.jpg](./_resources/用Pandas完成Excel中常见的任务_-_Python_-_伯乐在线.resources/bfdcef89gy1fknwaqrq59j20h803caau.jpg)](http://group.jobbole.com/22945/)
---
created: 2017-12-14 22:11:45
jarvis_ai_meta:
  key_people:
  - 李笑来(作家/投资人)
  - 乔先生(朋友/同事)
  mood: 热情、乐于分享
  summary: 作者分享了使用Markdown和CSS进行微信公众号排版的三种技术方案及工具推荐。
  tagged_at: '2026-01-11 02:38:01'
  time_space:
    date: '2017-12-14'
    location: ''
source: http://hongbowei.com/using-markdown-css-to-complete-typesetting.html
tags:
- 技术方案
- Markdown
- CSS
- 排版
- 微信公众号
updated: 2017-12-14 22:11:45
---

# Markdown + CSS 实现微信公众号排版 - 爱浪漫的程序媛

好技能啊，点赞点赞

* * *

## Markdown + CSS 实现微信公众号排版

> 本文版权归作者所有，转载请注明作者和出处。
> 未经作者许可，请勿将本文用作商业用途。
> 封面来源：见图片水印

**Markdown** 是一种轻量级的标记语言，它的文本可以转换为 **HTML** ，加上 CSS 的样式控制，能够很方便快捷进行文章排版。Markdown 解决了一文多处投放（_微信公众号+博客_）以及排版的问题。

**CSS** 指层叠样式表 (Cascading Style Sheets)，样式定义如何**显示 HTML 元素**，样式通常存储在样式表中，外部样式表可以极大提高工作效率，外部样式表通常存储在 CSS 文件中。

我们发布在网络各处的文章，最终都会被转换为 HTML 进行展示，因此，当不需要复杂排版时，**Markdown + CSS** 完全可以满足我们的排版需求，比如本文。

* * *

理论陈述完毕，在介绍具体操作流程之前，我们再来介绍几个接下来会用到的小工具。（_注：_这些工具所提供的功能都可以用其他工具替代，这里提到它们，单纯因为，我测试的时候用的这几个。）

#### 1\. Markdown Here

Markdown Here 是个浏览器插件（Chrome/Firefox/Safari），可以将浏览器中编辑器里的 Markdown 文本转换成渲染过后的 HTML，它的另一个特点是允许用户自定义渲染 HTML 的 CSS 。

#### 2\. 任意一款 Markdown 编辑器

Markdown 编辑器有千千万，在线的也有很多。如果对自己的 Markdown 语法够自信，不需要预览，其实用记事本写完存成(.md)文件也可以的。

#### 3\. Github

Github 是一家公司，主要提供基于 git 的版本托管服务。目前并可能未来长期是本星球上最流行的开源托管服务提供商，程序员们的不具名简历集散地（通过询问一只程序猿在 Github 上的代码贡献量来评价ta是一个什么样的程序猿）。另外，Github 本身支持 Markdown 的在线编辑。

* * *

工具介绍完毕，进入实践。

### 0\. 解决方案

1. Markdown Here + 自定义 CSS

* 支持自定义 CSS 的 Markdown 编辑器（**以下简称 Editor S**） + 自定义 CSS
* 不支持自定义 CSS 的 Markdown 编辑器（**以下简称 Editor US**） + 自定义 CSS + Github

### 1\. 操作流程

#### 方案一：Markdown Here + 自定义 CSS

> 1. 在 Google Chrome 中安装 Markdown Here 插件

* 配置 Markdown Here Option, 自定义一些 CSS
* 在 Atom/Sublimetext 之类的编辑器中书写
* 拷贝粘贴到微信公共帐号的编辑器中
* 使用 Markdown Here 渲染
* 插图图片，修订
* 发布……

#### 方案二：Editor S + 自定义 CSS

> 1. 自定义一些 CSS 并保存为文件

* 在 Editor S 中导入自定义的 CSS 文件
* 在 Editor S 中书写
* 导出渲染后的 HTML ，复制粘帖到微信公众号的编辑器中
* 插图，修订
* 发布……

#### 方案三：Editor US + 自定义 CSS + Github

> 1. 自定义一些 CSS 并保存为文件
> 2. 上传 CSS 文件到 Github 并生成源文件外链
> 3. 在 Editor US 书写的最开始插入 HTML 代码 `<link href="https://vivienbh.github.io/CodeBlock/Markdown-here/markdown-here.css" rel="stylesheet"></link>`
> 4. 在 EDI US 中书写其他内容
> 5. 导出渲染后的 HTML ，复制粘贴到微信公众号的编辑器中
> 6. 插图，修订
> 7. 发布……

### 2\. 关于 Markdown 编辑器

试过若干 Markdown 编辑器，在线的，离线的，还差一点儿就想去尝试李笑来推荐的 Atom （这两个属于程序编辑器，Markdown编辑只是辅助功能）。在群里看到网友推荐 _MWeb_ 之前，我一直都在使用 _Macdown_ ，一款基于开源项目 _Mou_ 的 Markdown 编辑器。现在，我在用 MWeb ，一款 运行在 OS X 以及 iOS 上的编辑器软件，支持 Github Flavored Markdown 语法（意味着它支持LaTex）。两款软件都支持自定义 CSS ，除了没有写作模版之外，其他的功能都灰常好用，并且这些好用的功能还免费。而我选择其中一个的原因，迟些时候，会在另一篇关于Wordpress写作的文章中提到。

对于辛勤耕耘在 Windows 上的同学，抛开 Github 的在线编辑器，MarkdownPad 是我目前能找到的还算能凑合用的编辑器。但是这款编辑器的自定义 CSS 功能是收费的，因此，我写下了方案三。

关于 Markdown 基础语法以及其他可用的编辑器，可以去看看这篇文章。4月15日我也许会重开一次关于 Markdown 写作的微课，平台暂定千聊，课程免费，欢迎带着问题来提问。（_附上课程邀请卡_）

> [关于 Markdown 你可能想知道的](http://t.cn/R6SKZOt)

[![1.jpg](./_resources/Markdown_+_CSS_实现微信公众号排版_-_爱浪漫的程序媛.resources/1.jpg)](http://ob0109bz1.bkt.clouddn.com/wp-content/uploads/2017/03/invitation-card.jpg)

邀请卡

### 3\. 关于中文排版

关于中文排版，我直接拷贝了李笑来教程的原话，重点只有三个：

> * 字体大小
> * 行间距
> * 字间距
> 
> 至于选择哪一种字体，其实并不是关键，因为对字体来说，最重要的其实是“通用” —— 即便是你设置好了你喜欢的字体，先不说那是不是你自己的偏好，更重要的是，若是读者的设备上没有那个字体，那你就等于是白折腾了……

鉴于微信中「微软雅黑」是通用字体，看着蛮顺眼，所以，我直接选了它。中文字体若是不设置行间距和字间距的话，在手机上读起来很费劲，另外很多人跟我反映大一点的字体尺寸，以上这些，除了字体，李笑来都做了。我在他的基础上进行了一些小修改。

李笑来版本：

    .markdown-here-wrapper {
      font-size: 16px;
      line-height: 1.8em;
      letter-spacing: 0.1em;
    }
    

我的版本：

    .markdown-here-wrapper {
      font-size: 16px;
      line-height: 1.8em;
      letter-spacing: 0.1em;
      font-family: 微软雅黑;
    }
    

注：**`.markdown-here-wrapper`**是插件 Markdown Here 的自定义标签，如果你使用的不是方案一，那么需要将其替换为 HTML 标签 **`body`**。

### 4\. 关于配色

经过乔先生漫长的吐槽以及挑刺，我最终有两个配色方案，一个是基于李笑来配色方案的修改版（本文采用的配色），一个是没采用 Markdown + CSS 排版之前一直使用的粉色系模板的配色方案。如果你已经有自己固定的配色方案，把它照搬过来就是；如果还没有，要么上网找一个，要么自己配一个。附上 Google Material Design 的 Color Scheme：

> <https://material.google.com/style/color.html>

我的**加粗**与_倾斜_样式配色如下：

    strong, b{
      color: #009688;
    }
    
    em, i {
      color: #BF360C;
    }
    

### 5\. 关于自定义 CSS

在自定义 CSS 里的设置不起作用的话，试试在后面补上!important，就好像这样：

    h2 {
      font-size: 20px !important;
    }
    

其他，请去 **W3School** 速成一下，附上网址：

> <http://www.w3school.com.cn/css/css_intro.asp>

英文好的同学也可以去 **codecademy** 上个 10 小时的课_Learn HTML & CSS: Part I_，培训 HTML 与 CSS 基础：

> <https://www.codecademy.com/learn/learn-html-css>

### 6\. 关于 Markdown Here 与 GFW

也许会有人因为 **GFW** 的原因没有办法安装 Markdown Here，如果你还不会爬墙，可以试试最基础的梯子 **Latern** ，同样是一个 Chrome 插件。另一个选择是，采用方案二或者方案三，这样会额外生成一个 HTML 文件（微信公众号关闭了对 HTML 纯文本的支持，如果有大神能够告诉怎么避免生成 HTML 文件那就最好了，前端我不太懂）。

Chrome 的插件数据是跟帐户同步的，也就是说，只要你能够在 Chrome 上保持 Google 帐户在线，那么不管你换多少台电脑，都不用重新配置 Markdown Here。如果你的 Markdown Here 不好使，尝试更新 Chrome 到最新版本。

### 7\. 我的 StyleSheet

网上的 Markdown Here CSS 一大把，可以找自己喜欢的，然后进行修改配置。本文所使用的 CSS 样式，在前面已经给出地址，初始来源是 Github，原始作者是李笑来。

### 8\. 参考文献

> 1. Markdown Here 教程（by 李笑来）
> 2. CSS 简介（from W3School）
> 3. 如何高效利用 Github （by 阳志平）
> 4. 关于 Markdown 你可能想知道的 （by 我自己）

嗯，以上是今天的全部内容，谢谢。

— End —

[![1.1.jpg](./_resources/Markdown_+_CSS_实现微信公众号排版_-_爱浪漫的程序媛.resources/1.1.jpg)](http://ob0109bz1.bkt.clouddn.com/wp-content/uploads/2017/04/qr-logo-20170312.jpg)
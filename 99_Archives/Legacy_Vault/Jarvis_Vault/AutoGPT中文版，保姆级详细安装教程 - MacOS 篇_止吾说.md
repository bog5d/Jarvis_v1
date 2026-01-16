---
created: 2023-05-06 21:38:11
jarvis_ai_meta:
  key_people:
  - Hossie(开源项目贡献者)
  mood: 平静
  summary: 用户收藏了一篇关于在MacOS系统上安装中文版AutoGPT的详细教程文章。
  tagged_at: '2026-01-11 02:00:43'
  time_space:
    date: '2023-05-06'
    location: ''
source: https://www.zhiwu300.com/612.html
tags:
- AI工具
- 技术分享
- 安装教程
- MacOS
- AutoGPT
updated: 2023-05-08 12:03:44
---

# AutoGPT中文版，保姆级详细安装教程 - MacOS 篇_止吾说

<https://www.zhiwu300.com/>

* [工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)

* [调色工具](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA/%E8%B0%83%E8%89%B2%E5%B7%A5%E5%85%B7)

* [LUT(影视视频调色)](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA/lut%E5%BD%B1%E8%A7%86%E8%A7%86%E9%A2%91%E8%B0%83%E8%89%B2)
* [LUT(平面照片调色)](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA/lut%E5%B9%B3%E9%9D%A2%E7%85%A7%E7%89%87%E8%B0%83%E8%89%B2)

* [AE插件](https://www.zhiwu300.com/%E6%8F%92%E4%BB%B6%E4%B8%93%E5%8C%BA/ae%E6%8F%92%E4%BB%B6)

* [PR插件](https://www.zhiwu300.com/%E6%8F%92%E4%BB%B6%E4%B8%93%E5%8C%BA/pr%E6%8F%92%E4%BB%B6)
* [达芬奇插件](https://www.zhiwu300.com/%E6%8F%92%E4%BB%B6%E4%B8%93%E5%8C%BA/%E8%BE%BE%E8%8A%AC%E5%A5%87%E6%8F%92%E4%BB%B6)
* [FCPX插件](https://www.zhiwu300.com/%E6%8F%92%E4%BB%B6%E4%B8%93%E5%8C%BA/fcpx%E6%8F%92%E4%BB%B6)
* [教程专区](https://www.zhiwu300.com/%E6%95%99%E7%A8%8B%E4%B8%93%E5%8C%BA)
* [音效专区](https://www.zhiwu300.com/%E9%9F%B3%E6%95%88%E4%B8%93%E5%8C%BA)
* [字体专区](https://www.zhiwu300.com/%E5%AD%97%E4%BD%93%E4%B8%93%E5%8C%BA)
* [往期视频](https://www.zhiwu300.com/%E5%BE%80%E6%9C%9F)
___[_登录_](https://www.zhiwu300.com/612.html#)___
____

# AutoGPT中文版，保姆级详细安装教程 - MacOS 篇

 [![unknown_filename.7.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.7.png)](https://www.zhiwu300.com/author/kkdtpz)  [工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)  
_1周前_
__0_ __625___

___

当前位置：1. _[首页](https://www.zhiwu300.com/)_

* _[工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)_
* _正文_

_

> 首先来简单的介绍 一下AutoGPT，簡單的說，AutoGPT 相當於給基於 GPT 的模型一個記憶體和一個身體。有了它，你可以把一項任務交給 AI 智慧體，讓它自主性地提出一個計畫，然後執行計畫。此外其還能連結網際網路、長期和短期記憶體管理、用於文本生成的 GPT-4 實例以及使用 GPT-3.5 進行檔案儲存和產生摘要等功能。AutoGPT 用處很多，可用來分析市場並提出交易策略、提供客戶服務、進行行銷等其他需要持續更新的任務。

### 為什麼AutoGPT這麼紅：整個過程完全不用人類插手！

AutoGPT 正在網際網路上掀起一場風暴，它無處不在。很快，已經有網友上手實驗了，該使用者讓 AutoGPT 建立一個網站，不到 3 分鐘 AutoGPT 就成功了。期間 AutoGPT 使用了 React 和 Tailwind CSS，全憑自己，人類沒有插手。

> 首先要感谢大神 @Hossie 对AutoGPT的汉化和开源。下面附上大神的 youtube 频道和 GitHub 项目地址。
> 
> ![unknown_filename.10.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.10.png)

[Hossie油管频道地址](https://www.youtube.com/@Hossie)      [Hossie的GitHub 项目地址](https://github.com/RealHossie/Auto-GPT-Chinese)

下面就进入正题，首先如果你想要安装AutoGPT，需要具备以下条件，

* 一台电脑或者一台服务器（必备）

* 科学的上网环境（必备）
* Git （必备）_
_* Python 3.10及更高的版本（必备）_
_* GitHub账号及访问权限（必备）_
_* ChatGPT  API 接口权限3.5版本，如果有4更好（必备）_
_* Pinecone API 接口权限（可选）
	
	###### 用途
	
	Pinecone API 是一种云原生的向量搜索服务，能够高效地存储、检索和排序数百万或数十亿个高维向量，支持快速相似度搜索和聚类。它可以帮助开发人员构建和部署基于向量的机器学习和深度学习应用程序，包括推荐系统、搜索引擎、图像和语音识别等。使用Pinecone 可以把对话记忆存储在Pinecone的服务器，不占用本地资源，同时访问和读取的速度也比本地要快上很多。
	
* 谷歌搜索API接口权限 （可选）
	
	###### 用途
	
	正常情况下是不需要配置谷歌的 API 服务的，但是如果在使用谷歌搜索时出现『错误429』的话，就需要配置谷歌 API 了。
	
* Eleven Labs 语音接口（可选）
	
	###### 用途
	
	这是语音服务的接口，如果你需要回答的同时用语音来朗读，就需要开启这个接口。
	
* HuggingFace图像生成接口（可选）
	
	###### 点击展开
	
	Auto-GPT 自带 OpenAI 自家的 DALL-e 文图模型，你可以命令它输出想要的图像，但是如果想用更流行更好的 Stable Diffusion 模型，需要申请 HuggingFace 的 API
	
上面提到的所有 API接口申请和使用方法，点击下方按钮即可直达。
[AutoGPT全功能 API 接入指南](https://www.zhiwu300.com/618.html)

满足以上必备条件之后，就可以往下看了！

# MacOS篇

#### 一、运行环境准备

1. 一般 MAC 电脑在使用过程中都会自动的安装 Git。查询MAC电脑是否安装 Git很方便，只需要打开终端输入 git 回车即可，如果安装了会提示版本号，如果没安装直接就会弹出安装窗口，安装即可。
	
	    git
	
	[Git 官网-点击进入](https://gitforwindows.org/)![unknown_filename.9.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.9.png)
	
2. 下载并安装 Python，安装完成后打开终端输入python3，如果出现版本号就是安装成功了。
	
	    python3
	
	[Python官网-点击进入](https://www.python.org/)![unknown_filename.23.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.23.png)
	
3. 下载并安装 VSCode[VSCode官网-点击进入](https://code.visualstudio.com/)![unknown_filename.18.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.18.png)

#### 二、克隆Auto-GPT-Chinese项目到本地

1. 打开“终端”直接运行下方命令
	
	    git clone https://github.com/RealHossie/Auto-GPT-Chinese.git
	
	![unknown_filename.8.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.8.png)
	
2. 输入下方命令进入Auto-GPT-Chinese文件夹
	
	    cd Auto-GPT-Chinese
	
	![unknown_filename.2.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.2.png)
	
3. 输入下方命令来安装所有需要的依赖，时间较长请耐心等待（代理开全局，避免出现下载中断）。
	
	    pip install -r requirements.txt
	
	![unknown_filename.20.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.20.png)
	
4. 出现一大片英文的时候就说明安装完成了。![unknown_filename.11.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.11.png)

#### 三、配置.env文件

1. 打开“访达”，找到 Auto-GPT-Chinese 文件夹。路径如下  `/Users/你的电脑名/Auto-GPT-Chinese`
2. 按下快捷键 `command+shift+.`  显示隐藏文件![unknown_filename.1.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.1.png)
3. 运行 VSCode,点击打开![unknown_filename.19.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.19.png)
4. 选择 Auto-GPT-Chinese文件夹![unknown_filename.13.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.13.png)
5. 左侧找到 “.env.template”文件，右键重命名为“.env”![unknown_filename.6.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.6.png)![unknown_filename.17.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.17.png)
6. 然后在右侧找到`OPENAI_API_KEY=`  在后面填入你的ChatGPT API keys（获取方法详见本帖顶端）![unknown_filename.5.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.5.png)
7. 保存文件![unknown_filename.14.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.14.png)
8. 左侧双击“main.py”，再点击右上角的运行按钮![unknown_filename.15.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.15.png)
9. 然后点击右下角向上的箭头，把终端界面放大即可![unknown_filename.12.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.12.png)
10. 输入如下代码运行Auto-GPT中文版
	
	    python -m autogpt --gpt3only
	
	![unknown_filename.24.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.24.png)
	

**声明：**本站所有文章，如无特殊说明或标注，均为本站原创发布。任何个人或组织，在未征得本站同意时，禁止复制、盗用、采集、发布本站内容到任何网站、书籍等各类媒体平台。如若本站内容侵犯了原著者的合法权益，可联系我们进行处理。

[![unknown_filename.7.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.7.png)kkdtpz](https://www.zhiwu300.com/author/kkdtpz) 
_打赏_ __海报_ __链接___

___

[_
上一篇 AutoGPT中文版，保姆级详细安装教程 - Windows 篇
_](https://www.zhiwu300.com/592.html)
_
[下一篇 AutoGPT 全功能API 接入指南 （云记忆、联网、语音朗读、图像生成）](https://www.zhiwu300.com/618.html)
_

__

### 相关文章

[![unknown_filename.21.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.21.png)](https://www.zhiwu300.com/588.html)

## [Photoshop 2023 for mac(ps 2023) v24.2.0/ACR15.2中文版 支持M1/M2-持续更新](https://www.zhiwu300.com/588.html)

[工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)
_2周前_
__65__

__

[![unknown_filename.4.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.4.png)](https://www.zhiwu300.com/581.html)

## [Photoshop 2023_24.4.1.449 (PS2023) WINX64+神经滤镜-持续更新](https://www.zhiwu300.com/581.html)

[工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)
_2周前_
__83__

__

<https://www.zhiwu300.com/534.html>

## [还是来了！我们要失业了！一句话生成大电影，Gen-2震撼发布，后期已经哭晕在厕所](https://www.zhiwu300.com/534.html)

[工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)
_1月前_
__129__

__

[![unknown_filename.16.jpeg](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.16.jpeg)](https://www.zhiwu300.com/424.html)

## [Parallels Desktop 18.1.1破解版（永久授权）](https://www.zhiwu300.com/424.html)

[工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6)
_1月前_
__231__

______

___

### 发表回复

您的电子邮箱地址不会被公开。 必填项已用\*标注

插入图片
浏览器会保存昵称、邮箱和网站cookies信息，下次评论时使用。

搜索
搜索

[![unknown_filename.3.jpeg](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.3.jpeg)](https://www.zhiwu300.com/618.html)

## [AutoGPT 全功能API 接入指南 （云记忆、联网、语音朗读、图像生成）](https://www.zhiwu300.com/618.html)

_1周前_

_

[![unknown_filename.22.jpeg](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.22.jpeg)](https://www.zhiwu300.com/612.html)

## [AutoGPT中文版，保姆级详细安装教程 - MacOS 篇](https://www.zhiwu300.com/612.html)

_1周前_

_

[![unknown_filename.jpeg](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.jpeg)](https://www.zhiwu300.com/592.html)

## [AutoGPT中文版，保姆级详细安装教程 - Windows 篇](https://www.zhiwu300.com/592.html)

_1周前_

_

[![unknown_filename.21.png](./_resources/AutoGPT中文版，保姆级详细安装教程_-_MacOS_篇_止吾说.resources/unknown_filename.21.png)](https://www.zhiwu300.com/588.html)

## [Photoshop 2023 for mac(ps 2023) v24.2.0/ACR15.2中文版 支持M1/M2-持续更新](https://www.zhiwu300.com/588.html)

_2周前_

___

##### ___下载热度排行榜___

* ___1 [Adobe CC for Win版全套破解版下载](https://www.zhiwu300.com/377.html)___

* ___2 [Adobe CC Mac版全套破解版下载 支持Mac M1/M2 芯片](https://www.zhiwu300.com/371.html)___
* ___3 [CorelDRAW 2019 学习版（大家珍惜）](https://www.zhiwu300.com/381.html)___
___

在线客服
在线客服

QQ客服

* [止吾说](http://wpa.qq.com/msgrd?v=3&uin=8295066&site=qq&menu=yes)

* <http://wpa.qq.com/msgrd?v=3&uin=&site=qq&menu=yes>

Copyright © 2021 [RiPro-V2](http://ritheme.com/) - All rights reserved[京ICP备18888888号-1](https://beian.miit.gov.cn/)[京公网安备 188888888](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=188888888)

* <https://www.zhiwu300.com/>

_* <https://www.aliyun.com/minisite/goods?userCode=u4kxbrjo>
_* <https://www.zhiwu300.com/user?action=vip>
_* <https://www.zhiwu300.com/user>
_* <http://wpa.qq.com/msgrd?v=3&uin=8295066&site=qq&menu=yes>
_

_

* [_首页_](https://www.zhiwu300.com/)

_* [_分类_](https://www.zhiwu300.com/uncategorized)
_* [_问答_](https://www.zhiwu300.com/question)
_* [_我的_](https://www.zhiwu300.com/user)
_* _顶部_
_

_

全部

全部



_

_

[LUT(平面照片调色)](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA/lut%E5%B9%B3%E9%9D%A2%E7%85%A7%E7%89%87%E8%B0%83%E8%89%B2) [LUT(影视视频调色)](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA/lut%E5%BD%B1%E8%A7%86%E8%A7%86%E9%A2%91%E8%B0%83%E8%89%B2) [M1芯片](https://www.zhiwu300.com/tag/m1%E8%8A%AF%E7%89%87) [安装方法](https://www.zhiwu300.com/tag/%E5%AE%89%E8%A3%85%E6%96%B9%E6%B3%95) [工具软件](https://www.zhiwu300.com/%E5%B7%A5%E5%85%B7%E8%BD%AF%E4%BB%B6) [往期视频](https://www.zhiwu300.com/%E5%BE%80%E6%9C%9F) [教程专区](https://www.zhiwu300.com/%E6%95%99%E7%A8%8B%E4%B8%93%E5%8C%BA) [未分类](https://www.zhiwu300.com/uncategorized) [调色专区](https://www.zhiwu300.com/%E8%B0%83%E8%89%B2%E4%B8%93%E5%8C%BA)

_

_

_

<https://www.zhiwu300.com/612.html#>

_
_

×

### _欢迎信息！_

_感谢您来到全网牙最少博主！ 止吾的资源分享网站。_

________________________________
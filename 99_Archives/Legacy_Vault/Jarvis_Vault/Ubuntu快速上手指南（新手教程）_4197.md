---
created: 2019-11-02 17:29:19
jarvis_ai_meta:
  key_people: []
  mood: 平静
  summary: 用户（zhyadn）整理了一份详尽的Ubuntu新手教程，涵盖软件安装与常用命令。
  tagged_at: '2026-01-11 02:42:17'
  time_space:
    date: '2019-08-21'
    location: ''
source: http://www.360doc.com/content/19/0821/10/33031165_856196988.shtml
tags:
- 新手教程
- Linux命令
- 技术指南
- Ubuntu
- 软件安装
updated: 2019-11-02 17:29:19
---

# Ubuntu快速上手指南（新手教程）

[![nlogo.jpg](./_resources/Ubuntu快速上手指南（新手教程）.resources/nlogo.jpg)](http://www.360doc.com/index.html)
[![dingtu.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/dingtu.gif)
我的图书馆](http://www.360doc.com/login.aspx?reurl=http://www.360doc.com/content/19/0821/10/33031165_856196988.shtml)
[留言交流](http://www.360doc.com/advice.html)

 [![unknown_filename.png](./_resources/Ubuntu快速上手指南（新手教程）.resources/unknown_filename.png)](http://www.360doc.com/) 

[zhyadn](http://www.360doc.com/userhome/33031165) / [程序设计](http://www.360doc.com/userhome.aspx?userid=33031165&cid=100) / [Ubuntu快速上手指南（新手教程）](#)

[](#)[](#)**0** [](#)**0** [](#)**1**

分享

[](#)[](#)[](#)[](#)[](#)

[更多](#)

![bgcolor.jpg](./_resources/Ubuntu快速上手指南（新手教程）.resources/bgcolor.jpg)
![fontSize.jpg](./_resources/Ubuntu快速上手指南（新手教程）.resources/fontSize.jpg)

## Ubuntu快速上手指南（新手教程）

2019-08-21 [zhyadn](http://www.360doc.com/userhome/33031165)  阅 102  转 1

[转藏到我的图书馆](#)

### 软件安装篇

#### 1.安装搜狗输入法（Ubuntu16.04）

1. 下载搜狗输入法
	去搜狗输入法官网下载deb包：<http://pinyin.sogou.com/linux/?r=pinyin>
	1. 切换到deb包所在的目录，并执行以下命令：
		sudo dpkg -i deb包名
	2. 在执行过程中，会产生由于缺少相关依赖文件的错误。执行以下命令，安装所缺少的依赖文件：
		sudo apt-get -f install
	3. 安装完成后，再安装一次搜狗输入法
		sudo dpkg -i deb包名
2. 在“语言支持”面板，添加汉语支持，并将输入法系统设置为fcitx。
3. 注销系统，重新登录。在Dash中搜索fcitx configuartion，在Input Method中添加和配置sogoupinyin即可

#### 2.安装flashplugin-installer

1. 安装flashplugin-installer
	sudo apt-get install flashplugin-installer

安装完成后，重启浏览器即可正常播放视频

#### 3.安装Chrome

1. 下载安装包
	wget <https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb>
2. 安装所需要的依赖包
	sudo apt-get -f install libappindicator1 libindicator7
3. 安装chrome
	sudo dpkg -i google-chrome-stable\_current\_amd64.deb
4. 启动chrome
	google-chrome

#### 4.安装为知笔记

1. 添加软件源
	sudo add-apt-repository ppa:wiznote-team
2. 更新软件源
	sudo apt-get update
3. 安装为知笔记
	sudo apt-get install wiznote
4. 启动为知笔记
	WizNote

#### 5.安装小书匠

1. [下载小书匠安装包](http://soft.xiaoshujiang.com/)
2. 解压安装包
	切换到安装包所在的目录，通过输入unzip + 文件名将文件解压到当前目录，例如：
	unzip Story-writer-linux64.zip
3. 运行小书匠
	切换到解压出来的文件夹根目录，然后输入./Story-writer即可成功运行小书匠。

#### 6.安装JDK

1. [JDK8下载地址](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
2. 解压已下载的tar.gz包，切换工作目录到jdk所在的目录，例如：cd Downloads
	sudo tar zxvf jdk-8u92-linux-x64.tar.gz
3. 将解压出来的文件夹移动到合适的文件夹，一般为/opt/Java
	sudo mkdir -p /opt/Java
	sudo mv jdk1.8.0\_92 /opt/Java
4. 通过编辑~/.bashrc文件来配置环境变量
	gedit ~/.bashrc
5. 在~/.bashrc添加一下几行代码：
	export JAVA\_HOME=/opt/Java/jdk1.8.0\_92
	export CLASSPATH=_J__A__V__A__H__O__M__E_/_l__i__b__e__x__p__o__r__t__P__A__T__H_\=JAVAHOME/libexportPATH\={JAVA\_HOME}/bin:$PATH
6. 让对~/.bashrc文件的更改即可生效
	source ~/.bashrc
7. 测试jdk
	java
	javac

#### 7.安装Eclipse

1. 安装Eclipse
	sudo apt-get install eclipse
2. 启动Eclipse
	eclipse

#### 8.安装git

    sudo apt-get install git
    

#### 9.安装rar压缩和解压工具

    sudo apt-get install rar
    sudo apt-get install unrar
    

#### 11.安装genymotion

    sudo chmod u+x genymotion-2.7.2-linux_x64.bin
    ./genymotion-2.7.2-linux_x64.bin
    

#### 12.安装网易云音乐

1. [下载网易云音乐安装包](http://music.163.com/#/download)
2. 使用dpkg -i 安装包名命令安装网易云音乐，例如：
	sudo dpkg -i netease-cloud-music\_0.9.0-1\_amd64.deb
3. 运行网易云音乐
	netease-cloud-music

#### 14.安装shadowsocks

1. 添加软件源
	sudo add-apt-repository ppa:hzwhuang/ss-qt5
2. 更新软件源
	sudo apt-get update
3. 安装shadowsocks
	sudo apt-get install shadowsocks-qt5
4. 运行Shadowsocks-Qt5
	在Dash中搜索Shadowsocks-Qt5点击图标即可运行，然后配置相关参数即可使用
	具体文档请查看[shadowsocks指南](https://github.com/shadowsocks/shadowsocks-qt5/wiki)

#### 15\. 安装Gnome3

以下是安装方法：

> sudo add-apt-repository ppa:gnome3-team/gnome3
> sudo apt-get update
> sudo apt-get dist-upgrade
> sudo apt-get install gnome-themes-standard ubuntu-desktop gnome-shell

删除方法：

> sudo apt-get install ppa-purge
> sudo ppa-purge ppa:gnome3-team/gnome3

#### 16.开启telnet服务

1. 查看telnet服务是否已开启
	netstat -a | grep telnet
	如果输出为空，表示没有开启该服务
2. 安装telnet服务
	sudo apt-get install telnetd
3. 查看telnet运行状态
	netstat -a | grep telnet
	输出：tcp　　0　　0 _:telnet_ :\*　　LISTEN
	此时表明已经开启了telnet服务。
4. telnet登陆测试
	telnet 127.0.0.1

#### 17.安装TeamViewer

1. 去TeamViewer官网下载linux版本deb包
2. 安装deb包
	sudo dpkg -i 包名
	如果出现缺少依赖包的错误提示信息，则执行第3步之后，再执行
	sudo dpkg -i 包名
3. 安装缺少的依赖包
	sudo apt-get -f install

#### 18.安装ubuntu受限的额外的解码器

“ubnutu 额外受限”指的是这些解码器的包没有默认安装在ubuntu系统里面，这些解码器没有默认安装在系统里面的原因是受到很多国家的法律的约束。 Canonical不能默认安装他们，但是如果你要安装这些解码器，你将使用不是ubuntu软件库的软件。但是不用担心，安装这些解码器是安全的（不会 破坏你的计算机）。在这些解码器安装完以后你将没有任何阻碍的播放很多格式的媒体格式，如MP3，MP4，AVI和以及其他的一些格式。安装这些解码器通 过使用下面的命令。
sudo apt-get install ubuntu-restricted-extras
注意：对于那些初学者，如果屏幕上出现那些协议，条款，按Tab键在选项之间切换，使用enter确认你的选择。

#### 19.安装VLC媒体播放器

sudo apt-get install vlc

#### 20.安装Terminaltor

sudo apt-get install terminaltor

#### 21\. 安装Dock

#### 22\. 安装Docky

#### 23\. 安装IntelliJ IDEA

### 常用命令篇

#### 1.文件操作命令之增删改查——增

    1.创建多级目录：例如在根目录下创建一个/firstLevel/secondLevel/thirdLevel三级目录
    sudo mkdir -p /firstLevel/secondLevel/thirdLevel
    2. 递归拷贝目录
    sudo cp -r 要拷贝的目录名 目标路径
    3. 拷贝文件
    sudo cp 要拷贝的文件名 目标路径

#### 2.文件操作命令之增删改查——删

1. 删除空目录：例如删除一个名为empty的目录
	sudo rmdir empty
	或者
	sudo rm empty
2. 递归删除非空目录，即删除该目录以及该目录下的所有文件：例如删除一个名为full的非空目录
	sudo rm -rf full
3. 删除文件
	sudo rm 文件名

#### 3.文件操作命令之增删改查——改

1. 文件重命名
	sudo mv 原文件名 目标文件名
2. 移动文件
	sudo mv 原文件名 目标路径

#### 4.文件操作命令之增删改查——查

#### 5.mount挂载命令

1. 查看已挂载的分区状态
	mount | column -t
2. 查看所有分区
	fdisk -l

#### 6\. 解压/压缩文件

1. 压缩
	tar -cvf jpg.tar \*.jpg //将目录里所有jpg文件打包成tar.jpg
	tar -czf jpg.tar.gz \*.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用gzip压缩，生成一个gzip压缩过的包，命名为jpg.tar.gz
	tar -cjf jpg.tar.bz2 \*.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用bzip2压缩，生成一个bzip2压缩过的包，命名为jpg.tar.bz2
	tar -cZf jpg.tar.Z \*.jpg //将目录里所有jpg文件打包成jpg.tar后，并且将其用compress压缩，生成一个umcompress压缩过的包，命名为jpg.tar.Z
	rar a jpg.rar \*.jpg //rar格式的压缩（如果没有安装rar，使用sudo apt-get install rar安装）
	zip jpg.zip \*.jpg //zip格式的压缩（如果没有安装zip,使用sudo apt-get install zip安装）
2. 解压
	tar -xvf file.tar //解压 tar包
	tar -xzvf file.tar.gz //解压tar.gz
	tar -xjvf file.tar.bz2 //解压 tar.bz2
	tar -xZvf file.tar.Z //解压tar.Z
	unrar e file.rar //解压rar（如果没有安装zip,使用sudo apt-get install unrar安装）
	unzip file.zip //解压zip（如果没有安装zip,使用sudo apt-get install unzip安装）

#### 7\. 进行系统更新和软件更新

sudo apt-get update
sudo apt-get upgrade 或者 sudo apt-get dist-upgrade

#### 8.md5校验文件的完整性和合法性

    md5sum 文件名
    

#### 9.ubuntu没声音

    alsamixer
    执行sudo alsactl store，配置将保存到/etc/asound.state。 
    

#### 10.设置root密码

    sudo passwd root
    

#### 11\. Ubuntu下自定义桌面图标

1. 在/usr/share/applications目录下创建名为xxx.desktop文件
2. 将下面内容复制到创建的文件中
3. 根据你的需求自定义你的桌面图标，
	下面是一个MyEclipse应用程序的图标文件myeclipse.desktop，内容如下：
	\[Desktop Entry\]
	Version=1.0
	Type=Application
	Terminal=false
	Name=MyEclipse
	Exec=/home/skyward/MyEclipse\\ 2015/myeclipse
	Comment=Integrated Android developer tools for development and debugging.
	Icon=/usr/share/icons/hicolor/scalable/apps/myeclipse
	Categories=GNOME;GTK;Development;IDE;

其中，Name属性是图标名称，Exec属性是程序的可执行文件绝对路径，Comment属性是注释
Icon属性是图标所在的绝对路径。

将dos格式文件批量转换成unix格式文件
<http://www.cnblogs.com/ini_always/archive/2012/03/23/2413023.html>

### 常用shell脚本篇

#### 1\. 递归打印当前目录下的所有文件（目录文件及普通文件）

    #!/bin/bash
    #    统计目录下文件个数，
    #    如果只要文件不要目录，
    #    就加上是文件的判断 [ -f ]
    #    
    i=0
    for file in $(ls -R)
    do
        i=$(( $i + 1 ))
        echo $i : $file
    done
    echo $i

#### 2.递归打印当前目录下的所有目录文件

    #!/bin/bash
    #递归打印当前目录下的所有目录文件。  
    PRINTF()
    {
    ls $1 | while read line
    #一次读取每一行放到line变量中
    do
      [ -d $1/$line ] && {
             DIR="$1/$line"
             echo $DIR
          }
         DIR1=`dirname $DIR`
    #求路径。
         A=`ls -F $DIR1 | grep / | grep "\<$line\>"`
         #判断line是不是一个目录。
         if [ "$A" == "$line/" ];then
             PRINTF "$DIR1/$line"
        #递归调用。
           fi
    done
    }
    PRINTF .

#### 3.递归打印指定目录下的所有普通文件（若不指定路径，则打印当前路径下的所有普通文件）

    #!/bin/bash  
    
    # $1是运行脚本时，输入的第一个参数，这里指的是使用者希望搜索的目录  
    # 下面的代码是对目录进行判断，如果为空则使用脚本所在的目录；否则，搜索用户输入的目录  
    if [[ -z "$1" ]] || [[ ! -d "$1" ]]; then  
        echo "The directory is empty or not exist!"  
        echo "It will use the current directory."  
        nowdir=$(pwd)  
    else  
        nowdir=$(cd $1; pwd)  
    fi  
    echo "$nowdir"  
    
    # 递归函数的实现  
    function SearchCfile()  
    {  
        cd $1  
        #这里可以修改为判断文件类型，如.c,.java等等文件类型，修改一下grep条件就可以了  
        cfilelist=$(ls -l | grep "^-" | awk '{print $9}')  
        for cfilename in $cfilelist  
        do  
            echo $cfilename  
        done  
    # 遍历当前目录，当判断其为目录时，则进入该目录递归调用该函数；  
        dirlist=$(ls)  
        for dirname in $dirlist　　　　　　  
        do  
            if [[ -d "$dirname" ]];then  
                cd $dirname  
                #SearchCfile 这里有bug，跳转到根目录了  
                #这里把当前的目录作为参数输入  
                SearchCfile $(pwd)  
                cd ..  
            fi;  
        done;  
    }  
    
    # 调用上述递归调用函数  
    SearchCfile $nowdir

本站是提供个人知识管理的网络存储空间，所有内容均由用户发布，不代表本站观点。如发现有害或侵权内容，请点击这里 或 拨打24小时举报电话：4000070609 与我们联系。

[转藏到我的图书馆](#) [献花（0）](#) 分享： [微信](#)

来自： [zhyadn](http://www.360doc.com/userhome/33031165) \> [《程序设计》](http://www.360doc.com/userhome.aspx?userid=33031165&cid=100)

[举报](#)

推一荐：[发原创得奖金，“原创奖励计划”来了！](http://www.360doc.com/pages/Wallet/bonus.html)  |  [浓浓思乡情，有奖征文邀你分享！](http://www.360doc.com/pages/activity/activity30.html)

上一篇：[移动 Ubuntu16.04 桌面左侧的启动器到屏幕底部](http://www.360doc.com/content/19/0821/10/33031165_856195256.shtml)

下一篇：[UBUNTU的默认root密码是多少，修改root密码](http://www.360doc.com/content/19/0821/11/33031165_856203093.shtml)

[**23岁小伙娶46岁富婆，婚后多次入院！医生摇头没救了！**广告](http://s3.nzbdw.com/s?type=2&r=20&mv_ref=www.360doc.com&enup=CAABcfiY/wgAAv+Y+HEA&mvid=ODgxOTE5NjE5Mjg0ODExMTIxMTAwMTc&bid=13b13d5c1dc8cc7c&price=AAAAAF29S/AAAAAAAAq2QxisK4lmX3t+l7pU9A==&finfo=DAABCAABAAAADAgAAgAAABUEAAM/QijwpMUrtgAIAAIAAAADCgADYqhW9ySvjTsIAAQAAAAVBgAGLbcGAAoAAAgADgAAABUKAA8AAAAAAAXzcwA&ugi=FYjJGRXGi0tMFQIVKhUqFQAAFZrep4gCJcgBFoDwtv+1lssFHBavqqCZ/ITNj44BFQAAAA&uai=FfCcngIlNBUEFsa2xrTa96aoxQEV8ggl+ceq+wMlABUaFAAcFuXswInx+8zZzwEVAAAA&ubi=FYCcXhWaufACFdrcgBkV9pSWXBUEFRwW9LaHwxcWxrbbm+S9q6jFATQCFqCAkIAIJQYVwOSWmQEVggYVADaGyoGY8a6it0YVAAA&clickid=0&cpx=__OFFSET_X__&cpy=__OFFSET_Y__&cs=__EVENT_TIME_START__&ce=__EVENT_TIME_END__&adsw=__ADSPACE_W__&adsh=__ADSPACE_H__&csign2=DO2pzOahYqj=&url=http%3A%2F%2Fxs.chezhuobang.cn%2F002)

[](#)
**猜你喜欢**

0条评论

[发表](#)

请遵守用户 [评论公约](http://www.360doc.com/agreement.html)

**类似文章** [更多](http://www.360doc.com/relevant/856196988_more.shtml)

		[ubuntu 常用命令](http://www.360doc.com/content/10/1123/19/2617151_71802887.shtml)
	
	[拷贝文件和目录最常用参数:-b —-为每个已经存在的目的文件作个备份-d —-遇到软链接时不拷贝软链接所指向的文件;拷贝时保留links属性(链接数)-p —-保留文件的访问权限,所有者,...](http://www.360doc.com/content/10/1123/19/2617151_71802887.shtml)
	
		[StarDict（星际译王）字典软件 for ubuntu - lubobill1990的日志 - 网易博客](http://www.360doc.com/content/10/1210/16/5018129_76806705.shtml)
	
	[StarDict（星际译王）字典软件 for ubuntu - lubobill1990的日志 - 网易博客 本人安装用下来感觉很好，最主要可以自定义字典，查单词和取词的字典可以不同，比如查单词时使用牛津英汉词典，取词是...](http://www.360doc.com/content/10/1210/16/5018129_76806705.shtml)
	
* [![748107224_1.jpg](./_resources/Ubuntu快速上手指南（新手教程）.resources/748107224_1.jpg)](http://www.360doc.com/content/18/0423/16/18945873_748107224.shtml)
	
	[构建ubuntu根文件系统](http://www.360doc.com/content/18/0423/16/18945873_748107224.shtml)
	
	[构建ubuntu根文件系统。Ubuntu Core是Ubuntu的一个精简版本，只包含Ubuntu根文件系统的核心部分，默认没有图形界面等等。在Ubuntu主机中...](http://www.360doc.com/content/18/0423/16/18945873_748107224.shtml)
	
* [![863099861_1.jpg](http://thumbnail1.360doc.com/DownloadImg/2019/10/1804/i109/863099861_1.jpg)](http://www.360doc.com/content/19/0925/11/61082271_863099861.shtml)
	
	[职场妈妈深夜求助：孩子不听话、老公搞暧昧都不是摧毁女人的致命武器，而是……](http://www.360doc.com/content/19/0925/11/61082271_863099861.shtml)
	
	[职场妈妈深夜求助：孩子不听话、老公搞暧昧都不是摧毁女人的致命武器，而是……日本女医生吉田穗波，是一个有着五个孩子的职场妈妈。为...](http://www.360doc.com/content/19/0925/11/61082271_863099861.shtml)
	

		[搞定Ubuntu 12.04 + Kile+ Texlive2013+CJK](http://www.360doc.com/content/14/0314/22/965235_360657789.shtml)
	
	[搞定Ubuntu 12.04 + Kile+ Texlive2013+CJK.首先，wordlink_affiliate" sizcache="17" sizset="44">Ubuntu12.04源中的Kile，默认安装的是 Texlive2009，这个版本对CJK的支...](http://www.360doc.com/content/14/0314/22/965235_360657789.shtml)
	
		[ubuntu 10.04 开机后没有登陆对话框 桌面一片空白 解决办法](http://www.360doc.com/content/15/0203/18/9408846_446014858.shtml)
	
	[今天打开ubuntu，结果发现到了登录阶段的时候桌面一片空白，没有登录框？？？！！然后搜了一下，看到有人说是安装zlib-1.2.5的缘故，然后果断卸载了zlib，果然解决了问题，过程是这样的：这里注意一下...](http://www.360doc.com/content/15/0203/18/9408846_446014858.shtml)
	
* [![215794364_1.jpg](http://thumbnail1.360doc.com/DownloadImg/2012/06/0412/i52/215794364_1.jpg)](http://www.360doc.com/content/12/0604/12/8890849_215794364.shtml)
	
	[Ubuntu下构建内核源码树](http://www.360doc.com/content/12/0604/12/8890849_215794364.shtml)
	
	[linux-source -Linux kernel source with Ubuntu patches.linux-source-2.6.32- Linux kernel source for version 2.6.32 with Ubuntu p...](http://www.360doc.com/content/12/0604/12/8890849_215794364.shtml)
	

		[ubuntu 安装ns2](http://www.360doc.com/content/13/0903/16/7832126_311866638.shtml)
	
	[ubuntu 安装ns2在ubuntu上装了好几次ns2了，但NS2是个麻烦的软件，经常出现一些问题，百般调试之后一直不能解决问题之后，只有重装。](http://www.360doc.com/content/13/0903/16/7832126_311866638.shtml)
	
		[Ubuntu 10.04下面安装MediaWiki](http://www.360doc.com/content/13/0806/18/13240348_305185406.shtml)
	
	[sudo apt-get install apache2 sudo apt-get install mysql-server mysql-client (中间要求设置密码，记住你设置的密码) sudo apt-get install php5 php5-mysql sudo apt-get install libgd2-xpm libgd...](http://www.360doc.com/content/13/0806/18/13240348_305185406.shtml)
	
		[Debian7 x64或Ubuntu 13.10 x64编译安装Wine 1.7的步骤](http://www.360doc.com/content/15/0116/11/597197_441258148.shtml)
	
	[然后运行：make install或者可以以非root用户的身份进入tools目录，运行：./wineinstall它会自动编译并安装程序，中间会提示输入管理员密码。安装到了/usr/local/bin目录下运行命令检查版本：wine64 --...](http://www.360doc.com/content/15/0116/11/597197_441258148.shtml)
	

 [![012.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/012.gif)](http://www.360doc.com/userhome/33031165) 

[zhyadn](http://www.360doc.com/userhome/33031165)

![userstar1.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/userstar1.gif)![userstar2.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/userstar2.gif)![userstar3.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/userstar3.gif)![userstar3.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/userstar3.gif)![userstar3.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/userstar3.gif)

[关注](#) [对话](#)

* [TA的最新馆藏 (共366篇)](http://www.360doc.com/userhome/33031165)

* [ubuntu下添加开机启动项](http://www.360doc.com/content/19/0829/02/33031165_857666683.shtml)
	[Red Hat Linux 安装教程](http://www.360doc.com/content/19/0829/00/33031165_857659291.shtml)
	[Ubuntu更新命令](http://www.360doc.com/content/19/0827/17/33031165_857401852.shtml)
	[ubuntu使用命令更新ubuntu系统](http://www.360doc.com/content/19/0827/17/33031165_857401661.shtml)
	[linux命令及全程详解](http://www.360doc.com/content/19/0827/11/33031165_857329398.shtml)
	[Linux常用命令英文全称及中文对照](http://www.360doc.com/content/19/0827/11/33031165_857328937.shtml)
	

喜欢该文的人也喜欢 [更多](http://www.360doc.com/readroom.html)

* [异性交往，如何选一个终生伴侣？这些“东西”很重要](http://www.360doc.com/content/19/1001/09/55422398_864370671.shtml)
	[年薪20万的大厨，教你5款干锅酱的配方和4个诀窍，5分钟就能学会](http://www.360doc.com/content/19/0528/07/62344734_838668524.shtml)
	[为什么陕西看起来像三个省？2946字 l 地缘谷](http://www.360doc.com/content/19/0527/08/57987571_838602668.shtml)
	[大厨教你秘制花椒油，又香又麻又好吃，用它下饭美味吃到停不下！](http://www.360doc.com/content/19/0615/12/49216685_842517037.shtml)
	[【中医秘方】治牙痛特效神方，1剂见效3剂痊愈！](http://www.360doc.com/content/19/0323/03/9986257_823513067.shtml)
	[《鸿蒙出世：中国神兽图鉴》](http://www.360doc.com/content/19/0811/01/17132703_854221831.shtml)
	[十三款秘制卤水技术配方，学会任意一款，有车有房不是梦](http://www.360doc.com/content/19/0809/08/32326570_853932705.shtml)
	[给儿子的一封信](http://www.360doc.com/content/13/1126/01/4609717_332280807.shtml)
	[入过狱，卖过艺，她说情义算个屁！](http://www.360doc.com/content/19/0905/08/40719971_859210962.shtml)
	

十一月全新spa项目，欢迎体验！ ¥ 十一月全 男士spa会所，50多种养生项目，别样的安逸与享受！ ¥ 男士sp 高端会所尊贵服务 ¥0 高端会所 spa水疗养生 ¥0 spa水

[关闭](#)

[关闭](#)

[![freeread.gif](./_resources/Ubuntu快速上手指南（新手教程）.resources/freeread.gif)](http://www.360doc.com/member/)

<http://www.360doc.com/content/19/0821/10/33031165_856196988.shtml#>
[](#)
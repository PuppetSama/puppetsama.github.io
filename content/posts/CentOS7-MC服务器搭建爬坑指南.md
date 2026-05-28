---
date: '2017-03-01'
draft: false
title: CentOS7 MC服务器搭建爬坑指南
url: /03/09/CentOS7-MC服务器搭建爬坑指南/
---

VPS系统为CentOS 7

### 首先更新系统

`yum -y update  
 yum -y upgrade`

### 安装配置JAVA

首先，MC需要JAVA环境。由于服务器是纯文本界面，在服务器上安装JAVA环境时选择本地下载JAVA的RPM安装包，然后通过xftp上传至服务器，在服务器进行安装。

JAVA环境设置这里就不再多提，不懂的话，可以自行去网上搜索。

### MC服务端下载

首先，我们需要下载MC的服务端文件。我选择了Cauldron（原MCPC+，可安装Mod）1.7.10版本。

下载[服务器文件](https://sourceforge.net/projects/cauldron-unofficial/files/1.7.10/),下载libraries文件即可，如图：  
![Alt text](http://omjz7so35.bkt.clouddn.com/mc-2-1-1.png)

下载好后，将libraries文件夹解压，将解压出来的文件上传到服务器。我上传到了“/home/mcserver”这个文件夹下，mcserver这个文件夹需要自己创建。  
![Alt text](http://omjz7so35.bkt.clouddn.com/blog/mc/mc-2-1-2.png)

### MC服务器设置

现在回到Putty，我们需要在服务器中安装一个工具：Screen。

首先我们在命令行中执行：

```
yum -y install screen
```

然后，创建一个新的Screen，命名为mc，用于启动管理MC服务器：

```
screen -S mc
```

然后切换到mcserver目录，建立启动脚本文件：

```
nano start.sh
```

新建start.sh文件，弹出编辑器窗口，粘贴内容如下：

```
#!/bin/sh         
java -Xmx768M -Xms512M -jar /home/mcserver/minecraft_server.1.7.10.jar
```

其中的minecraft\_server.1.7.10.jar为你的服务器文件，即当前目录下你上传的server.jar文件名。

按Ctrl + X退出，输入Y确定保存，然后回车。

执行命令，赋予脚本执行权限

```
chmod 777 start.sh
```

修改EULA文件，在命令行输入：

```
nano eula.txt
```

将eula=false改为eula=true

### 启动服务器

在启动服务器之前有一点需要注意，一般来说，Linux的安全组设置为仅开放22端口，而MC服务器所需端口号为25565，我们需要映射端口或者选择开放25565端口。

之后，运行启动脚本启动MC服务器：

```
sh ./start.sh
```

接下来，还有非常重要的一步：

要想让非正版客户端也可以连接服务器，还需要设置一下server.properties文件。

首先Ctrl + C 停止MC服务器

命令行输入：

```
nano server.properties
```

将

```
online-mode=true
```

改为

```
online-mode=false
```

保存后重新运行服务器。

搞定XD

下次我们使用Putty连接服务器时，只要使用命令：

```
screen -r mc
```

即可回到我们的MC服务器状态啦。

### 服务器mod安装

如果想手动添加mod服务,那么需要手动下载服务器文件下载 里边的cauldron-1.7.10-1.1388.1.0-server.jar (注意和你下载的libraries的版本要相同),然后放到服务器mc目录下,修改启动脚本 start.sh为:

```
#!/bin/sh
java -Xmx768M -Xms512M -jar /home/mcserver/cauldron-1.7.10-1.1388.1.0-server.jar
```

</code>  
就可以了。

这个时候不要去想，mod到底安装在哪里，先重新启动服务器：

```
sh ./start.sh
```

然后就会在mcserver目录下出现/mods。将希望添加的mod放进去就可以了。

### 客户端mod安装

安装mod请从官网下载，这样可以确保mod的纯净性和可用性。

安装前需要先安装forge，不要试图绕过他，除非你要玩原生版。

> 参考于Sinton’s Blog <https://sintonwong.github.io>
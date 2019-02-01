### 事前准备: 下载本工具
在[本页面](https://github.com/HHHHhgqcdxhg/azurlane-unpack)点击Clone or download后点击Download ZIP下载本工具,下载完成后解压
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr32nu9cuj30kx0af0tw.jpg)  
### 事前准备: 准备碧蓝航线原文件
将手机或模拟器中的Android/data目录下的com.bilibili.azurlane拷贝到本工具目录.
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr39j1efwj30ik0ezta4.jpg)  
注意:原手机或模拟器上必须是打开过一次游戏,才能下载完整游戏资源
### 事前准备: 安装python
> 注意,本文接下来介绍做的事将为系统安装一个python环境,如果之前系统上有python环境,自己又不懂的则请谨慎选择是否继续.打开一个cmd,输入python回车,如果显示系统找不到python,则代表没有安装python环境
1. 点击链接下载python3.6.4安装文件: [https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe](https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe)  
2. 运行下载好的exe
**务必选中Add Python 3.6 to PATH**
![务必选中Add Python 3.6 to PATH](https://ws1.sinaimg.cn/large/006WuIpegy1fzr2vg5stmj30im0bgwgp.jpg)  
3. 点击Install Now就完事了;  
如果你不想装到C盘,而选择Customize installation的话,**这一步一定要勾选pip**![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr2y9v03pj30im0bg76l.jpg)  
之后一直下一步就完事了
### 事前准备: 安装库
1. 在本工具目录下打开命令行窗口:进入本工具目录,在空白处,按住键盘上shift键右击,点击"在此处打开命令窗口",之后输入```pip install -r requirements.txt```回车,等待下载完毕.  
注意,按住shift右键时,不能有选中的文件,最好先在空白处左键点击一下,再shift+右键
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr3hcuhk6j30c30bzt97.jpg)
2. 下载安装unityPack库
    点击链接[https://github.com/HearthSim/UnityPack/archive/0.9.0.zip](https://github.com/HearthSim/UnityPack/archive/0.9.0.zip)下载UnityPack,下载完成后解压,进入解压后的文件夹,在空白处按住shift右键在此处打开命令窗口,输入```python setup.py install```回车
## 使用
回到本工具目录,在此处打开命令窗口,输入```python main -h```回车,能看到如下图所示的帮助,恭喜你已经可以正常使用该工具了,接下来可以前往[github.com/HHHHhgqcdxhg/azurlane-unpack#使用](https://github.com/HHHHhgqcdxhg/azurlane-unpack#%E4%BD%BF%E7%94%A8)查看具体使用  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzrb5obj2sj30g20730sx.jpg)

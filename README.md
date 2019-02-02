# azurlane-unpack	
碧蓝航线图片拆包工具  	
一条命令将 原文件 或 目录下的所有文件中的图片 解包导出  	
notice:  
- 不出意外应该只限windows系统下使用	
-  解包只限图片
### 使用准备
1. 在[本页面](https://github.com/HHHHhgqcdxhg/azurlane-unpack)点击Clone or download后点击Download ZIP下载本工具,下载完成后解压  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr32nu9cuj30kx0af0tw.jpg)  
2. 将手机或模拟器中的Android/data目录下的com.bilibili.azurlane拷贝到本工具目录.  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzr39j1efwj30ik0ezta4.jpg)  
注意:原手机或模拟器上必须是打开过一次游戏,才能下载完整游戏资源  
3. 在本工具目录下打开命令行窗口: 进入本工具目录,在空白处,按住键盘上shift键右击,点击"在此处打开命令窗口"  
之后输入```./unpack -h```回车,能看到如下图所示的帮助,则表示可以正常使用该工具了  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzsghtpoexj30gv08at8z.jpg)
### 使用
- ```./unpack -f com.bilibili.azurlane\files\AssetBundles\painting\aidang_h_tex```  
-f 后面跟文件位置,将只解包该文件,如输入上面命令将解包爱宕立绘  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzsgm85a8xj3115021mx6.jpg)  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzrc4q9ockj30if05c0sx.jpg)	
- ```./unpack -d com.bilibili.azurlane\files\AssetBundles\painting -w 4```  
-d 后面跟文件目录,将解包该目录下所有文件,如输入上面命令将解包全部立绘  
-w 后面跟数字,指定解包并行的进程数,默认跑满CPU  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzsgtj8ivmj3120087gmi.jpg)  
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzrc45oxxjj30vc0a9jsa.jpg)	
- ```./unpack```  
直接执行将跑满CPU,解包com.bilibili.azurlane下所有文件  

注意: 指定文件或文件夹时,使用com.bilibili.azurlane开头的路径,如上面两个示例  

输出在本工具目录中的output文件夹
## 性能	
实测使用Intel Core i7 2.6GHz 4核CPU的设备,使用最大进程数  
解包全部文件大概2分20秒左右  
解包全部立绘(com.bilibili.azurlane\files\AssetBundles\painting)需要25秒左右
## 参考
本项目~~参考~~照抄了以下代码  
- KiraFanWiki白井姐姐的assertsDownloader.py(私有repo)  
- [Goodjooy/AzurLane-PaintingExtract](https://github.com/Goodjooy/AzurLane-PaintingExtract)  
- [Ericsson/ETCPACK](https://github.com/Ericsson/ETCPACK)

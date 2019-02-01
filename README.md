# azurlane-unpack
碧蓝航线图片拆包工具  
一条命令将原文件或目录下的所有文件中的图片解包导出
notice: 不出意外应该只限windows使用
## 准备
将下载好的游戏资源存到本项目根目录下的com.bilibili.azurlane中
然后执行
```
pip install -r requirements.txt
python main -h
```
UnityPack包没有pip,需要下载后```python setup.py install```安装  
UnityPack releases: [https://github.com/HearthSim/UnityPack/releases](https://github.com/HearthSim/UnityPack/releases)  


> 如果你看上面的几行没有看亲人般熟悉,可以请点击查看[详细的使用方法](https://github.com/HHHHhgqcdxhg/azurlane-unpack/blob/master/greenhand.md)
## 使用
- ```python main -f com.bilibili.azurlane\files\AssetBundles\painting\aidang_h_tex```  
-f 后面跟文件位置,将只解包该文件,如输入上面命令将解包爱宕立绘
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzrc4q9ockj30if05c0sx.jpg)
- ```python main -d com.bilibili.azurlane\files\AssetBundles\painting -w 4```
-d 后面跟文件目录,将解包该目录下所有文件,如输入上面命令将解包全部立绘  
-w 后面跟数字,指定解包并行的进程数,默认跑满CPU
![](https://ws1.sinaimg.cn/large/006WuIpegy1fzrc45oxxjj30vc0a9jsa.jpg)
- ```python main```
直接执行将跑满CPU,解包com.bilibili.azurlane下所有文件

输出在本工具目录中的output文件夹

## 性能
实测使用Intel Core i7 2.6GHz 4核CPU的设备,使用最大进程数,解包全部文件大概2分15秒左右,只解包立绘(com.bilibili.azurlane\files\AssetBundles\painting)需要30秒左右

## 参考
本项目~~参考~~照抄了以下代码
- KiraFanWiki白井姐姐的assertsDownloader.py(私有repo)
- [Goodjooy/AzurLane-PaintingExtract](https://github.com/Goodjooy/AzurLane-PaintingExtract)
- [Ericsson/ETCPACK](https://github.com/Ericsson/ETCPACK)

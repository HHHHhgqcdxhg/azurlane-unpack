import sys,os
from argparse import ArgumentParser

from azurlaneUnpack import Azurlane_unpack

CWD = os.path.dirname(os.path.abspath(__file__))

class AzurlaneUnpackControl:
    def __init__(self,args):
        self.parse_args(args)
        self.azurlaneUnpack = Azurlane_unpack(QUALITY=self.args.quality)

    def run(self):
        if self.args.file:
            ret = self.azurlaneUnpack.unpackTexture(self.args.file)
            if ret:
                oPath,_ = os.path.split(ret[0])
                os.startfile(oPath)
        else:
            self.args.works = int(self.args.works)
            allFiles = self.azurlaneUnpack.list_all_files(self.args.directorie)
            self.azurlaneUnpack.unpackTextureAllFutureP(allFiles,self.args.works)
            outPath = os.path.join(CWD, "output",self.args.directorie)
            os.startfile(outPath)
        self.clearEtcPackTmp()

    def clearEtcPackTmp(self):
        for file in os.listdir(CWD):
            if file[-12:] == "alphaout.pgm" or file[-7:]=="tmp.ppm":
                os.remove(file)

    def parse_args(self,args):
        p = ArgumentParser()
        p.add_argument('-f', '--file', help="input a file path begin with com.bilibili.azurlane\n输入需要解包的文件目录,以com.bilibili.azurlane开头")
        p.add_argument('-d','--directorie',default="com.bilibili.azurlane\\files\\AssetBundles", help="input a directorie path begin with com.bilibili.azurlane, default com.bilibili.azurlane\\files\\AssetBundles \n输入需要解包的文件夹目录,以com.bilibili.azurlane开头, 默认为com.bilibili.azurlane\\files\\AssetBundles")
        p.add_argument('-w','--works',default=os.cpu_count(), help="max works to handdle files, default os.cpu_count()\n 处理解包的最大进程数,默认跑满CPU")
        p.add_argument('-q','--quality',default=80, help="extract image quality, default 80\n 导出图片的质量,默认80")
        self.args = p.parse_args(args)
        self.args.quality = int(self.args.quality)
        if not 0<=self.args.quality<=100:
            self.args.quality = 80

if __name__ == '__main__':

    # ass = ['-f', 'x', '-d', 'com.bilibili.azurlane']
    ass = sys.argv[1:]
    # if not ass:
    #     ass = ['-h']
    app = AzurlaneUnpackControl(ass)
    # app.clearEtcPackTmp()
    app.run()

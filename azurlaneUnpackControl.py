import sys,os
from argparse import ArgumentParser

from azurlaneUnpack import Azurlane_unpack

CWD = os.path.dirname(os.path.abspath(__file__))
azurlaneUnpack = Azurlane_unpack()
class AzurlaneUnpackControl:
    def __init__(self,args):
        self.parse_args(args)

    def run(self):
        if self.args.file:
            azurlaneUnpack.unpackTexture(self.args.file)
        else:
            allFiles = azurlaneUnpack.list_all_files(self.args.directorie)
            azurlaneUnpack.unpackTextureAllFutureP(allFiles,self.args.works)
        self.clearEtcPackTmp()

    def clearEtcPackTmp(self):
        for file in os.listdir(CWD):
            if file[-12:] == "alphaout.pgm" or file[-7:]=="tmp.ppm":
                os.remove(file)

    def parse_args(self,args):
        p = ArgumentParser()
        p.add_argument('-f', '--file', help="input a file path begin with com.bilibili.azurlane\n输入需要解包的文件目录,以com.bilibili.azurlane开头")
        p.add_argument('-d','--directorie',default="com.bilibili.azurlane\\files\\AssetBundles", help="input a directorie path begin with com.bilibili.azurlane, default com.bilibili.azurlane\\files\\AssetBundles \n输入需要解包的文件夹目录,以com.bilibili.azurlane开头, 默认为com.bilibili.azurlane\\files\\AssetBundles")
        p.add_argument('-w','--works',default=os.cpu_count(), help="max works to handdle files, default full os.cpu_count()\n 处理解包的最大进程数,默认跑满CPU")
        self.args = p.parse_args(args)

if __name__ == '__main__':

    # ass = ['-f', 'x', '-d', 'com.bilibili.azurlane']
    ass = sys.argv[1:]
    # if not ass:
    #     ass = ['-h']
    app = AzurlaneUnpackControl(ass)
    app.clearEtcPackTmp()
    # app.run()

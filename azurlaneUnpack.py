#!/usr/bin/env python3
import os, sys
from PIL import Image, ImageOps
import io
import subprocess
import pickle
from argparse import ArgumentParser

import unitypack
from unitypack.asset import Asset
from unitypack.export import OBJMesh
from unitypack.utils import extract_audioclip_samples
from unitypack.engine.texture import TextureFormat

from pieceTex import az_paint_restore
from timeprint import timeWrite as print

CWD = os.path.dirname(os.path.abspath(__file__))

QUALITY = 80

ETCPACK_CMD = os.path.join(CWD, 'etcpack_linux')
if sys.platform == "darwin":
    ETCPACK_CMD = os.path.join(CWD, 'etcpack_macos')
if sys.platform == "win32":
    ETCPACK_CMD = os.path.join(CWD, 'etcpack.exe')

ETC_SERIES = [TextureFormat.ETC_RGB4, TextureFormat.ETC2_RGB, TextureFormat.ETC2_RGBA8,
              TextureFormat.ETC2_RGBA1, TextureFormat.EAC_R, TextureFormat.EAC_RG,
              TextureFormat.EAC_R_SIGNED, TextureFormat.EAC_RG_SIGNED]

TMP_PPM_FNAME_0 = 'tmp.ppm'
TMP_PKM_FNAME_0 = 'tmp.pkm'
TMP_PPM_FNAME = 'tmp.ppm'


class Azure_unpack:
    @classmethod
    def list_all_files(cls, rootdir):
        _files = []
        list = os.listdir(rootdir)
        for i in range(0, len(list)):
            path = os.path.join(rootdir, list[i])
            if os.path.isdir(path):
                _files.extend(cls.list_all_files(path))
            if os.path.isfile(path):
                _files.append(path)
        return _files

    @staticmethod
    def get_pkm_header(width, height, tformat):
        header = b"\x50\x4B\x4D\x20"
        version = b"20"
        if tformat == TextureFormat.ETC_RGB4:
            version = b"10"
            formatD = 0
        elif tformat == TextureFormat.ETC2_RGB:
            formatD = 1
        elif tformat == TextureFormat.ETC2_RGBA8:
            formatD = 3
        elif tformat == TextureFormat.ETC2_RGBA1:
            formatD = 4
        elif tformat == TextureFormat.EAC_R:
            formatD = 5
        elif tformat == TextureFormat.EAC_RG:
            formatD = 6
        elif tformat == TextureFormat.EAC_R_SIGNED:
            formatD = 7
        elif tformat == TextureFormat.EAC_RG_SIGNED:
            formatD = 8
        else:
            formatD = 0
        formatB = formatD.to_bytes(2, byteorder="big")
        widthB = width.to_bytes(2, byteorder="big")
        heightB = height.to_bytes(2, byteorder="big")
        return header + version + formatB + widthB + heightB + widthB + heightB

    @staticmethod
    def makeDirs(path: str):
        if not (os.path.exists(path)):
            os.makedirs(path)

    def __init__(self):
        self.allFiles = self.list_all_files("com.bilibili.azurlane\\files\\AssetBundles")
        self.outPath = os.path.join(CWD, "output")
        self.makeDirs(self.outPath)
        self.fileCount = self.allFiles.__len__()
        # self.maxWorks = 30

    def write_to_file(self, path, contents, mode="w"):
        dir, _ = os.path.split(path)
        self.makeDirs(dir)
        with open(path, mode) as f:
            f.write(contents)

    def unpackTexture(self, filePath):
        filePathPath, filePathFile = os.path.split(filePath)
        _, ifpainting = os.path.split(filePathPath)
        # print(ifpainting,filePathFile[-3:])
        if filePathFile[-3:] == "tex":
            needPintu = True
        else:
            needPintu = False
        savePath = os.path.join(self.outPath, filePath)
        self.makeDirs(savePath)
        with open(filePath, "rb") as f:
            bundle = unitypack.load(f)
            for asset in bundle.assets:
                needRemove = False
                # print("%s: %s:: %i objects" % (bundle, asset, len(asset.objects)))
                for id, object in asset.objects.items():
                    # Let's say we only want TextAsset objects
                    # print(object.type)
                    if (object.type == "Texture2D"):
                        d = object.read()
                        # print(d.name)
                        try:
                            if d.format in ETC_SERIES:
                                needRemove = True
                                TMP_PKM_FNAME = os.path.join(savePath, TMP_PKM_FNAME_0 + str(id))
                                bin_data = self.get_pkm_header(d.width, d.height, d.format) + d.image_data
                                with open(TMP_PKM_FNAME, 'wb') as f:
                                    f.write(bin_data)
                                cmd = ' '.join([ETCPACK_CMD, TMP_PKM_FNAME, TMP_PPM_FNAME, ">/dev/null 2>&1"])
                                if sys.platform == "win32":
                                    cmd = ' '.join([ETCPACK_CMD, TMP_PKM_FNAME, TMP_PPM_FNAME])
                                ret = subprocess.check_output(cmd, shell=True)
                                img = Image.open(TMP_PPM_FNAME)
                                # img.show()
                            else:
                                try:
                                    img = d.image
                                except Exception as e:
                                    print(filePath, str(e))
                                    continue
                        except:
                            try:
                                img = d.image
                            except Exception as e:
                                print(filePath, str(e))
                                continue
                        if (img.mode not in ('RGBA', 'LA')):
                            saveFileName = f"{d.name}.jpeg"
                            savePathFile = os.path.join(savePath, saveFileName)
                            img = ImageOps.flip(img)

                            img.save(savePathFile, "JPEG", quality=QUALITY, optimize=True, progressive=True)
                            if needPintu:
                                pintuImgPath = savePathFile
                        else:
                            saveFileName = f"{d.name}.png"
                            savePathFile = os.path.join(savePath, saveFileName)
                            img = ImageOps.flip(img)
                            img.save(savePathFile, "PNG")
                            if needPintu:
                                pintuImgPath = savePathFile
                        continue
                    elif object.type == "Mesh":
                        d = object.read()
                        try:
                            mesh_data = OBJMesh(d).export()
                            savePathFile = os.path.join(savePath, d.name)
                            savePathFile = savePathFile + ".obj"
                            self.write_to_file(savePathFile, mesh_data, mode="w")
                        except NotImplementedError as e:
                            print("WARNING: Could not extract %r (%s)" % (d, e))
                            mesh_data = pickle.dumps(d._obj)
                            savePathFile = os.path.join(savePath, d.name)
                            savePathFile = savePathFile + ".Mesh.pickle"
                            self.write_to_file(savePathFile, mesh_data, mode="wb")
                        if needPintu:
                            pintuMeshPath = savePathFile
                if needRemove:
                    try:
                        os.remove(TMP_PKM_FNAME)
                        os.remove(TMP_PPM_FNAME)
                    except:
                        pass
        if needPintu:
            pinPic = az_paint_restore(pintuMeshPath, pintuImgPath)
            pintuImgSavePath = ".".join(pintuImgPath.split(".")[:-1]) + ".png"
            pinPic.save(pintuImgSavePath, "PNG")

    def unpackTextureAll(self):
        handdled, errs = 0, []
        for f in self.allFiles:
            try:
                self.unpackTexture(f)
            except:
                errs.append(f)
            handdled += 1
            print(f"{handdled}/{self.fileCount} handdled")
        print(errs)
        # with futures.ThreadPoolExecutor(self.maxWorks) as exe:
        #     res = exe.map(self.unpackTexture,self.allFiles)
azure_unpack = Azure_unpack()

if __name__ == '__main__':
    azure_unpack.unpackTextureAll()

import os, sys
import subprocess

def decrypt(data, path):
    if (data[0:7] == b"UnityFS"):
        return data
    else:
        TMP_MUAST_FNAME = 'tmp.muast'
        TMP_UNITY_FNAME = 'tmp.muast.unity3d'
        CWD = os.path.dirname(os.path.abspath(__file__))
        DECRYPT_CMD = os.path.join(CWD, 'decryptor.exe')
        with open(TMP_MUAST_FNAME, 'wb') as f:
            f.write(data)
        cmd = ' '.join(["mono", DECRYPT_CMD, TMP_MUAST_FNAME, TMP_UNITY_FNAME])
        ret = subprocess.check_output(cmd, shell=True)
        print(ret)
        with open(TMP_UNITY_FNAME, 'rb') as f:
            data = f.read()
        try:
            os.remove(TMP_MUAST_FNAME)
        except:
            pass
        try:
            os.remove(TMP_UNITY_FNAME)
        except:
            pass
        return data
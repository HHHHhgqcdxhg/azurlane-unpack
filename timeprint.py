import datetime
oriWrite = print

def timeWrite(*args):
    datetimeString = "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]"
    oriWrite(datetimeString,*args)

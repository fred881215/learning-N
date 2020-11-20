
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
"""
from datetime import time,datetime
import os.path

"""
return list
"""
FilePath = "/home/nick/pi/log/"


def main():
    return get(timeNow, secNow, fileName, choose="")

def get(timeNow=None, secNow=None, fileName=None, choose="pub"):
    global FilePath
    showLog = []
    if timeNow == None or secNow == None:
        # timeNow = time.strftime("%Y-%m-%d")
        # secNow = int(time.time())
        # timesec = str(timeNow)+str(secNow)
        timesec = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        showLog.append(timesec)
        # print(timesec)
    return showLog

if __name__ == "__main__":
    ans = main()
    print(ans)

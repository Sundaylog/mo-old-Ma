from ctypes import *
import os
import time
import datetime
from PIL import Image
import win32gui
import win32con
import win32clipboard as w
m=0
d=0
while True:
    moment=datetime.datetime.now()
    moment=str(moment)
    day,tim=moment.split(" ")
    year,mon,date=day.split("-")
    mon=str(mon)
    m=int(mon)
    date=str(date)
    d=int(date)
    hour,minute,second=tim.split(":")
    hour=int(hour)
    minute=int(minute)
    second=int(float(second))
    if hour == 15 and minute == 51 and second == 10:
        m=str(m)
        d=str(d)
        name=m+"-"+d+".jpg"
        im=Image.open(name)
        im.save("temp.bmp")
        aString = windll.user32.LoadImageW(0,r"temp.bmp",win32con.IMAGE_BITMAP,0,0,win32con.LR_LOADFROMFILE)
        print(aString)
        if aString != 0:
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_BITMAP,aString)
            w.CloseClipboard()
        to_who = '老马夸夸群'
        # 获取qq窗口句柄
        qq = win32gui.FindWindow(None, to_who)
        # 投递剪贴板消息到QQ窗体
        win32gui.SendMessage(qq, 258, 22, 2080193)
        win32gui.SendMessage(qq, 770, 0, 0)
        # 模拟按下回车键
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        time.sleep(1)

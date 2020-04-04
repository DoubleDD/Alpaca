#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import time


#判断是否有手机连接
result = os.popen('adb devices -l')
textArr = result.readlines()
if len(textArr) == 2:
    os._exit(0)

print('开始处理截图')
#获得当前时间时间戳 
now = int(time.time())

#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S" 
timeStruct = time.localtime(now)
strTime = time.strftime("%Y-%m-%d_%H-%M-%S", timeStruct)

print(strTime)
fileName=f'{strTime}.jpg'
path = f'/home/kedong/Pictures/weixin/{fileName}'
cmd = f'deepin-screenshot -s {path}'
print(path)

os.system(cmd)
print('截图中...')

os.system('wait $!')


# 判断是否截图成功
if not os.path.exists(path):
    print('截图取消')
    os._exit(0)

print('截图完成')
print('显示图片')
#os.system(f'feh {path}')

print('将图片发送到手机')
os.system(f'adb push {path} /sdcard/tencent/MicroMsg/WeiXin')
os.system(f'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/tencent/MicroMsg/WeiXin/{fileName}')

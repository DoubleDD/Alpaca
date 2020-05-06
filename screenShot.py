#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import time


print('开始处理截图')
#获得当前时间时间戳 
now = int(time.time())

#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S" 
timeStruct = time.localtime(now)
strTime = time.strftime("%Y-%m-%d_%H-%M-%S", timeStruct)

print(strTime)
fileName=f'{strTime}.jpg'
deepinPath = '/home/kedong/Pictures/deepin'
if not os.path.exists(deepinPath):
    print('创建目录')
    os.makedirs(deepinPath)
path = f'/home/kedong/Pictures/deepin/{fileName}'
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

# -*- coding = utf-8 -*-
# @Time : 2021/5/5 17:16
# @Author : 水神与月神
# @File : 灰度转彩色.py
# @Software : PyCharm

from PIL import Image

path = r'C:\Users\dell\Desktop\20210501spectrograph.gif'
path2 = r'C:\Users\dell\Desktop\20210501spectrograph.png'

from PIL import Image, ImageSequence

im = Image.open(path)  # 使用Image的open函数打开test.gif图像

index = 1
for frame in ImageSequence.Iterator(im):  # for循环迭代的取im里的帧
    frame.save(path2)  # 取到一个帧调用一下save函数保存，每次保存明明为frameX.png
    index += 1  # 序号依次叠加






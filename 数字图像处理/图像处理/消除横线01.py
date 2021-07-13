# -*- coding = utf-8 -*-
# @Time : 2021/4/10 9:33
# @Author : 水神与月神
# @File : 消除横线01.py
# @Software : PyCharm


import cv2 as cv
import numpy as np
import mypackage.dip_function as df
import mypackage.dip_class as dc

path = r"G:\LearmonthData\New\II\LM200106120714_II_28_180.jpg"
img = cv.imread(path, cv.IMREAD_UNCHANGED)

img2 = df.normal(img)
img3 = df.amplitude_filter(img2, 20)
img4 = cv.adaptiveThreshold(img3, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 0)
img5 = dc.EraseLine(img4, 100).erase_line_mean()
img6 = dc.EraseLine(img4, 100).erase_line_gaussian()
img7 = dc.EraseLine(img, 100).erase_line_gaussian()
img8 = df.normal(img7)
img9 = df.amplitude_filter(img8, 20)
img10 = cv.adaptiveThreshold(img9, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 0)
images = np.hstack([img, img7, img8, img9, img10])
print(type(images))
df.cv_show(images)


"""
方法1：消除横线-->通道归一化-->幅值滤波-->自适应二值化，结果还不错
问题：底部噪声处，存在需要的数据，怎么处理
如果横线噪声上下两行差距非常大，不能用取均值的方法处理，要想办法平滑过渡
方块噪声怎么处理
"""



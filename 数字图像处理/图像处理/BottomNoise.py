# -*- coding = utf-8 -*-
# @Time : 2021/4/9 22:13
# @Author : 水神与月神
# @File : BottomNoise.py
# @Software : PyCharm


import cv2 as cv
import numpy as np
import mypackage.dip_function as df

read_path = r"G:\LearmonthData\New\II\LM200109192335_II_36_68.jpg"
image = cv.imread(read_path, cv.IMREAD_UNCHANGED)
ret, img2 = cv.threshold(image, 60, 255, cv.THRESH_BINARY)
imgs = np.hstack([image, img2])
df.cv_show(imgs, "img")




# -*- coding = utf-8 -*-
# @Time : 2021/3/6 16:53
# @Author : 水神与月神
# @File : test2.py
# @Software : PyCharm

import cv2 as cv
import numpy as np
import mypackage.dip_function as df
import mypackage.dip_class as dc

path = r"G:\LearmonthData\New\II\LM200103262256_II_46_75.jpg"
img = cv.imread(path, cv.IMREAD_UNCHANGED)
img2 = df.normal(img)
img3 = df.amplitude_filter(img2, 20)
img4 = cv.adaptiveThreshold(img3, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 0)
img5 = dc.EraseLine(img4, 100).erase_line_mean()
img6 = dc.EraseLine(img4, 100).erase_line_gaussian()
images = np.hstack([img, img2, img3, img4, img5, img6])
print(type(images))
df.cv_show(images)





# a = np.random.randint(0, 255, (200, 200))
# a = a.astype(np.uint8)
# print(type(a))
# print(a.shape)
# df.cv_show(a, "ff")
# -*- coding = utf-8 -*-
# @Time : 2021/3/14 17:28
# @Author : 水神与月神
# @File : 背景消除.py
# @Software : PyCharm


import cv2 as cv
import numpy as np
import mypackage.dip_function as df
import mypackage.dip_class as dc
import matplotlib.pyplot as plt


def count(img):
    row = img.shape[0]
    c = []
    for i in range(row):
        c.append(np.sum(img[i]))
    return c


# Parameters
blur = 21
canny_low = 10  # 灵敏度
canny_high = 50  # 阈值

read_path = r"G:\LearmonthData\New\II\LM200109192335_II_36_68.jpg"
image = cv.imread(read_path, cv.IMREAD_UNCHANGED)

gray_img_1 = dc.EraseLine(image, 100).erase_line_gaussian()
gray_normal = df.normal(gray_img_1)

edges1 = cv.Canny(gray_img_1, canny_low, canny_high)
edges2 = cv.Canny(gray_normal, canny_low, canny_high)

oc = count(edges2)

edges3 = dc.EraseLine(edges2, 100, rate=0.6, row_rate=1).erase_line_zero()

plt.plot(oc)
images = np.hstack([image, gray_img_1, edges1, edges2, edges3])
cv.imshow("edges", images)
cv.waitKey()
cv.destroyWindow("edges")




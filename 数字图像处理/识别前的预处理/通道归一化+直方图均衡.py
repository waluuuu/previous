# -*- coding = utf-8 -*-
# @Time : 2021/4/19 19:43
# @Author : 水神与月神
# @File : 通道归一化+直方图均衡.py
# @Software : PyCharm


import mypackage.dip_function as df
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

# 小试牛刀
# path = r"G:\useful\2\CG199711030433_FN,H_30_130.jpg.jpg"
# path = r"G:\useful\2\CG199811062332_FN_30_50.jpg.jpg"
#
# image = cv.imread(path, cv.IMREAD_UNCHANGED)
# image2 = df.normal(image)
# image3 = df.amplitude_filter(image2, 23)
# image4 = cv.equalizeHist(image3)
# kernel_2_2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2), (-1, -1))
#
# dst = cv.erode(image4, kernel_2_2)  # 水平方向
# images = np.hstack([image, image2, image3, image4, dst])
#
# df.cv_show(images)

# path = r"G:\useful\3\LM200102110853_III_30_90.jpg"
#
# image = cv.imread(path, cv.IMREAD_UNCHANGED)
# image2 = df.normal(image)
# image3 = cv.equalizeHist(image2)
# # image4 = df.amplitude_filter(image3,20)
# images = np.hstack([image, image2, image3])
# plt.hist(image2.ravel(),256,[0,256])
# plt.show()
# df.cv_show(images)

# 批量处理

path_read_2 = r"G:\useful\2"
path_read_3 = r"G:\useful\3"
path_read_4 = r"G:\useful\4"
path_read_n = r"G:\useful\noburst"

path_save_2 = r"G:\useful\processed\2"
path_save_3 = r"G:\useful\processed\3"
path_save_4 = r"G:\useful\processed\4"
path_save_n = r"G:\useful\processed\noburst"

path_2 = df.get_path(path_read_2, path_save_2)
path_3 = df.get_path(path_read_3, path_save_3)
path_4 = df.get_path(path_read_4, path_save_4)
path_n = df.get_path(path_read_n, path_save_n)

# for path in path_2:
#     image = cv.imread(path[0], cv.IMREAD_UNCHANGED)
#     image2 = df.normal(image)
#     # image3 = df.amplitude_filter(image2, 20)
#     image4 = cv.equalizeHist(image2)
#     cv.imwrite(path[1], image4)
#
# print("二型爆处理完成")
#
# for path in path_3:
#     try:
#         image = cv.imread(path[0], cv.IMREAD_UNCHANGED)
#         image2 = df.normal(image)
#         # image3 = df.amplitude_filter(image2, 20)
#         image4 = cv.equalizeHist(image2)
#         cv.imwrite(path[1], image4)
#     except AttributeError:
#         print(path)
#
# print("三型爆处理完成")
#
# for path in path_n:
#     image = cv.imread(path[0], cv.IMREAD_UNCHANGED)
#     image2 = df.normal(image)
#     # image3 = df.amplitude_filter(image2, 20)
#     image4 = cv.equalizeHist(image2)
#     cv.imwrite(path[1], image4)
#
# print("全部处理完成")


for path in path_4:
    image = cv.imread(path[0], cv.IMREAD_UNCHANGED)
    image2 = df.normal(image)
    # image3 = df.amplitude_filter(image2, 20)
    image4 = cv.equalizeHist(image2)
    cv.imwrite(path[1], image4)
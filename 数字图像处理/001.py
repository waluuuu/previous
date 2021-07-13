# -*- coding = utf-8 -*-
# @Time : 2021/5/5 21:59
# @Author : 水神与月神
# @File : 001.py
# @Software : PyCharm

import cv2 as cv
import numpy as np

path = r"G:\09.png"
image = cv.imread(path, cv.IMREAD_UNCHANGED)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# gray2 = cv.equalizeHist(gray)
c = cv.applyColorMap(gray, cv.COLORMAP_JET)

# opencv b g r 色域


r = c[:, :, 2]
shaper = r.shape

for i in range(shaper[0]):
    for j in range(shaper[1]):
        if r[i][j] - 150 < 0:
            r[i][j] = 70
        else:
            r[i][j] = r[i][j] - 150

temp = r
c[:, :, 2] = temp

g = c[:, :, 1]
shapeg = g.shape

for i in range(shapeg[0]):
    if i <200:
        for j in range(shapeg[1]):
            if g[i][j] - 100 < 70:
                g[i][j] = 70
            else:
                g[i][j] = g[i][j] - 100
    else:
        for j in range(shapeg[1]):
            if g[i][j] > 160:
                g[i][j] = 160
            # elif g[i][j] < 70:
            #     g[i][j] = 70

temp = g
c[:, :, 1] = temp





# b = c[:, :, 0]
# shapeb = b.shape
#
# for i in range(shapeg[0]):
#     if i <200:
#         for j in range(shapeg[1]):
#             if b[i][j] - 100 < 70:
#                 b[i][j] = 70
#             else:
#                 b[i][j] = b[i][j] - 100
#     else:
#         for j in range(shapeg[1]):
#             if b[i][j] + 100 > 160:
#                 b[i][j] = 160
#             else:
#                 b[i][j] = b[i][j] + 100
#
# temp = b
# c[:, :, 0] = temp






cv.imshow('fff', c)
cv.waitKey(0)
cv.destroyWindow('fff')

# rnum = 250 - 70
# reach = rnum / 255
# r = []
# for i in range(0, 256):
#     r.append(int(70 + reach * i))
#
# gnum = 156 - 70
# geach = gnum / 255
# g = []
# for i in range(0, 256):
#     g.append(int(70 + geach * i))
#
# bnum = 183 - 127
# beach = bnum / 255
# b = []
# for i in range(0, 256):
#     b.append(int(183 - beach * i))
#
#
# all = []
#
# for i in range(256):
#     temp = []
#     temp.append(b[i])
#     temp.append(g[i])
#     temp.append(r[i])
#
#     all.append(temp)
#
#
# all = np.array(all).astype(np.uint8)
#
#
#
#
# path = r"G:\09.png"
#
# image = cv.imread(path, cv.IMREAD_UNCHANGED)
#
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#
# ishape = gray.shape
# a = np.zeros(shape=ishape)
# a = a.tolist()
#
# gray = cv.bitwise_not(gray)
#
#
# for i in range(ishape[0]):
#     for j in range(ishape[1]):
#         a[i][j] = all[gray[i][j]]
#
# im_color = cv.applyColorMap(gray, cv.COLORMAP_RAINBOW)
#
#
# # COLORMAP_SUMMER
# # COLORMAP_RAINBOW
# # COLORMAP_PARULA
#
# a = np.array(a).astype(np.uint8)
# cv.imshow("images", a)
# cv.waitKey()
# cv.destroyWindow('images')

# 天蓝色的RGB为：87,250,255

# 橘红色 RGB：237,111,0


# <p style="background-color:rgba(70,70,183,1)">
# <p style="background-color:rgba(250,156,127,1)">

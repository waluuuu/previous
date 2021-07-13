# -*- coding = utf-8 -*-
# @Time : 2021/5/5 18:25
# @Author : 水神与月神
# @File : 灰度转彩色.py
# @Software : PyCharm


import cv2 as cv
import numpy as np
import os
import mypackage.dip_function as df

# demo
# path = r"C:\Users\dell\Desktop\8.png"
#
# image = cv.imread(path, cv.IMREAD_UNCHANGED)
#
# image1 = image[:, :, 0]
# image2 = image[:, :, 1]
# image3 = image[:, :, 2]
#
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# gray2 = cv.bitwise_not(gray)
# image4 = image3 - image2
# im_color = cv.applyColorMap(gray2, cv.COLORMAP_PARULA)
# # COLORMAP_SUMMER
# # COLORMAP_RAINBOW
# # COLORMAP_PARULA
# cv.imshow("images", im_color)
# cv.waitKey()
# cv.destroyWindow('images')

path = r'G:\colour_img'
save = r'G:\colour_img\processed'

folders = os.listdir(path)

for folder in folders[0:-1]:
    path_read = os.path.join(path, folder)
    path_save = os.path.join(save, folder)
    paths = df.get_path(path_read, path_save)
    for p in paths:
        image = cv.imread(p[0], cv.IMREAD_UNCHANGED)
        gray = cv.equalizeHist(image)
        colour = cv.applyColorMap(gray, cv.COLORMAP_JET)

        r = colour[:, :, 2]
        shaper = r.shape
        for i in range(shaper[0]):
            for j in range(shaper[1]):
                if r[i][j] - 150 < 0:
                    r[i][j] = 70
                else:
                    r[i][j] = r[i][j] - 150

        temp = r
        colour[:, :, 2] = temp

        g = colour[:, :, 1]
        shapeg = g.shape

        for i in range(shapeg[0]):
            if i < 600:
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
        colour[:, :, 1] = temp

        cv.imwrite(p[1], colour)
        print("保存成功")



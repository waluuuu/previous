# -*- coding = utf-8 -*-
# @Time : 2021/4/18 9:30
# @Author : 水神与月神
# @File : GetCalibrationImages.py
# @Software : PyCharm


import mypackage.dip_function as df
import cv2 as cv
import numpy as np

path_read = r"G:\hrpdata\NoBurst\LM0801010.png"
# path_save = r""
# paths = df.get_path(path_read, path_save)
# for path in paths:

image = cv.imread(path_read, cv.IMREAD_UNCHANGED)
# image2 = df.normal(image)
# image3 = cv.threshold(image2, 40, 255, cv.THRESH_BINARY)
# images = np.hstack([image, image2, image3])
df.cv_show(image)

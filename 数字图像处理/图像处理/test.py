# -*- coding = utf-8 -*-
# @Time : 2021/3/5 20:55
# @Author : 水神与月神
# @File : test.py
# @Software : PyCharm

import cv2 as cv
import numpy as np
import mypackage.dip_function as df
import matplotlib.pyplot as plt

path = r"G:\LearmonthData\New\II\LM201311052210_II_25_180.jpg"
img = cv.imread(path, cv.IMREAD_UNCHANGED)
img2 = df.normal(img)
# flatten() 将数组变成一维
hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
"""
histogram统计数据中处于各个区间的个数
histogram(a,bins=10,range=None,weights=None,density=False);

a是待统计数据的数组；
bins指定统计的区间个数；
range是一个长度为2的元组，表示统计范围的最小值和最大值，默认值None，表示范围由数据的范围决定
weights为数组的每个元素指定了权值,histogram()会对区间中数组所对应的权值进行求和
density为True时，返回每个区间的概率密度；为False，返回每个区间中元素的个数

所以，本次使用的为256个区间，最大值为255，最小值为0
参考链接：https://blog.csdn.net/yangwangnndd/article/details/89489946
"""

# 计算累积分布图
cdf = hist.cumsum()
"""
计算累加的值：
array([1,2,3,4,5,6,7,8,9])
计算之后
array([ 1,  3,  6, 10, 15, 21, 28, 36, 45]
参考链接：https://blog.csdn.net/qq_32572085/article/details/85092710
"""

cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

cv.imshow('test', img2)
cv.waitKey(0)
cv.destroyWindow('test')





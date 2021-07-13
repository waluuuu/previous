# -*- coding = utf-8 -*-
# @Time : 2021/5/14 16:01
# @Author : 水神与月神
# @File : 分割彩色图片.py
# @Software : PyCharm

# %%
import cv2 as cv
import numpy as np
import PIL

# def cv_imread(file_path):
#     """可读取图片（路径为中文）
#
#     :param file_path: 图片路径
#     :return:
#     """
#     # 可以使用中文路径读取图片
#     cv_img = cv.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
#     return cv_img
#
#
# path = r'G:\images_culgoora\1995\8\1995.08.17.jpg'
# image = cv_imread(path)
# print(image.shape)
# print('-------------------------------------')

# %%
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageSequence

path = r'G:\images_culgoora\1995\8\1995.08.25.gif'
img = Image.open(path)
i = 0
for frame in ImageSequence.Iterator(img):
    frame.save("G://frame%d.png" % i)
    i += 1

# %%
import cv2 as cv

path = r'G:\frame0.png'
image = cv.imread(path)
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyWindow('image')

# %%


# import cv2
# import numpy as np
#
# image = cv2.imread(r'G:\useful_L\2\CG199503130651_FN_30_70.jpg.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# original = cv2.imread(r'C:\Users\dell\Desktop\color.png')
# original = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
#
#
# def getavgstd(image):
#     avg = []
#     std = []
#     image_avg_l = np.mean(image[:, :, 0])
#     image_std_l = np.std(image[:, :, 0])
#     image_avg_a = np.mean(image[:, :, 1])
#     image_std_a = np.std(image[:, :, 1])
#     image_avg_b = np.mean(image[:, :, 2])
#     image_std_b = np.std(image[:, :, 2])
#     avg.append(image_avg_l)
#     avg.append(image_avg_a)
#     avg.append(image_avg_b)
#     std.append(image_std_l)
#     std.append(image_std_a)
#     std.append(image_std_b)
#     return (avg, std)
#
#
# image_avg, image_std = getavgstd(image)
# original_avg, original_std = getavgstd(original)
#
# height, width, channel = image.shape
# for i in range(0, height):
#     for j in range(0, width):
#         for k in range(0, channel):
#             t = image[i, j, k]
#             t = (t - image_avg[k]) * (original_std[k] / image_std[k]) + original_avg[k]
#             t = 0 if t < 0 else t
#             t = 255 if t > 255 else t
#             image[i, j, k] = t
# image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)
# cv2.imwrite('G://out.jpg', image)


# %%


# USAGE
# python example.py --source images/01.jpg --target images/02.jpg -o images/01_02.jpg


import cv2
# 导入必要的类
from color_transfer import color_transfer


def show_image(title, image, width=300):
    # resize图像以使得图像具有固定的大小，以便整个屏幕都可以展示
    r = width / float(image.shape[1])
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # 展示缩放后的图像
    cv2.imshow(title, resized)


path1 = r'C:\Users\dell\Desktop\888.png'
path2 = r'G:\useful_C\I\CG200006190000_I_120_180.jpg'
save = r'C:\Users\dell\Desktop\1.png'

# 加载图像
source = cv2.imread(path1)
target = cv2.imread(path2)

# 转移源图像的色彩分配 到 目标图像
transfer = color_transfer(source, target)



# r = transfer[:, :, 2]
#g = transfer[:, :, 1]

# r = cv2.equalizeHist(r)
#g = cv2.equalizeHist(g)

# transfer[:, :, 2] = r
#transfer[:, :, 1] = g
# 检测是否保存输出图像

cv2.imwrite(save, transfer)

# 展示图像
show_image("Source", source)
show_image("Target", target)
show_image("Transfer", transfer)
cv2.waitKey(0)
cv2.destroyAllWindows()




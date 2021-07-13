# -*- coding = utf-8 -*-
# @Time : 2021/2/2 15:45
# @Author : 水神与月神
# @File : DIP.py
# @Software : PyCharm


# %%

import cv2 as cv

import mypackage.dip_function as df
import mypackage.dip_class as dc
""""
用消除横线噪声的第一种方法
批量处理和保存图片
得到文件夹中所有图片的绝对路径
"""

"""
2021.4.10
加上了幅值滤波，自适应二值化原始1参数为9，-2
"""


def batch_process(read_path, save_path):
    file_names = df.get_path(read_path, save_path)
    count = 0
    for file_name in file_names:
        img = cv.imread(file_name[0], cv.IMREAD_UNCHANGED)
        gray_img_1 = dc.EraseLine(img, 150).erase_line_gaussian()
        gray_normal = df.normal(gray_img_1)
        binary_img_3 = df.amplitude_filter(gray_normal, 20)
        binary_img_2 = cv.adaptiveThreshold(binary_img_3, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)
        d

        cv.imwrite(file_name[1], dst4)
        print(count)
        count += 1


if __name__ == "__main__":
    read_path = r"G:\LearmonthData\New\III"
    save_path = r"G:\LearmonthData\test\III"
    batch_process(read_path, save_path)

# if __name__ == "__main__":
#     # path = r"G:\LearmonthData\New\III\LM200103240707_III_25_169.jpg"
#     # path = r"G:\LearmonthData\New\III\LM200103280021_III_25_180.jpg"
#     # path = r"G:\LearmonthData\New\III\LM200103242307_III_31_151.jpg"
#     # path = r"G:\LearmonthData\New\III\LM200104010144_III_25_56.jpg"
#     path = r"G:\LearmonthData\New\III\LM200104180211_III_25_180.jpg"
#     gray_img = cv.imread(path, cv.IMREAD_UNCHANGED)
#     b = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)
#     gray_img_1 = dc.dc(path, 150).erase_line_gaussian()
#     binary_img_1 = cv.adaptiveThreshold(gray_img_1, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)
#     gray_normal = df.normal(gray_img_1)
#     binary_img_2 = cv.adaptiveThreshold(gray_normal, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)
#     """
#     numpy.hstack:沿着水平方向，将数组堆叠起来
#     """
#
#     # 开始尝试腐蚀和膨胀
#     kernel_1_6 = cv.getStructuringElement(cv.MORPH_RECT, (1, 20), (-1, -1))
#     kernel_1_4 = cv.getStructuringElement(cv.MORPH_RECT, (1, 4), (-1, -1))
#     kernel_1_3 = cv.getStructuringElement(cv.MORPH_RECT, (1, 3), (-1, -1))
#
#     kernel_3_20 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 20), (-1, -1))
#
#     dst = cv.erode(binary_img_2, kernel_1_6)  # 水平方向
#     dst4 = cv.dilate(dst, kernel_3_20)  # 水平方向
#
#     images = np.hstack([gray_img, b, gray_img_1, gray_normal, binary_img_1, binary_img_2, dst, dst4])
#     df.cv_show(images, "test")

# %%
# img = cv.imread(path, cv.IMREAD_UNCHANGED)
# # 直方图均衡
# equ = cv.equalizeHist(img)
# # 像素取反
# # gray_src = cv.bitwise_not(img)
# med = cv.medianBlur(img, 7)
# # equ2 = cv.equalizeHist(med)
# # 绘制灰度直方图
# # plt.hist(img.flatten(), 256, [0, 256])
# # plt.figure()
# # plt.hist(equ.flatten(), 256, [0, 256])
# # plt.figure()
# # a, new = cv.threshold(equ, 200, 255, cv.THRESH_BINARY)
# # plt.hist(new.flatten(), 256, [0, 256])
# # plt.show()
# binary_src = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)


"""
收获：
1.如果路径不对，会报错，但是不显示路径有问题
2.cv.bitwise_not对数值进行取反，150取反->105（255最大）
3.ravel返回图片展开的数组，改变返回值，原来的图片也会改变
4.flatten和ravel功能一样，但是，改变返回值，原来的值不会改变
"""

"""
现在需要：
1.如果灰度小于某一个值，就让它归零，这样可以减少一些消除横线噪声所带来的影响
2.消除横线噪声的过程中，新的像素要符合高斯分布
3.需要看到图像的直方图，了解到，背景大概是一个什么灰度范围
4.腐蚀和膨胀的参数需要进一步选择
"""

"""
2021.3.5
在原始图像上进行归一化，然后统计背景像素大概在哪个范围之内
然后，对图像进行幅值滤波，小于某个值的，都设置为0
有可能导致强度比较小的爆发被消去

"""

kernel = 1



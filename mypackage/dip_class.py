# -*- coding = utf-8 -*-
# @Time : 2021/4/11 15:21
# @Author : 水神与月神
# @File : MyDIPClass.py
# @Software : PyCharm


import cv2 as cv
import os
import numpy as np
import mypackage.dip_function as df

"""
类的私有变量和属性：
单下划线开头，自己和子类可以引用
双下划线开头，只能自己引用
参考链接：https://www.cnblogs.com/lijunjiang2015/p/7802410.html
"""


class EraseLine:
    """
    消除横线噪声
    流程：
    读取图片，自适应二值化处理，得到哪些行是要处理的
    开始的时候得到的是一些行数，要找到这些行数哪些是连续的，把连续的存储到一个数组里面
    如果离得特别近，在消除噪声的时候，进行合并处理
    用高斯噪声进行填充
    """

    def __init__(self, img, length, rate=0.85, row_rate=7 / 8):
        """
        初始化，存放相关的常量
        :param img: 图片
        :param length: 横向的长度
        :param rate: 横线中全白的比例
        :param row_rate: 在
        """
        self.length = length
        self.rate = rate
        self.row_rate = row_rate
        self.gray_img = img.copy()
        self.gray_img2 = self.gray_img.copy()
        self.binary_img = cv.adaptiveThreshold(self.gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, -2)

        self.row = self.binary_img.shape[0]
        self.column = self.binary_img.shape[1]
        """
        np.adaptiveThreshold函数用法：
        把图片每个像素点作为中心取 N*N 的区域，然后计算这个区域的阈值，来决定这个像素点变0还是变255
        第三个参数：ADAPTIVE_THRESH_MEAN_C为求均值，ADAPTIVE_THRESH_GAUSSIAN_C为高斯加权求和
        第四个参数：
        第五个参数：N的大小
        第六个参数：每个邻域计算出阈值后再减去C作为最终阈值
        参考链接：https://blog.csdn.net/laoyezha/article/details/106445437
        """

    def get_line(self):
        """
        检测横线
        设计思路：给定一个长度，通过kernel检测横线是否大于预设的长度
        :return:
        """
        rows = []  # 存储需要处理的行
        kernel = np.ones((1, self.length))  # 核

        for i in range(int(self.row * self.row_rate)):

            for j in range(0, self.column - self.length + 1):
                temp = self.binary_img[i][j:j + self.length]  # 列表切片，左闭右开
                result = temp * kernel
                """
                numpy中，用*表示矩阵对应相乘
                dot表示正常的矩阵乘法：np.dot(A,B) or A.dot(B)
                nu.array可以和列表相乘，但是，两个列表不能直接相乘
                """
                num = np.sum(result == 255)
                if num >= self.length * self.rate:
                    rows.append(i)
                    break
        return rows

    def get_continue_num(self):
        """
        检测列表中连续的数字
        :return:
        """
        rows = self.get_line()
        s = 1
        start = 0

        find_list = []
        while s < len(rows):

            if rows[s] - rows[s - 1] == 1:
                while rows[s] - rows[s - 1] == 1:
                    s += 1
                    if s >= len(rows):
                        break
                find_list.append(rows[start:s])
                start = s
                s += 1

            else:
                find_list.append(rows[start:s])
                start = s
                s += 1
        # print(find_list)
        return find_list, self.list_dilate(find_list)

    def list_dilate(self, find_list):
        """
        列表膨胀，将相邻的非常近的横线合并
        :return:
        """
        length = len(find_list)
        new = [find_list[0]]
        for i in range(1, length):
            if find_list[i][0] - new[-1][-1] <= 12:
                temp = [x for x in range(new[-1][0], find_list[i][-1] + 1)]
                new.pop(-1)
                new.append(temp)
                """
                使用pop，按照索引删除元素
                使用remove，删除第一个要删除的数值
                使用del，根据索引删除元素del list[-1]，也可使用切片
                """
            else:
                new.append(find_list[i])
        return new

    def erase_line_mean(self):
        """
        按照均值填充，来消除横线噪声
        :return:
        """

        find_list = self.get_continue_num()[1]
        for i in find_list:
            # 判断行和列是否符合条件
            start_num = 0 if i[0] - 5 < 0 else i[0] - 5
            end_num = self.row if i[-1] + 5 > self.row else i[-1] + 5

            start_line = self.gray_img2[start_num].tolist()
            end_line = self.gray_img2[end_num].tolist()
            add_value = list(map(lambda x: x[0] + x[1], zip(start_line, end_line)))
            """
            zip函数用法：
            将两个列表中的对应元素放到一个元组里面，所有元组组成列表
            参考链接：https://www.runoob.com/python/python-func-zip.html
            """
            mean_value = [x // 2 for x in add_value]

            for j in range(start_num, end_num):
                self.gray_img2[j] = mean_value
        return self.gray_img2

        # print(find_list)

        # images = np.hstack([self.gray_img, self.gray_img2, self.binary_img])
        # cv.imshow('test', images)
        # cv.waitKey(0)
        # cv.destroyWindow('test')

    def erase_line_gaussian(self):
        """
        按照高斯分布来填充，消除横线噪声

        参考链接：https://www.cnblogs.com/wojianxin/p/12499928.html
        """
        find_list = self.get_continue_num()[1]
        for i in find_list:
            if i[0] < 400 and i[-1] > 400:
                continue
            # 判断行和列是否符合条件
            start_num = 0 if i[0] - 5 < 0 else i[0] - 5
            end_num = self.row if i[-1] + 5 > self.row else i[-1] + 5
            """
            上下取3个，求平均值
            """
            for j in range(self.column):
                count = int(self.gray_img2[start_num - 1][j]) + int(self.gray_img2[end_num + 1][j]) + \
                        int(self.gray_img2[start_num - 2][j]) + int(self.gray_img2[end_num + 2][j]) + \
                        int(self.gray_img2[start_num - 3][j]) + int(self.gray_img2[end_num + 3][j])
                mean = count // 6
                num = end_num - start_num
                list = df.my_Gaussian(mean, num + 1)
                for c in range(start_num, end_num + 1):
                    self.gray_img2[c][j] = list[c - start_num]

        return self.gray_img2

    def erase_line_zero(self):
        """
        将白线变成0
        :return:
        """
        find_list = self.get_continue_num()[0]
        for i in find_list:
            for j in range(self.column):
                for c in range(i[0], i[-1] + 1):
                    self.gray_img2[c][j] = 0
        return self.gray_img2


class ImageSegmentation:
    def __init__(self, path_read, path_save):
        self.path_read = path_read
        self.path_save = path_save
        self.image = cv.imread(self.path_read, cv.IMREAD_UNCHANGED)
        (path, self.filename) = os.path.split(self.path_read)
        if not os.path.exists(self.path_save):  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(self.path_save)

    def number(self, num):
        try:
            image = self.image.copy()
            row = self.image.shape[0]
            column = self.image.shape[1]
        except AttributeError:
            return None
        if num == 0:
            print("参数num不能为0")
            return None

        length = column // num
        for i in range(num - 1):
            temp = image[:, i * length:(i + 1) * length]
            path_save = os.path.join(self.path_save, self.filename.split(".")[0] + str(i) + ".png")
            if temp.size == 0:
                return None
            cv.imwrite(path_save, temp)
        temp = image[:, (num - 1) * length:]
        path_save = os.path.join(self.path_save, self.filename.split(".")[0] + str(num) + ".png")
        if temp.size == 0:
            return None
        cv.imwrite(path_save, temp)

    def size(self, size):
        try:
            image = self.image.copy()
            row = self.image.shape[0]
            column = self.image.shape[1]
        except AttributeError:
            return None
        if size > column:
            print("超出了图片的长度")
            return None

        num = column // size
        for i in range(num):
            temp = image[:, i * size:(i + 1) * size]
            path_save = os.path.join(self.path_save, self.filename.split(".")[0] + str(i) + ".png")
            if temp.size == 0:
                return None
            cv.imwrite(path_save, temp)

        # temp = image[:, num * size:]
        # path_save = os.path.join(self.path_save, self.filename.split(".")[0] + str(num) + ".png")
        # if temp.size == 0:
        #     return None
        # cv.imwrite(path_save, temp)


def test():
    """
    测试的时候，需要加上显示图片的语句
    :return:
    """
    # path = r"G:\LearmonthData\New\II\LM200103100408_II_25_130.jpg"
    # img = cv.imread(path, cv.IMREAD_UNCHANGED)
    # EraseLine(img, 200).erase_line_mean()

    path_read = r"G:\LearmonthData\learmonth_pics\03\LM030102.srs.png"
    path_save = r"G:\ceshi1"
    ImageSegmentation(path_read, path_save).size(1000)


if __name__ == '__main__':
    test()

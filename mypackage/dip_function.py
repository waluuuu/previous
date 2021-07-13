# -*- coding = utf-8 -*-
# @Time : 2021/4/11 15:11
# @Author : 水神与月神
# @File : MyDIPFunction.py
# @Software : PyCharm

import os
import cv2 as cv
import numpy as np
import openpyxl
import datetime


def amplitude_filter(gray_image, threshold):
    """
    幅值滤波，将小于阈值的像素置0
    :param gray_image: 灰度图片
    :param threshold: 阈值
    :return:返回处理之后的图片
    """

    gray_image = gray_image.copy()
    row = gray_image.shape[0]
    column = gray_image.shape[1]

    for i in range(row):
        for j in range(column):
            if gray_image[i][j] < threshold:
                gray_image[i][j] = 0
    return gray_image


def normal(gray_image):
    """
    通道归一化
    :param gray_image: 输入图片
    :return: 返回归一化之后的图片
    """

    binary_image = gray_image.copy()
    shape = binary_image.shape
    row = shape[0]

    # mean = binary_image.mean()
    # mean = 0
    for i in range(row):
        minimum = binary_image[i].min()
        binary_image[i] = binary_image[i] - minimum
    return binary_image


def half(read_path, save_path):
    """
    批量处理图片，只要图片的下半部分，之后可能会加上别的half方式
    :param read_path:读取图片的文件夹
    :param save_path:保存图片的文件夹
    :return:没有返回值，直接将处理好的图片，保存在想要的路径
    """
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    file_names = os.listdir(read_path)
    for file_name in file_names:
        path_read = os.path.join(read_path, file_name)
        path_save = os.path.join(save_path, file_name + '.jpg')
        f = cv.imread(path_read, cv.IMREAD_UNCHANGED)
        w = f[1002:, :]
        cv.imwrite(path_save, w)
    print("图片保存成功！")


def cv_show(images, name="img"):
    """
    显示图片，输入单张图片或者numpy.hstack([img, img2])拼接起来的图片
    :param images:图片，二维数组
    :param name: 窗口的名称
    :return:
    """
    cv.imshow(name, images)
    cv.waitKey(0)
    cv.destroyWindow(name)


def my_Gaussian(mean, size, fluctuation=2):
    """
    产生符合高斯分布的数组
    利用高斯分布的性质，”投机取巧“的产生想要的数组
    横轴区间（μ-σ,μ+σ）内的面积为68.268949%
    横轴区间（μ-2σ,μ+2σ）内的面积为95.449974%
    横轴区间（μ-3σ,μ+3σ）内的面积为99.730020%

    参考链接：百度百科 & https://blog.csdn.net/fjssharpsword/article/details/93157726?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=1328603.40007.16150789219018851&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control

    :param mean: 均值
    :param size: 数组大小
    :param fluctuation:均值上下的波动范围
    :return: 返回一个在均值附近波动的、大概符合高斯分布的数组
    """
    my_list = []
    # 标准差取1，得到的数据更加的集中，然后再用2σ进行过滤
    s = list(np.random.normal(mean, 1, 2 * size))

    """
    三个参数分别为均值(μ)、标准差(σ)、数组大小
    参考链接：https://blog.csdn.net/ewfwewef/article/details/109050343
    """

    s = [int(x) for x in s]  # python语法糖

    for i in range(0, size):
        if mean + fluctuation >= s[i] >= mean - fluctuation:
            my_list.append(s[i])

    length = len(my_list)
    if length >= size:
        # 大于需要的长度，截断
        my_list = my_list[0:size]
    else:
        # 小于需要的长度，产生新的随机数，补充进去
        # 新产生的随机数不符合高斯分布，但是由于需要补充的数非常少，所以影响不大
        remainder = size - length
        others = np.random.randint(mean - fluctuation, mean + fluctuation + 1, size=remainder)
        for i in others:
            a = np.random.randint(0, len(my_list), size=1)[0]
            my_list.insert(a, i)
    return my_list


def get_path(read_path, write_path):
    """
    给定一个读取和保存文件的根目录，自动生成每张图片读取和保存的路径
    :param read_path: 读取文件的路径
    :param write_path: 保存文件的路径
    :return: 二维数组，第一个为读取的路径，第二个为保存的路径
    """
    out = []
    file_names = os.listdir(read_path)
    for file_name in file_names:
        abs_read_path = os.path.join(read_path, file_name)
        abs_write_path = os.path.join(write_path, file_name)
        temp = [abs_read_path, abs_write_path]
        out.append(temp)
    return out


def count(img):
    """
    输入一张图片，统计图片每行的像素总值
    :param img: 图片
    :return: 列表，每个元素为图片一行像素总值
    """
    row = img.shape[0]
    c = []
    for i in range(row):
        c.append(sum(row[i]))
    return c


def read_log(path, num=0):
    """
    读取日志中数据，并打印数据的数量
    :param path: 日志路径
    :param num: 日志的第几个表
    :return: 日志中的所有数据
    """
    wb = openpyxl.load_workbook(path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    # 获取第三张sheet
    sheet1 = sheets[num]
    rows = sheet1.rows
    data = []
    inside_count = 0
    for row in rows:
        row_value = [col.value for col in row]
        data.append(row_value)
        inside_count += 1
    data.pop(0)  # 删除开头的数据也即表头
    print("————总共读取了{:d}条数据————".format(inside_count - 1))
    return data


def time_split(startTime, endTime, duration):
    """
    :param startTime: 开始时间（小时）
    :param endTime: 结束时间（小时）
    :param duration: 需要的时长
    :return: 处理之后的开始和结束时间
    """
    hour = duration / 3600
    # 两个时间不能相加
    mid_time = startTime + (endTime - startTime) / 2
    d1 = mid_time - datetime.timedelta(hours=hour / 2)
    d2 = d1 + datetime.timedelta(hours=hour)
    return d1, d2


def save_excel(path, data):
    wb = openpyxl.Workbook()
    ws = wb.active
    table_title = ['startTime', 'endTime', 'startFre', 'endFre', 'types']
    ws.append(table_title)
    for row in data:
        ws.append(row)
    wb.save(path)
    print("成功保存！")



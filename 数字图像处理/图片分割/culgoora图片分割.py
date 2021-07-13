# -*- coding = utf-8 -*-
# @Time : 2021/2/19 14:52
# @Author : 水神与月神
# @File : culgoora图片分割.py
# @Software : PyCharm

# %%

# 24 401*2
# 40 501*4

# %%
import datetime
import numpy as np
import cv2 as cv
import openpyxl
import os

count1 = 0
count2 = 0


# %%
def read_log(path):
    wb = openpyxl.load_workbook(path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    sheet1 = sheets[0]
    rows = sheet1.rows
    data = []
    count = 0
    for row in rows:
        row_value = [col.value for col in row]
        data.append(row_value)
        count += 1
    data.pop(0)  # 删除开头的数据也即表头
    print("读取日志的次数", count)
    return data


# %%

def read_byte(bytestream, num):
    """
   :param bytestream: 一个打开的文件
   :param num: 读取字节的数目
   :return: 返回一个数组
   """
    dt = np.dtype(np.uint8)  # 读取字节
    return np.frombuffer(bytestream.read(num), dtype=dt)


# %%

def read_date(head_data):
    """
    当前数据所对应的时间
    :return:返回一个包含时间信息的数组
    """
    time_data = []
    try:
        for i in range(6):
            time_data.append(head_data[i])
        return time_data
    except TypeError:
        print("没有找到数据头")


# %%
def read(filepath, split_time):
    """
    读取数据
    :return:
    """
    array = []
    with open(filepath, "rb") as f:
        while True:
            header_data = read_byte(f, 40)  # 返回一个数组，存储前40位数据
            if len(header_data) == 0:
                break
            date = read_date(header_data)  # 解析头里面的时间信息，存储在一个数组中
            # 开始条件
            if ((date[1] == split_time[0].month) and (date[2] == split_time[0].day) and
                    (date[3] == split_time[0].hour) and (date[4] == split_time[0].minute) and
                    (date[5] >= 0)):
                while True:
                    needed = read_byte(f, 2004)
                    needed = needed[::-1]
                    array.append(needed)

                    header_data = read_byte(f, 40)  # 返回一个数组，存储前24位数据
                    if len(header_data) == 0:
                        break
                    date = read_date(header_data)  # 解析头里面的时间信息，存储在一个数组中
                    # 结束条件
                    if ((date[1] == split_time[1].month) and (date[2] == split_time[1].day) and
                            (date[3] == split_time[1].hour) and (date[4] == split_time[1].minute) and
                            (date[5] >= 0)):
                        return array
            else:
                needless = read_byte(f, 2004)


# %%

def write_image(array, date, save_path):
    global count1
    global count2
    types = date[4]
    folder = os.path.join(save_path, types)
    name_save = "CG{:4d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}_{:s}_{:s}_{:s}.jpg"
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:
        array_1d = np.concatenate(array, axis=0)  # 将数组拼接成一整个
        dt = np.dtype(np.uint8)
        array_1d = np.array(array_1d, dtype=dt)
        array_nd = array_1d.reshape(-1, 2004)
        array_nd = np.transpose(array_nd).astype(np.uint8)  # 转置

        image_save_path = os.path.join(folder, name_save.format(date[0].year, date[0].month, date[0].day,
                                                                date[0].hour, date[0].minute, types,
                                                                date[2], date[3]))
        cv.imwrite(image_save_path, array_nd)
        count1 += 1
    except TypeError:
        count2 += 1
        print("没有需要的值")
        print(name_save.format(date[0].year, date[0].month, date[0].day,
                               date[0].hour, date[0].minute, types,
                               date[2], date[3]))
        print(date)


# %%

if __name__ == '__main__':
    path_read = r"G:\CulgooraData\culgoora原始数据\{:0>2d}"
    path_save = r"G:\CulgooraData\new"
    path_log = r'G:\CulgooraData\log\原始时长分割.xlsx'
    file_name_format = "SPEC{:0>2d}{:0>2d}{:0>2d}"
    data = read_log(path_log)
    print(len(data))
    count = 0
    count3 = 0
    count4 = 0
    for one_date in data:
        start_year = one_date[0].year
        start_month = one_date[0].month
        start_day = one_date[0].day
        start_hour = one_date[0].hour

        if start_hour > 20:
            one_date[0] = one_date[0] + datetime.timedelta(hours=24)
            start_month = one_date[0].month
            start_day = one_date[0].day
            file_name = os.path.join(path_read.format(start_year % 100),
                                     file_name_format.format(start_year % 100, start_month, start_day))
            one_date[0] = one_date[0] - datetime.timedelta(hours=24)

        else:
            file_name = os.path.join(path_read.format(start_year % 100),
                                     file_name_format.format(start_year % 100, start_month, start_day))
        try:
            row_array = read(file_name, one_date)
            write_image(row_array, one_date, path_save)
            count3+=1
        except FileNotFoundError:
            print(one_date)
            count4 += 1

    print("有{:d}个文件没有找到".format(count))
    print("保存的次数为{:d}\n没有找到数据的次数为{:d}".format(count1, count2))
    print(count3, count4)



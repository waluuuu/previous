# -*- coding = utf-8 -*-
# @Time : 2021/4/24 15:19
# @Author : 水神与月神
# @File : 分割时间（原始时长）.py
# @Software : PyCharm

"""
对日志文件进行清洗，然后根据原始时长分割图片
二型爆最短10分钟，别的不限
三型爆时长5分钟或10分钟
"""

import mypackage.dip_function as df
import openpyxl
import datetime

path_read = r"G:\LearmonthData\日志文件合并\2001-2020合并清洗.xlsx"
path_save = r"G:\LearmonthData\日志文件合并\原始时长分割.xlsx"

data = df.read_log(path_read, 0)
data2 = []
# startTime	endTime	duration	startFre	endFre	Frequency drift	types
for row_value in data:
    temp_use = []
    if row_value[6] == "III" or row_value[6] == "V":
        if (row_value[1] - row_value[0]).seconds > 600:
            continue
        elif (row_value[1] - row_value[0]).seconds > 300:
            d1, d2 = df.time_split(row_value[0], row_value[1], 600)
        else:
            d1, d2 = df.time_split(row_value[0], row_value[1], 300)
    elif row_value[6] == "II":
        if (row_value[1] - row_value[0]).seconds > 1200:
            continue
        elif (row_value[1] - row_value[0]).seconds < 600:
            d1, d2 = df.time_split(row_value[0], row_value[1], 600)
        else:
            d1, d2 = row_value[0], row_value[1]
    elif row_value[6] == "IV":
        if (row_value[1] - row_value[0]).seconds < 600:
            continue
        else:
            d1, d2 = row_value[0], row_value[1]
    else:
        d1, d2 = row_value[0], row_value[1]

    temp_use.append(d1)  # 开始时间
    temp_use.append(d2)  # 结束时间
    temp_use.append(row_value[3])  # 最低频率
    temp_use.append(row_value[4])  # 最高频率
    temp_use.append(row_value[6])  # 大类
    data2.append(temp_use)

df.save_excel(path_save, data2)

# -*- coding = utf-8 -*-
# @Time : 2021/4/24 16:46
# @Author : 水神与月神
# @File : 分割时间（原始时长）（C）.py
# @Software : PyCharm


import mypackage.dip_function as df
import openpyxl
import datetime

path_read = r"G:\CulgooraData\log\1994-2015合并.xlsx"
path_save = r"G:\CulgooraData\log\原始时长分割.xlsx"

data = df.read_log(path_read, 0)
data2 = []
# startTime	endTime	duration	startFre	endFre	Frequency drift	types
for row_value in data:
    temp_use = []
    if row_value[5] == "III" or row_value[5] == "V":
        if (row_value[1] - row_value[0]).seconds > 600:
            d1, d2 = row_value[0], row_value[1]
        elif (row_value[1] - row_value[0]).seconds > 300:
            d1, d2 = df.time_split(row_value[0], row_value[1], 600)
        else:
            d1, d2 = df.time_split(row_value[0], row_value[1], 300)
    elif row_value[5] == "II":
        if (row_value[1] - row_value[0]).seconds > 1200:
            continue
        elif (row_value[1] - row_value[0]).seconds < 600:
            d1, d2 = df.time_split(row_value[0], row_value[1], 600)
        else:
            d1, d2 = row_value[0], row_value[1]
    elif row_value[5] == "IV":
        if (row_value[1] - row_value[0]).seconds < 600:
            continue
        else:
            d1, d2 = row_value[0], row_value[1]
    elif row_value[5]== "I":
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
    temp_use.append(row_value[5])  # 大类
    temp_use.append(row_value[6])  # 小类
    temp_use.append(row_value[7])  # 强度
    data2.append(temp_use)

df.save_excel(path_save, data2)



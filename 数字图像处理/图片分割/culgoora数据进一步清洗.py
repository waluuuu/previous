# -*- coding = utf-8 -*-
# @Time : 2021/2/24 14:09
# @Author : 水神与月神
# @File : culgoora数据进一步清洗.py
# @Software : PyCharm


"""
发现数据存在重合的情况，进一步清洗数据，
如果开始时间相同，那么就删除

"""

import openpyxl
import culgoora日志分类时间分割 as cu

path = "C:\\Users\\dell\\Desktop\\1994-2015合并时间分割.xlsx"
path2 = "C:\\Users\\dell\\Desktop\\1994-2015二型.xlsx"
wb = openpyxl.load_workbook(path)
sheets = wb.worksheets  # 获取当前所有的sheet
# 获取第一张sheet
sheet1 = sheets[2]
rows = sheet1.rows
data = []
data2 = []
# 迭代读取所有的行
for row in rows:
    temp_use = []
    row_value = [col.value for col in row]
    temp_use.append(row_value[0])  # 开始时间
    temp_use.append(row_value[1])  # 结束时间
    temp_use.append(row_value[2])  # 最低频率
    temp_use.append(row_value[3])  # 最高频率
    temp_use.append(row_value[4])  # 大类
    temp_use.append(row_value[5])  # 小类
    temp_use.append(row_value[6])  # 爆发强度
    data.append(temp_use)

data.pop(0)
data2.append(data[0])
for i in range(0,len(data)):
    for j in range(0, len(data2)):
        if data[j][0] == data[i][0]:
            break
        if j == len(data2) - 1:
            data2.append(data[i])

cu.save_new_time(data2, path2)






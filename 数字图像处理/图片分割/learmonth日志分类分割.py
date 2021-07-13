# -*- coding = utf-8 -*-
# @Time : 2021/1/23 21:41
# @Author : 水神与月神
# @File : learmonth日志分类分割.py
# @Software : PyCharm


# %%
import datetime
import openpyxl


# %%
def get_new_time(path):
    wb = openpyxl.load_workbook(path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    # 获取第一张sheet
    sheet1 = sheets[0]
    rows = sheet1.rows
    data = []
    # 迭代读取所有的行
    for row in rows:
        # 获得每一行的全部值
        row_value = [col.value for col in row]
        if row_value[6] == 'II':
            temp_use = []
            if (row_value[1] - row_value[0]).seconds > 1200:
                continue
            d1, d2 = my_split(row_value[0], row_value[1], 1200)
            temp_use.append(d1)  # 开始时间
            temp_use.append(d2)  # 结束时间
            temp_use.append(row_value[3])  # 最低频率
            temp_use.append(row_value[4])  # 最高频率
            temp_use.append(row_value[6])  # 大类
            data.append(temp_use)
        elif row_value[6] == 'III' or row_value[6] == 'V':
            if (row_value[1] - row_value[0]).seconds > 600:
                continue
            temp_use = []
            d1, d2 = my_split(row_value[0], row_value[1], 600)
            temp_use.append(d1)  # 开始时间
            temp_use.append(d2)  # 结束时间
            temp_use.append(row_value[3])  # 最低频率
            temp_use.append(row_value[4])  # 最高频率
            temp_use.append(row_value[6])  # 大类
            data.append(temp_use)
        else:
            if (row_value[1] - row_value[0]).seconds >= 39600:
                continue
            elif (row_value[1] - row_value[0]).seconds > 3600:
                num = (row_value[1] - row_value[0]).seconds // 3600
                mod = (row_value[1] - row_value[0]).seconds % 3600
                if mod >= 600:
                    for i in range(num+1):
                        temp_use = []
                        d1 = row_value[0] + datetime.timedelta(hours=i)
                        d2 = d1 + datetime.timedelta(hours=1)
                        temp_use.append(d1)  # 开始时间
                        temp_use.append(d2)  # 结束时间
                        temp_use.append(row_value[3])  # 最低频率
                        temp_use.append(row_value[4])  # 最高频率
                        temp_use.append(row_value[6])  # 大类
                        data.append(temp_use)
                else:
                    for i in range(num):
                        temp_use = []
                        d1 = row_value[0] + datetime.timedelta(hours=i)
                        d2 = d1 + datetime.timedelta(hours=1)
                        temp_use.append(d1)  # 开始时间
                        temp_use.append(d2)  # 结束时间
                        temp_use.append(row_value[3])  # 最低频率
                        temp_use.append(row_value[4])  # 最高频率
                        temp_use.append(row_value[6])  # 大类
                        data.append(temp_use)
            else:
                temp_use = []
                d1, d2 = my_split(row_value[0], row_value[1], 3600)
                temp_use.append(d1)  # 开始时间
                temp_use.append(d2)  # 结束时间
                temp_use.append(row_value[3])  # 最低频率
                temp_use.append(row_value[4])  # 最高频率
                temp_use.append(row_value[6])  # 大类
                data.append(temp_use)
    return data


def save_new_time(data, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    table_title = ['startTime', 'endTime', 'startFre', 'endFre', 'types']
    ws.append(table_title)
    for row in data:
        ws.append(row)
    wb.save(path)


def my_split(startTime, endTime, duration):
    hour = duration / 3600
    # 两个时间不能相加
    mid_time = startTime + (endTime - startTime) / 2
    d1 = mid_time - datetime.timedelta(hours=hour / 2)
    d2 = d1 + datetime.timedelta(hours=hour)
    return d1, d2


if __name__ == "__main__":
    read_path = r"G:\LearmonthData\日志文件合并\2001-2020清洗之后.xlsx"
    save_path = r"G:\LearmonthData\日志文件合并\2001-2020合并时间分割.xlsx"

    save_new_time(get_new_time(read_path), save_path)
    print("保存成功！")



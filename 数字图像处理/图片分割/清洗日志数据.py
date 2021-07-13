# -*- coding = utf-8 -*-
# @Time : 2021/1/21 15:10
# @Author : 水神与月神
# @File : 清洗日志数据.py
# @Software : PyCharm


import datetime
import openpyxl


# %%
def data_cleaning(path):
    wb = openpyxl.load_workbook(path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    # 获取第一张sheet
    sheet1 = sheets[0]
    rows = sheet1.rows
    data = []
    index = 0
    # 迭代读取所有的行
    for row in rows:
        index += 1
        temp_use = []
        # 获得每一行的全部值
        row_value = [col.value for col in row]
        # 开始日期和结束日期
        try:
            date1 = row_value[0].split("/")
            date2 = row_value[2].split("/")
            # 开始时间和结束时间
            time1 = row_value[1].split(":")
            time2 = row_value[3].split(":")
        except AttributeError:
            print(index)
            continue
        try:
            d1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]), int(time1[0]), int(time1[1]))
            d2 = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]), int(time2[0]), int(time2[1]))
        except ValueError:
            continue
        drift = int(row_value[7]) - int(row_value[6])
        if d1 > d2 or drift < 0:      # 判断开始时间是否小于结束时间 and 频率
            continue
        duration = (d2 - d1)
        temp_use.append(d1)  # 开始时间
        temp_use.append(d2)  # 结束时间
        temp_use.append(duration)  # 持续时间
        temp_use.append(row_value[6])  # 最低频率
        temp_use.append(row_value[7])  # 最高频率
        temp_use.append(drift)  # 频率漂移
        temp_use.append(row_value[5])  # 爆发类型
        # 将数组存放到更大的数组
        data.append(temp_use)
    return data


# %%
def save_new_time(data, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    table_title = ['startTime', 'endTime', 'duration', 'startFre', 'endFre', 'Frequency drift', 'types']
    ws.append(table_title)
    for row in data:
        ws.append(row)
    wb.save(path)


if __name__ == "__main__":
    years = []
    read_path = r"G:\LearmonthData\日志文件合并\2001-2020.xlsx"
    save_path = r"G:\LearmonthData\日志文件合并\2001-2020清洗之后.xlsx"
    save_new_time(data_cleaning(read_path), save_path)
    print("保存成功！")



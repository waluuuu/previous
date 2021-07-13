# -*- coding = utf-8 -*-
# @Time : 2020/12/21 22:00
# @Author : 水神与月神
# @File : NewTime.py
# @Software : PyCharm

# %%
import datetime
import openpyxl


# %%
# 检查日期的合理性
def check_date(year, month, day):
    # if判断输入的年月日的正确合理性
    if 0 < month <= 12:
        if (month in (1, 3, 5, 7, 8, 10, 12)) and (day > 31 or day < 0):
            return 1
        if (month in (4, 6, 9, 11)) and (day > 30 or day < 0):
            return 1
        if month == 2:
            if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                if day > 29 or day < 0:
                    return 1
            else:
                if day > 28 or day < 0:
                    return 1
    else:
        return 1


# %%
def get_new_time(path):
    # 小时->秒
    hour_second = 3600
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
        # 开始日期和结束日期
        date1 = row_value[0].split("/")
        date2 = row_value[2].split("/")
        # 开始时间和结束时间
        time1 = row_value[1].split(":")
        time2 = row_value[3].split(":")

        # 判断日期是否合乎规范
        # 有的表存在表头，用异常检测避免报错
        try:
            if check_date(int(date1[0]), int(date1[1]), int(date1[2])) or check_date(int(date2[0]), int(date2[1]),
                                                                                     int(date2[2])):
                continue
        except ValueError:
            continue
        # 生成开始时间和结束时间
        # 进行异常检测，存在时间错误的情况
        try:
            d1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]), int(time1[0]), int(time1[1]))
            d2 = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]), int(time2[0]), int(time2[1]))
        except ValueError:
            continue
        seconds = (d2 - d1).seconds

        # 生成需要分割的时间
        if seconds < 1800:
            temp_use = []
            d3 = None
            d4 = None
            if seconds == 0:
                # 开始时间和结束时间
                d3 = d1 - datetime.timedelta(hours=0.25)
                d4 = d2 + datetime.timedelta(hours=0.25)
            else:
                remainder_seconds = 1800 - seconds
                # 转换成小时
                remainder_hours = remainder_seconds / hour_second
                # 计算开始和结束各需要增加多少时间
                half_remainder_hours = remainder_hours // 2
                d3 = d1 - datetime.timedelta(hours=half_remainder_hours)
                d4 = d3 + datetime.timedelta(hours=0.5)
            # 将需要的信息添加到数组中
            temp_use.append(d3)
            temp_use.append(d4)
            temp_use.append(row_value[5])
            temp_use.append(row_value[6])
            temp_use.append(row_value[7])
            # 将数组存放到更大的数组
            data.append(temp_use)

        else:
            num = seconds // 1800
            for i in range(num):
                temp_use = []
                d3 = d1 + datetime.timedelta(hours=i * 0.5)
                d4 = d3 + datetime.timedelta(hours=0.5)

                temp_use.append(d3)
                temp_use.append(d4)
                temp_use.append(row_value[5])
                temp_use.append(row_value[6])
                temp_use.append(row_value[7])

                data.append(temp_use)

    return data


# %%
def save_new_time(data, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    table_title = ['startTime', 'endTime', 'types', 'startFre', 'endFre']
    ws.append(table_title)
    for row in data:
        ws.append(row)
    wb.save(path)


if __name__ == "__main__":
    years = []
    read_root_path = "C:/Users/dell/Desktop/日志文件合并/{:d}年合并.xlsx"
    save_root_path = "C:/Users/dell/Desktop/分割时间/{:d}.xlsx"
    for year in range(2001, 2021):
        years.append(year)
    for year in years:
        read_path = read_root_path.format(year)
        save_path = save_root_path.format(year)
        save_new_time(get_new_time(read_path), save_path)
        print("保存成功！")

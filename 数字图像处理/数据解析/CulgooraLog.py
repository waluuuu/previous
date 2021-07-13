# -*- coding = utf-8 -*-
# @Time : 2021/1/21 17:17
# @Author : 水神与月神
# @File : CulgooraLog.py
# @Software : PyCharm


import openpyxl
import datetime
import os


def read_log(root_path):
    data = []  # 存储读取的数据
    files = os.listdir(root_path)

    for file in files:
        path = os.path.join(root_path, file)

        ###################################################
        # 读取每行数据
        ###################################################
        for line in open(path, 'r'):
            temp_use = []
            temp = line.split()
            if not temp:
                continue
            else:
                if len(temp) < 9:
                    continue
                if temp[3] == 'CULG':
                    if len(temp) < 11:
                        continue
                    temp.pop(1)
                    temp.pop(1)
                elif temp[1] == 'CULG':
                    pass
                else:
                    continue

            ##################################################
            # 改变数据的格式
            ##################################################
            # 得到日期
            func = lambda x: 1900 if x > 90 else 2000
            year = int(temp[0]) // 10000
            year = year + func(year)
            month = int(temp[0]) // 100 % 100
            day = int(temp[0]) % 100
            # 得到时间
            try:
                start_hour = int(temp[2][:4]) // 100
                start_min = int(temp[2][:4]) % 100
                end_hour = int(temp[3][:4]) // 100
                end_min = int(temp[3][:4]) % 100
            except ValueError:
                continue

            ###################################################
            # 生成开始时间和结束时间
            ###################################################
            try:
                d1 = datetime.datetime(year, month, day, start_hour, start_min)
                d2 = datetime.datetime(year, month, day, end_hour, end_min)
                if d1 > d2:
                    continue
            except ValueError:
                continue
            temp_use.append(d1)  # 开始时间
            temp_use.append(d2)  # 结束时间
            temp_use.append(d2 - d1)  # 持续时间
            temp_use.append(temp[7])  # 最低频率
            temp_use.append(temp[8])  # 最高频率
            temp_use.append(temp[4])  # 大类
            temp_use.append(temp[5])  # 小类
            temp_use.append(temp[6])  # 爆发强度

            if len(temp) > 9:
                remark = ''
                remarks = temp[9:]
                for i in remarks:
                    remark += i
                    remark += ' '
                temp_use.append(remark)
            data.append(temp_use)
    return data


def write_log(data, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    table_title = ['startTime', 'endTime', 'duration', 'startFre', 'endFre', 'types', 'Appended symbols', 'intensity',
                   'remarks']
    ws.append(table_title)
    for row in data:
        ws.append(row)
    wb.save(path)


read_path = "G:/CulgooraData/log_culgoora/{:d}/"
save_path = "G:/CulgooraData/log/{:d}.xlsx"

years = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
         2012, 2013, 2014, 2015]
if __name__ == "__main__":
    for year in years:
        write_log(read_log(read_path.format(year)), save_path.format(year))
        print(str(year) + "年数据日志转换完毕")


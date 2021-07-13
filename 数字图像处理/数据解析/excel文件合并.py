# -*- coding = utf-8 -*-
# @Time : 2021/1/23 14:40
# @Author : 水神与月神
# @File : excel文件合并.py
# @Software : PyCharm


import os
import openpyxl


def excel_merge(path):
    data = []
    names = os.listdir(path)
    for name in names:
        log_path = os.path.join(path, name)
        wb = openpyxl.load_workbook(log_path)
        sheets = wb.worksheets  # 获取当前所有的sheet
        # 获取第一张sheet
        sheet1 = sheets[0]
        rows = sheet1.rows
        flag = 0
        for row in rows:
            if flag == 0:
                flag = 2
                continue
            # 获得每一行的全部值
            row_value = [col.value for col in row]
            # 开始日期和结束日
            data.append(row_value)
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


if __name__ == '__main__':
    root_path = r'G:\CulgooraData\log'
    save_path = r'G:\CulgooraData\log\1994-2015合并.xlsx'
    write_log(excel_merge(root_path), save_path)



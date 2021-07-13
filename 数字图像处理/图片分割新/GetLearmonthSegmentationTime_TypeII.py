# -*- coding = utf-8 -*-
# @Time : 2021/3/26 15:13
# @Author : 水神与月神
# @File : GetLearmonthSegmentationTime_TypeII.py
# @Software : PyCharm

import openpyxl
import datetime


def mySplit(startTime, endTime, duration):
    hour = duration / 3600
    # 两个时间不能相加
    mid_time = startTime + (endTime - startTime) / 2
    d1 = mid_time - datetime.timedelta(hours=hour / 2)
    d2 = d1 + datetime.timedelta(hours=hour)
    return d1, d2


class GetSegmentationTime:
    def __init__(self, read_path, save_path):
        self.read_path = read_path
        self.save_path = save_path
        self.threshold_II = 1200
        # 小于5分钟，按5分钟计算，小于10分钟，按10分钟计算，其余按20分钟
        self.seg_time_II = {0: 600, 1: 600, 2: 1200, 3: 1200, 4: 1200}

    def getSegmentationTime(self):
        wb = openpyxl.load_workbook(self.read_path)
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
                # 时长大于20分钟，放弃该数据
                if (row_value[1] - row_value[0]).seconds > 1200:
                    continue
                d1, d2 = mySplit(row_value[0], row_value[1],
                                 self.seg_time_II[(row_value[1] - row_value[0]).seconds // 300])
                temp_use.append(d1)  # 开始时间
                temp_use.append(d2)  # 结束时间
                temp_use.append(row_value[3])  # 最低频率
                temp_use.append(row_value[4])  # 最高频率
                temp_use.append(row_value[6])  # 大类
                data.append(temp_use)
            else:
                pass
        return data

    def saveDate(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        table_title = ['startTime', 'endTime', 'startFre', 'endFre', 'types']
        ws.append(table_title)
        for row in self.getSegmentationTime():
            ws.append(row)
        wb.save(self.save_path)
        print("成功保存！")


    def newDate(self):
        self.saveDate()


if __name__ == "__main__":
    read_path = r"G:\LearmonthData\日志文件合并\2001-2020合并清洗.xlsx"
    save_path = r"G:\LearmonthData\日志文件合并\2001-2020合并清洗II02.xlsx"
    GetSegmentationTime(read_path, save_path).newDate()

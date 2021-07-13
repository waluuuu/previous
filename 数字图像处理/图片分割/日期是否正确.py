# -*- coding = utf-8 -*-
# @Time : 2021/1/21 15:44
# @Author : 水神与月神
# @File : 日期是否正确.py
# @Software : PyCharm


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
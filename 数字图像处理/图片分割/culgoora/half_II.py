# -*- coding = utf-8 -*-
# @Time : 2021/4/16 19:52
# @Author : 水神与月神
# @File : half.py
# @Software : PyCharm

"""
选取culgoora图片下半部分
"""
import mypackage.dip_function as df


if __name__ == "__main__":
    path_read = r"G:\CulgooraData\test\all"
    path_save = r"G:\CulgooraData\test\half"
    df.half(path_read,path_save)



# -*- coding = utf-8 -*-
# @Time : 2020/10/20 15:47
# @Author : 水神与月神
# @File : 下载日志文件.py
# @Software : PyCharm

import os
import requests

import os
import requests


class DownloadPic:
    def __init__(self, base_url, file_url, end_year, end_mouth, start_year, start_mouth):
        self.baseUrl = base_url
        self.endYear = end_year
        self.startYear = start_year
        self.startMouth = start_mouth
        self.endMouth = end_mouth
        self.f = open(file_url, 'w+', encoding='utf-8')

    def __download_first_year(self):
        for year in range(self.startYear, self.startYear + 1):
            for mouth in range(self.startMouth, 13):
                path = 'log_culgoora/{:d}/'.format(year)  # 创建文件夹，用来存储日志
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                log_url = self.baseUrl.format(year, year % 100, mouth)  # 图片网址
                log_name = "{:d}.{:0>2d}".format(year, mouth)  # 图片名称
                # 异常处理
                try:
                    log = requests.get(log_url, timeout=100)  # 得到图片
                except requests.exceptions.ConnectionError:
                    print('连接超时，请手动下载', end="###")
                    self.f.writelines(log_url + "\n")  # 整行写入并换行
                    print("已将网址写入文件")
                    continue
                # 准备写入图片
                dir = path + log_name + ".txt"  # 图片写入地址
                fp = open(dir, 'wb')
                print("正在下载{:d}年{:0>2d}月的日志".format(year, mouth))
                fp.write(log.content)  # 写入图片
                fp.close()

    def __download_mid_years(self):
        for year in range(self.startYear + 1, self.endYear):
            for mouth in range(1, 13):
                path = 'log_culgoora/{:d}/'.format(year)  # 创建文件夹，用来存储日志
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                log_url = self.baseUrl.format(year, year % 100, mouth)  # 图片网址
                log_name = "{:d}.{:0>2d}".format(year, mouth)  # 图片名称
                # 异常处理
                try:
                    log = requests.get(log_url, timeout=100)  # 得到图片
                except requests.exceptions.ConnectionError:
                    print('连接超时，请手动下载', end="###")
                    self.f.writelines(log_url + "\n")  # 整行写入并换行
                    print("已将网址写入文件")
                    continue
                # 准备写入图片
                dir = path + log_name + ".txt"  # 图片写入地址
                fp = open(dir, 'wb')
                print("正在下载{:d}年{:0>2d}月的日志".format(year, mouth))
                fp.write(log.content)  # 写入图片
                fp.close()

    def __download_last_year(self):
        for year in range(self.endYear, self.endYear + 1):
            for mouth in range(1, self.endMouth + 1):
                path = 'log_culgoora/{:d}/'.format(year)  # 创建文件夹，用来存储日志
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                log_url = self.baseUrl.format(year, year % 100, mouth)  # 图片网址
                log_name = "{:d}.{:0>2d}".format(year, mouth)  # 图片名称
                # 异常处理
                try:
                    log = requests.get(log_url, timeout=100)  # 得到图片
                except requests.exceptions.ConnectionError:
                    print('连接超时，请手动下载', end="###")
                    self.f.writelines(log_url + "\n")  # 整行写入并换行
                    print("已将网址写入文件")
                    continue
                # 准备写入图片
                dir = path + log_name + ".txt"  # 图片写入地址
                fp = open(dir, 'wb')
                print("正在下载{:d}年{:0>2d}月的日志".format(year, mouth))
                fp.write(log.content)  # 写入图片
                fp.close()

    def download(self):
        self.__download_first_year()
        self.__download_mid_years()
        self.__download_last_year()
        self.f.close()


base_url = r'http://www.sws.bom.gov.au/Category/World%20Data%20Centre/Data%20Display%20and%20Download/Spectrograph/eventlogs/culgoora/{:d}/culgoorarsg{:0>2d}{:0>2d}.txt'
file_url = r'log_download_failed.txt'

DownloadPic(base_url=base_url, file_url=file_url, end_year=2015, end_mouth=12, start_year=1994,
            start_mouth=1).download()



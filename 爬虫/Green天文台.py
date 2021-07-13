# -*- coding = utf-8 -*-
# @Time : 2020/10/20 16:55
# @Author : 水神与月神
# @File : Green天文台.py
# @Software : PyCharm

import os
import requests


class DownloadPic:
    def __init__(self, base_url, file_url, end_year, end_mouth, start_year, start_mouth):
        self.baseUrl = base_url
        self.endYear = end_year
        self.startYear = start_year
        self.startMouth = start_mouth
        self.endMouth = end_mouth

    def __download_first_year(self):
        for year in range(self.startYear, self.startYear + 1):
            for mouth in range(self.startMouth, 13):
                path = 'G://images_culgoora/{:d}/{:d}/'.format(year, mouth)  # 创建文件夹，用来存储图片
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                for day in range(1, 32):
                    pic_url = self.baseUrl.format(year % 100, year, mouth, day)  # 图片网址
                    pic_name = "{:d}.{:0>2d}.{:0>2d}".format(year, mouth, day)  # 图片名称
                    # 异常处理
                    try:
                        pic = requests.get(pic_url, timeout=100)  # 得到图片
                    except requests.exceptions.ConnectionError:
                        print('连接超时，请手动下载', end="###")
                        self.f = open(file_url, 'w+', encoding='utf-8')
                        self.f.writelines(pic_url + "\n")  # 整行写入并换行
                        self.f.close()
                        print("已将网址写入文件")
                        continue
                    except requests.HTTPError:
                        print('没有找到网页')
                        continue
                    # 准备写入图片
                    dir = path + pic_name + ".jpg"  # 图片写入地址
                    fp = open(dir, 'wb')
                    print("正在下载{:d}年{:0>2d}月{:0>2d}日的照片".format(year, mouth, day))
                    fp.write(pic.content)  # 写入图片
                    fp.close()

    def __download_mid_years(self):
        for year in range(self.startYear + 1, self.endYear):
            for mouth in range(1, 13):
                path = 'G://images_culgoora/{:d}/{:d}/'.format(year, mouth)  # 创建文件夹，用来存储图片
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                for day in range(1, 32):
                    pic_url = self.baseUrl.format(year % 100, year, mouth, day)  # 图片网址
                    pic_name = "{:d}.{:0>2d}.{:0>2d}".format(year, mouth, day)  # 图片名称
                    # 异常处理
                    try:
                        pic = requests.get(pic_url, timeout=100)  # 得到图片
                    except requests.exceptions.ConnectionError:
                        print('连接超时，请手动下载', end="###")
                        self.f = open(file_url, 'w+', encoding='utf-8')
                        self.f.writelines(pic_url + "\n")  # 整行写入并换行
                        self.f.close()
                        print("已将网址写入文件")
                        continue
                    except requests.HTTPError:
                        print('没有找到网页')
                        continue
                    # 准备写入图片
                    dir = path + pic_name + ".jpg"  # 图片写入地址
                    fp = open(dir, 'wb')
                    print("正在下载{:d}年{:0>2d}月{:0>2d}日的照片".format(year, mouth, day))
                    fp.write(pic.content)  # 写入图片
                    fp.close()

    def __download_last_year(self):
        for year in range(self.endYear, self.endYear + 1):
            for mouth in range(1, self.endMouth + 1):
                path = 'G://images_culgoora/{:d}/{:d}/'.format(year, mouth)  # 创建文件夹，用来存储图片
                if os.path.exists(path):
                    pass  # 存在文件夹，跳过
                else:
                    os.makedirs(path)  # 不存在文件夹，创建
                for day in range(1, 32):
                    pic_url = self.baseUrl.format(year % 100, year, mouth, day)  # 图片网址
                    pic_name = "{:d}.{:0>2d}.{:0>2d}".format(year, mouth, day)  # 图片名称
                    # 异常处理
                    try:
                        pic = requests.get(pic_url, timeout=100)  # 得到图片
                    except requests.exceptions.ConnectionError:
                        print('连接超时，请手动下载', end="###")
                        self.f = open(file_url, 'w+', encoding='utf-8')
                        self.f.writelines(pic_url + "\n")  # 整行写入并换行
                        self.f.close()
                        print("已将网址写入文件")
                        continue
                    except requests.HTTPError:
                        print('没有找到网页')
                        continue
                    # 准备写入图片
                    dir = path + pic_name + ".jpg"  # 图片写入地址
                    fp = open(dir, 'wb')
                    print("正在下载{:d}年{:0>2d}月{:0>2d}日的照片".format(year, mouth, day))
                    fp.write(pic.content)  # 写入图片
                    fp.close()

    def download(self):
        self.__download_first_year()
        self.__download_mid_years()
        self.__download_last_year()


base_url = r'http://www.sws.bom.gov.au/Category/World%20Data%20Centre/Data%20Display%20and%20Download/Spectrograph/station/culgoora/images/{:0>2d}/{:d}{:0>2d}{:0>2d}spectrograph.gif'
# 另一个天文台
# r'http://www.sws.bom.gov.au/Category/World%20Data%20Centre/Data%20Display%20and%20Download/Spectrograph/station/learmonth/images/{:0>2d}/{:d}{:0>2d}{:0>2d}spectrograph.gif'
file_url = r'download_failed.txt'

download = DownloadPic(base_url=base_url, file_url=file_url, end_year=2015, end_mouth=12, start_year=1997,
                       start_mouth=4).download()

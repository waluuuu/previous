# -*- coding = utf-8 -*-
# @Time : 2020/10/20 14:39
# @Author : 水神与月神
# @File : 下载图片.py
# @Software : PyCharm


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import requests
import os
import xlwt  # 进行excel操作


class Green:
    '''
    输入年份和爆发类型
    通过调用getDATE方法来下载数据
    下载的数据自动按爆发类型和年份分类
    爆发时间和网站上对图片的描述信息保存到Exel文件
    如果网页上没有图片，依旧会创建文件夹
    '''

    def __init__(self, year, type):
        self._year = year
        self._type = type
        self._baseurl = r'https://www.astro.umd.edu/~white/gb/Html/{:d}/{}_ims.html'
        # 正则表达式
        self._findLink = re.compile(r'<a href="(.*?)">')  # 找到图片网址
        self._findTime = re.compile(r'<p>(.*?)<br/>', re.S)  # 找到图片时间信息
        self._findInfo = re.compile(r'<br/>(.*?)<br/>', re.S)

    def _askURL(self):
        head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
        }
        # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
        self._url = self._baseurl.format(self._year, self._type)
        request = urllib.request.Request(self._url, headers=head)
        self._html = ""
        try:
            response = urllib.request.urlopen(request)
            self._html = response.read().decode("utf-8")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

    def _createFolder(self):
        self._path = 'green/{}/{:d}/'.format(self._type, self._year)  # 创建文件夹，用来存储图片
        if os.path.exists(self._path):
            pass  # 存在文件夹，跳过
        else:
            os.makedirs(self._path)  # 不存在文件夹，创建

    def getDATE(self):
        self._askURL()  # 得到网页内容
        soup = BeautifulSoup(self._html, "html.parser")  # 用BeautifulSoup处理
        self._createFolder()  # 创建文件夹，保存图片和数据
        self._bigData = []
        all = soup.find_all('td', valign="top")
        if all == []:
            print("{}年{}类型信息不存在".format(self._year, self._type))
        else:
            for item in all:  # 查找符合要求的字符串，形成列表
                self._data = []
                item = str(item)
                self._link = re.findall(self._findLink, item)[0]
                self._time = re.findall(self._findTime, item)[0]
                self._time = re.sub(r'\n', "", self._time)  # 去掉换行
                self._info = re.findall(self._findInfo, item)[0]
                self._info = re.sub(r'\n', "", self._info)  # 去掉换行
                self._getImage()
                self._data.append([self._myurl, self._time, self._info, self._link, self._picurl])  # 将信息保存到数组中
                self._bigData.append(self._data)
            self._saveData()

    def _changeUrl(self):

        self._myurl = re.findall(r'{}/(.*?).html'.format(self._type), self._link)[0]
        self._picurl = r'https://www.astro.umd.edu/~white/gb/Data/Images/{:d}/{:0>2d}/{:0>2d}/{}.png'.format(
            int(self._myurl[0:4]),
            int(self._myurl[4:6]),
            int(self._myurl[6:8]),
            self._myurl)

    def _saveImage(self):
        picname = self._myurl
        dir = self._path + picname + ".jpg"  # 图片写入地址
        fp = open(dir, 'wb')
        fp.write(self._pic.content)  # 写入图片
        fp.close()
        print("图片保存成功！，路径为{}".format(dir))



    def _getImage(self):
        self._changeUrl()  # 改变网址
        self._pic = requests.get(self._picurl, timeout=100)  # 得到图片
        self._saveImage()  # 保存图片

    def _saveData(self):
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
        sheet = book.add_sheet("{}_{}".format(self._type, self._year), cell_overwrite_ok=True)  # 创建工作表
        col = ("图片名称", "时间", "信息", "图片前级链接", "图片链接")
        for i in range(0, 5):
            sheet.write(0, i, col[i])  # 列名
        for i in range(0, len(self._bigData)):
            data = self._bigData[i]
            for j in range(0, 5):
                sheet.write(i + 1, j, data[0][j])  # 数据
        book.save(self._path + "{}.xls".format(self._year))  # 保存
        print("{}年{}类型信息保存成功".format(self._year, self._type))


years = [2004, 2005, 2006, 2007, 2008, 2009, 2010,2011, 2012, 2013, 2014, 2015]
types = [ "Flare", "Continua", "Other"]
for type in types:
    for year in years:
        mygreen = Green(year=year, type=type).getDATE()

# years = [2011, 2012, 2013, 2014, 2015]
# for year in years:
#          mygreen = Green(year=year, type="TypeIV").getDATE()


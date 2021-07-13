# -*- coding = utf-8 -*-
# @Time : 2020/12/1 9:41
# @Author : 水神与月神
# @File : DownloadRawData.py
# @Software : PyCharm


from ftplib import FTP
import os


def ftpConnect(ftpserver, port):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login()
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome())  # 打印登陆成功后的欢迎信息
        print('\n+------- ftp connection successful!!! --------+')
        return ftp


# 下载单个文件
def ftpDownloadFile(ftp, ftpfile, localfile):
    # fid = open(localfile, 'wb') # 以写模式打开本地文件
    bufsize = 1024
    with open(localfile, 'wb') as fid:
        ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize)  # 接收服务器文件并写入本地文件
    return True


# 下载整个目录下的文件
def ftpDownload(ftp, ftpath, localpath):
    print('Remote Path: {0}'.format(ftpath))
    if not os.path.exists(localpath):
        os.makedirs(localpath)
    file_names = os.listdir(localpath)
    ftp.cwd(ftpath)
    print('+---------- downloading ----------+')
    for file in ftp.nlst():
        if file in file_names:
            continue
        local = os.path.join(localpath, file)
        if os.path.isdir(file):  # 判断是否为子目录
            if not os.path.exists(local):
                os.makedirs(local)
            ftpDownload(ftp, file, local)  # 递归调用
        else:
            ftpDownloadFile(ftp, file, local)
        print(file)
    ftp.cwd('..')
    ftp.quit()
    return True


# 程序入口
if __name__ == '__main__':

    ftpserver = 'ftp-out.sws.bom.gov.au'
    port = 21
    base_path = '/wdc/wdc_spec/data/culgoora/raw/{:0>2d}/'
    base_local_path = 'G:/CulgooraData/culgoora原始数据/{:0>2d}/'

    for i in range(94, 100):
        ft_path = base_path.format(i)
        local_path = base_local_path.format(i)
        ftp = ftpConnect(ftpserver, 21)
        flag = ftpDownload(ftp, ft_path, local_path)
        print(flag)
        # ftp.quit()
        print("\n+-------- OK!!! --------+\n")


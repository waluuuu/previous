# -*- coding = utf-8 -*-
# @Time : 2020/11/28 11:49
# @Author : 水神与月神
# @File : ReadFile.py
# @Software : PyCharm

# %%
import os
import numpy as np
import cv2 as cv


# %%
# 这个函数用来生成文件名，所有的文件名，存储在数组中
def file_path(file_dir):
    file_names = os.listdir(file_dir)
    if len(file_names):
        print('Succesfully read file names in dirctory of %s' % file_dir)
    else:
        ValueError('%s is a empty directory' % file_dir)
    filepath_list = []
    for filename in file_names:
        filepath = os.path.join(file_dir, filename)
        filepath_list.append(filepath)
    return filepath_list


# %%
def read_int16(bytestream):  # read 64 bytes,
    dt = np.dtype(np.int16).newbyteorder('<')  # 读取字节，更改字节位置
    return np.frombuffer(bytestream.read(64), dtype=dt)


# %%
# 读取二进制文件信息，并且丢弃前64个字节，即前32个int16
def read_file(filename, size_bytes=None):
    # read data of image ,and discard the first 32 int16 (64 bytes) 丢弃32个 int16数据
    # return a 1-D array
    # size_bytes = None:indicating read data until EOF
    with open(filename, 'rb') as bytestream:  # 二进制文件
        discard32int16 = read_int16(bytestream)  # discard the first 32 int16 (64 bytes) #读取64位。32个int16
        if len(discard32int16) != 32:
            ValueError('%s is a empty file' % filename)
        else:
            print('Successfully discard the first 32 int16 of %s' % filename)
        if size_bytes is None:  # read 'size_bytes'bytes in 'filename'
            size_bytes = -1  # size_bytes == -1 ,read until EOF is reached
        dt = np.dtype(np.int16).newbyteorder('<')
        data = np.frombuffer(bytestream.read(size_bytes), dtype=dt)
        if len(data) != 604800:  # the size of a image file is 604800 int16
            ValueError('The image has been damaged')
        else:
            print('Successfully read effective data of the image')
    return data


# %%
def save_image(ndarray, path, name):
    ndarray = ndarray.astype(np.uint8)  # transform  into np.uint8
    cv.imwrite(path + '{}.png'.format(name), ndarray)


# %%
def preprocess_image(file_dir, save_path, eachfilesizebytes=None):
    filepath = file_path(file_dir)
    names = os.listdir(file_dir)
    i = 0
    for filename in filepath:
        image_data = read_file(filename, eachfilesizebytes)
        image_data = image_data.reshape(-1, 120)
        image_data = np.transpose(image_data)

        image_data = image_data.astype(np.uint8)

        save_image(image_data, save_path, names[i])
        i += 1


# %%
if __name__ == '__main__':
    preprocess_image(r'F:\太阳射电爆识别\SpectrumCls\database\database\burst',
                     r'burst/')
    preprocess_image(r'F:\太阳射电爆识别\SpectrumCls\database\database\calibration',
                     r'calibration/')
    preprocess_image(r'F:\太阳射电爆识别\SpectrumCls\database\database\non_burst',
                     r'non_burst/')


#%%   test
image_data = read_file(r"F:\太阳射电爆识别\SpectrumCls\database\database\burst\20010101_1152959.NUS")
image_data = image_data.reshape(-1, 120)
image_data = np.transpose(image_data)
image_data = image_data.astype(np.uint8)
print(image_data)



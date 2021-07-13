# -*- coding = utf-8 -*-
# @Time : 2021/5/18 20:01
# @Author : 水神与月神
# @File : 加急调色的图片.py
# @Software : PyCharm

#%%
import os
import cv2
from color_transfer import color_transfer

#%%

def show_image(title, image, width=300):
    # resize图像以使得图像具有固定的大小，以便整个屏幕都可以展示
    r = width / float(image.shape[1])
    dim = (width, int(image.shape[0] * r))
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # 展示缩放后的图像
    cv2.imshow(title, resized)


path1 = r'C:\Users\dell\Desktop\888.png'
target_path = r'C:\Users\dell\Desktop\d'
save_path = r'C:\Users\dell\Desktop\c'
names = os.listdir(target_path)

for name in names:
    path2 = os.path.join(target_path, name)
    save = os.path.join(save_path, name)
    source = cv2.imread(path1)
    target = cv2.imread(path2)
    transfer = color_transfer(source, target)

    # r = transfer[:, :, 2]
    # g = transfer[:, :, 1]

    # r = cv2.equalizeHist(r)
    # g = cv2.equalizeHist(g)

    # transfer[:, :, 2] = r
    # transfer[:, :, 1] = g
    # 检测是否保存输出图像

    cv2.imwrite(save, transfer)

    # 展示图像
    # show_image("Source", source)
    # show_image("Target", target)
    # show_image("Transfer", transfer)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# 先变成灰度图片，然后，再进行上色
#%%
# 彩色图片变灰色

path = r'C:\Users\dell\Desktop\b'
save = r'C:\Users\dell\Desktop\a'
names = os.listdir(path)
for name in names:
    full_path = os.path.join(path, name)
    full_path2 = os.path.join(save,name)
    image = cv2.imread(full_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(full_path2, gray_image)


#%%
# 尝试将图片像素反转

path = r'C:\Users\dell\Desktop\a'
save = r'C:\Users\dell\Desktop\d'
names = os.listdir(path)
for name in names:
    full_path = os.path.join(path, name)
    full_path2 = os.path.join(save,name)
    gray = cv2.imread(full_path)
    gray_not = cv2.bitwise_not(gray)
    cv2.imwrite(full_path2, gray_not)

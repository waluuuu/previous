# -*- coding = utf-8 -*-
# @Time : 2021/5/5 23:16
# @Author : 水神与月神
# @File : 002.py
# @Software : PyCharm




# <p style="background-color:rgba(70,70,183,1)">
# <p style="background-color:rgba(250,156,127,1)">



rnum = 250 - 70
reach = rnum / 255
r = []
for i in range(0, 256):
    r.append(int(70 + reach * i))

gnum = 156 - 70
geach = gnum / 255
g = []
for i in range(0, 256):
    g.append(int(70 + geach * i))

bnum = 183 - 127
beach = bnum / 255
b = []
for i in range(0, 256):
    b.append(int(183 - beach * i))


all = []

for i in range(256):
    temp = []
    temp.append(r[i])
    temp.append(g[i])
    temp.append(b[i])

    all.append(temp)





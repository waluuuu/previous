# -*- coding = utf-8 -*-
# @Time : 2021/3/12 13:42
# @Author : 水神与月神
# @File : ttt.py
# @Software : PyCharm

# %%


from keras import models
from keras import layers
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# %%

model = models.Sequential()
# 卷积层，参数意义分别为：
# 经过这一层之后，特征图的个数，一个卷积核，产生一个特征图，第一层：32，说明有32个卷积核；第二层64，说明在第一层的特征图基础上，每张特征图有两个卷积核进行特征采集
# 卷积核大小
# 激活函数
# 输入大小（只在开始的第一层有，后面不需要）
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 400, 3)))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())


model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()  # 查看模型整体情况



# %%

# 配置模型的损失函数、优化器、指标名称


model.compile(loss='binary_crossentropy',  # 损失函数
              optimizer=optimizers.RMSprop(lr=1e-4),  # 优化器
              metrics=['acc'])  # 指标名称

# %%

# 图片的训练路径和验证路径
train_dir = r'G:\23\23\train'
validation_dir = r'G:\23\23\validation'

# %%

# 生成训练需要的图片和标签


# 将图片大小调整到1以内，原先图片每个像素的格式为uint8，所以要除以255
train_datagen = ImageDataGenerator(rescale=1. / 255)
validation_datagen = ImageDataGenerator(rescale=1. / 255)

# 根据目录的名称，生成对应的标签
# train_dir有Ⅱ型和Ⅲ型的图片
# 每次生成batch_size数量的图片，图片大小为target_size
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(200, 400),  # 生成图片的大小
    batch_size=20,  # 一次生成图片的数量
    class_mode='binary')  # 图片标签的类型

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(200, 400),  # 生成图片的大小
    batch_size=10,  # 一次生成图片的数量
    class_mode='binary')  # 图片标签的类型

# %%

# 开始训练
history = model.fit_generator(
    train_generator,  # 通过生成器传入图片和标签
    steps_per_epoch=20,  # 每轮要传入20次，即400张图片进行训练
    epochs=10,  # 总共训练30轮
    validation_data=validation_generator,  # 通过生成器传入图片和标签进行验证
    validation_steps=20)  # 每轮要传入20次，即200张图片进行验证

# %%

# 绘制训练精度、验证精度
# 绘制训练损失、验证损失
# python画图库，类似matlab的plot


acc = history.history['acc']  # 得到训练的指标数据
val_acc = history.history['val_acc']  # 得到验证的指标数据
loss = history.history['loss']  # 得到训练损失
val_loss = history.history['val_loss']  # 得到验证损失
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()  # 画图例
plt.figure()  # 另一张图
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()  # 画图，最后加上



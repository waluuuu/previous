# -*- coding = utf-8 -*-
# @Time : 2021/4/21 0:00
# @Author : 水神与月神
# @File : 001.py
# @Software : PyCharm


# %%

from keras import models
from keras import layers

# %%

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())  # 讲数据展开成1维
model.add(layers.Dropout(0.5))  # dropout使一半的神经元不工作
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

model.summary()  # 查看模型整体情况

# %%

from keras import optimizers

model.compile(loss='categorical_crossentropy',  # 损失函数
              optimizer=optimizers.RMSprop(lr=1e-4),  # 优化器
              metrics=['acc'])  # 指标名称

# %%

# 图片的训练路径和验证路径
train_dir = r'G:\Multiclassification\train'
validation_dir = r'G:\Multiclassification\validation'

# %%

# 生成训练需要的图片和标签
from keras.preprocessing.image import ImageDataGenerator

# 将图片大小调整到1以内，原先图片每个像素的格式为uint8，所以要除以255
train_datagen = ImageDataGenerator(rescale=1. / 255)
validation_datagen = ImageDataGenerator(rescale=1. / 255)

# 根据目录的名称，生成对应的标签
# train_dir有Ⅱ型和Ⅲ型的图片
# 每次生成batch_size数量的图片，图片大小为target_size
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),  # 生成图片的大小
    batch_size=150,  # 一次生成图片的数量
    class_mode='categorical')  # 图片标签的类型

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),  # 生成图片的大小
    batch_size=20,  # 一次生成图片的数量
    class_mode='categorical')  # 图片标签的类型

# %%

# 开始训练
history = model.fit_generator(
    train_generator,  # 通过生成器传入图片和标签
    steps_per_epoch=10,  # 每轮要传入10次，即1500张图片进行训练
    epochs=30,  # 总共训练30轮
    validation_data=validation_generator,  # 通过生成器传入图片和标签进行验证
    validation_steps=25)  # 每轮要传入10次，即300张图片进行验证

# %%

# 绘制训练精度、验证精度
# 绘制训练损失、验证损失
# python画图库，类似matlab的plot
import matplotlib.pyplot as plt

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

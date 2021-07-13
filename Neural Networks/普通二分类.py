# -*- coding = utf-8 -*-
# @Time : 2021/5/23 9:35
# @Author : 水神与月神
# @File : 支持向量机.py
# @Software : PyCharm


# 使用不同的数字图像处理方式，提取图片特征，然后分别进行二分类

# %%
from keras import models
from keras import layers

# %%

model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPool2D(2, 2))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

# %%

from keras import optimizers

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# %%

train_dir = r'F:\dogs-vs-cats\数据集\train'
val_dir = r'F:\dogs-vs-cats\数据集\validation'

# %%

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(200, 200),
    batch_size=20,
    class_mode='binary')

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(200, 200),
    batch_size=10,
    class_mode='binary'
)

# %% 变成同样大小的，有点问题，想用同样大小的处理，要先做出来

history = model.fit_generator(
    train_generator,
    steps_per_epoch=25,
    epochs=30,
    validation_data=val_generator,
    validation_steps=10
)

# %%

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


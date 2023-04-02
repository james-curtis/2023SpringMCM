import pandas as pd
import numpy as np

df = pd.read_excel('版本1_生成自然对数(Ln)变量_版本1_缺失值处理_Monohulled Sailboats_副本1.xlsx')
# df = pd.read_excel(r'原始数据_2023_MCM_Problem_Y_Boats.xlsx')
df = df.sample(frac=1).reset_index(drop=True)
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)
X = df
Y = df.pop('Q1-自然对数(Ln)_Listing Price (USD)_缺失值处理')  # 用实际的列名替换“列名”
Y = np.asarray(Y)

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 定义模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1024, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 编译模型
model.compile(optimizer='adam', loss='mse')

# 训练模型
history = model.fit(X, Y, epochs=1000, batch_size=100, validation_split=0.2)

# 可视化训练和测试误差
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
# plt.ylim([0, 10])
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()

# 预测并可视化结果
y_pred = model.predict(X)
plt.scatter(Y, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.axis('square')
# plt.xlim([9e4, 1e5])
# plt.ylim([9e4, 1e5])
_ = plt.plot([-1e10, 1e10], [-1e10, 1e10])
plt.show()

from sklearn.metrics import r2_score

print(r2_score(Y, y_pred))
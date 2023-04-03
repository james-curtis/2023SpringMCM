from sklearn.linear_model import *
from sklearn.model_selection import *
from sklearn.cross_decomposition import *
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import *
import os

df = pd.read_excel(r'E:\Programing\DataspellProjects\2023ICM-spring\T1\tensor-test\版本1_生成自然对数(Ln)变量_版本1_缺失值处理_Monohulled Sailboats_副本1.xlsx')
X = df
Y = df.pop('Q1-自然对数(Ln)_Listing Price (USD)_缺失值处理')


# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 创建 Ridge 模型，设置 alpha 值为 0.1
ridge = Ridge(alpha=0.1)

# 在训练集上训练模型
ridge.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = ridge.predict(X_test)

# 预测并可视化结果
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.axis('square')
# plt.xlim([9e4, 1e5])
# plt.ylim([9e4, 1e5])
_ = plt.plot([-1e10, 1e10], [-1e10, 1e10])


print(ridge.coef_)
# 计算均方误差
print(f'r2_score: {r2_score(y_test, y_pred)}')
print(f'mse: {mean_squared_error(y_test, y_pred)}')
print(f'mae: {mean_absolute_error(y_test, y_pred)}')
print(f'mape: {mean_absolute_percentage_error(y_test, y_pred)}')

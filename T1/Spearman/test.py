import numpy as np
import pandas as pd
from scipy.stats import spearmanr
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'


df = pd.read_excel(r'../数据预处理/xlsx/merged_file.xlsx')

# 计算Spearman相关系数及P值
corr_matrix, p_matrix = spearmanr(df)

# 绘制热力图（corr_matrix）
sns.set(style="white")
mask = np.zeros_like(corr_matrix, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(10, 8))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr_matrix, mask=mask, cmap=cmap, annot=True, annot_kws={"size": 10}, center=0, square=True, linewidths=.5,
            fmt=".2f",
            cbar_kws={"shrink": .5}, xticklabels=df.columns.values, yticklabels=df.columns.values)

# 绘制热力图（p_matrix）
sns.set(style="white")
mask = np.zeros_like(p_matrix, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(10, 8))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr_matrix, mask=mask, cmap=cmap, annot=True, annot_kws={"size": 10}, center=0, square=True, linewidths=.5,
            fmt=".2f",
            cbar_kws={"shrink": .5}, xticklabels=df.columns.values, yticklabels=df.columns.values)
plt.show()

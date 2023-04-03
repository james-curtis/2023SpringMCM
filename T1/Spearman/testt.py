import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# 画布设置
f, ax = plt.subplots(figsize=(6, 10))

# 绘图
sns.set_color_codes("pastel")  # 设置色调
sns.barplot(x="缺失比例", y="类别", data=data,
            label="缺失比例", color="b")
ax.legend(ncol=1, loc="lower right", frameon=True)  # 添加图例
ax.set(xlim=(0, 2), ylabel="")
plt.xlabel("数 据 缺 失 比 例（%）", fontsize=14)  # 调整横轴标题字体
sns.despine(left=True, bottom=True)  # 移除坐标轴的线

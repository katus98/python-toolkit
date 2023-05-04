import matplotlib.pyplot as plt

# 准备数据
filtering_magnitude_level = [1, 2, 3, 4, 5]
latency_ratio = [12.49, 39.37, 56.19, 64.25, 71.50]
average_latency = [2.642274488, 26.36506144, 60.2384895, 74.7569053, 91.11317215]

# 创建图形和轴对象
fig, ax1 = plt.subplots()

# 绘制第一条曲线和标记数据点
color = 'tab:red'
ax1.set_xlabel('Filtering Magnitude Level')
ax1.set_ylabel('Latency Ratio (%)', color=color)
ax1.plot(filtering_magnitude_level, latency_ratio, 'o-', color=color, label='Latency Ratio')
ax1.tick_params(axis='y', labelcolor=color)
for x, y in zip(filtering_magnitude_level, latency_ratio):
    ax1.annotate(f'{y:.2f}%', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

# 创建第二个纵坐标轴对象
ax2 = ax1.twinx()

# 绘制第二条曲线和标记数据点
color = 'tab:blue'
ax2.set_ylabel('Average Latency (s)', color=color)
ax2.plot(filtering_magnitude_level, average_latency, 's-', color=color, label='Average Latency')
ax2.tick_params(axis='y', labelcolor=color)
for x, y in zip(filtering_magnitude_level, average_latency):
    ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(20, -5), ha='center')

# 添加标题和图例
# plt.title('Latency vs. Filtering Magnitude Level')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax1.legend(lines, labels, loc='upper left')

# 显示图形
plt.show()

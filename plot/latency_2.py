import matplotlib.pyplot as plt

# 准备数据
filtering_magnitude_level = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
latency_ratio = [52.10, 61.87, 72.42, 76.60, 78.67, 79.50, 79.83, 80.01, 80.13, 80.19]
average_latency = [4.17041744, 5.836840548, 8.074337544, 8.97834728, 9.445875432, 9.6591705, 9.813374172, 9.835501284,
                   9.907521603, 9.914940189]
matching_point_accuracy = [77.22, 80.50, 84.43, 84.67, 84.80, 85.05, 85.12, 85.08, 85.07, 85.10]

# 创建图形和轴对象
fig, ax1 = plt.subplots()

# 绘制第一条曲线和标记数据点
color = 'tab:red'
ax1.set_xlabel('Filtering Magnitude Level')
ax1.set_ylabel('Latency Ratio (%)', color=color)
ax1.plot(filtering_magnitude_level, latency_ratio, 'o-', color=color, label='Latency Ratio')
ax1.tick_params(axis='y', labelcolor=color)
for x, y in zip(filtering_magnitude_level, latency_ratio):
    ax1.annotate(f'{y:.2f}%', (x, y), textcoords="offset points", xytext=(-15, 5), ha='center')

# 创建第二个纵坐标轴对象
ax2 = ax1.twinx()

# 绘制第二条曲线和标记数据点
color = 'tab:blue'
ax2.set_ylabel('Average Latency (s)', color=color)
ax2.plot(filtering_magnitude_level, average_latency, 's-', color=color, label='Average Latency')
ax2.tick_params(axis='y', labelcolor=color)
for x, y in zip(filtering_magnitude_level, average_latency):
    ax2.annotate(f'{y:.2f}', (x, y), textcoords="offset points", xytext=(15, 5), ha='center')

# 创建第三个纵坐标轴对象
ax3 = ax1.twinx()

# 将第三个纵坐标轴移动到图形的右侧
ax3.spines["right"].set_position(("axes", 1.05))

# 绘制第三条曲线和标记数据点
color = 'tab:green'
ax3.set_ylabel('Matching Point Accuracy (%)', color=color)
ax3.plot(filtering_magnitude_level, matching_point_accuracy, '^-', color=color, label='Matching Point Accuracy')
ax3.tick_params(axis='y', labelcolor=color)
for x, y in zip(filtering_magnitude_level, matching_point_accuracy):
    ax3.annotate(f'{y:.2f}%', (x, y), textcoords="offset points", xytext=(0, 5), ha='center')

# 将图例设置在图表内左上角
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines = lines1 + lines2 + lines3
labels = labels1 + labels2 + labels3
ax1.legend(lines, labels, loc='upper left')

# 显示图形
plt.show()

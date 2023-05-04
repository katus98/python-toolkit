import matplotlib.pyplot as plt

# 数据
x = [i for i in range(1, 31)]
y1 = [57537, 101269, 135022, 168883, 199209, 224091, 252730, 288054, 322820, 366889,
      408525, 460713, 506625, 549882, 594965, 626792, 682244, 734068, 765944, 808280,
      847648, 891882, 941539, 987804, 1033847, 1077478, 1122210, 1166992, 1206043, 1247058]
y2 = [5.27, 8.59, 11.5, 14.5, 17.1, 19.7, 22.4, 25.4, 28.4, 32.3,
      35.9, 39.8, 42.8, 47.6, 51.5, 55.2, 59.3, 62.7, 66.3, 70.1,
      73.4, 77.3, 81.6, 85.6, 89.6, 93.3, 97.3, 101, 105, 108]

# 创建画布和子图对象
fig, ax1 = plt.subplots()

# 绘制曲线
color = 'tab:red'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Matching Quantity')
ax1.plot(x, y1, color=color, marker='o', label='Matching Quantity')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Amount of GPS trajectory point data consumed (KB)')
ax2.plot(x, y2, color=color, marker='s', label='Amount of GPS trajectory point data consumed')
ax2.tick_params(axis='y', labelcolor=color)

# 设置图例位置
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 添加网格线
# ax1.grid(True)

# 显示图表
plt.show()

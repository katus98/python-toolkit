import matplotlib.pyplot as plt

# 数据
degree_of_parallelism = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
real_time_processing_throughput_items = [173.2108731, 389.2291105, 512.1461029, 673.7406542, 1089.710443, 1309.286693, 1441.006693, 1600.289308, 2233.598693, 2067.211511, 2507.483691, 2757.156373, 2971.034014, 3332.691004, 3285.926582, 3294.893151, 3965.061493, 4122.158307, 3927.281943, 3624.833333, 4223.913882, 3506.378066, 4256.899522, 4732.903821]
real_time_processing_throughput_kb = [15.40217463, 34.5933513, 45.56137583, 59.69345794, 96.56708861, 116.2270059, 127.7601071, 141.6855346, 198.1071895, 182.6992806, 222.359739, 244.8988173, 263.3142857, 295.0508475, 291.2135021, 291.769863, 350.8286969, 364.338558, 348.1816262, 321.4883721, 373.7994859, 310.3030303, 375.6299841, 419.5836627]

# 绘图
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# 绘制Real-time Processing Throughput (items/s)
ax1.plot(degree_of_parallelism, real_time_processing_throughput_items, 'bo-', label='Real-time Processing Throughput (items/s)')
ax1.set_xlabel('Degree of Parallelism')
ax1.set_ylabel('Real-time Processing Throughput (items/s)')

# 绘制Real-time Processing Throughput (KB/s)
ax2.plot(degree_of_parallelism, real_time_processing_throughput_kb, 'go-', label='Real-time Processing Throughput (KB/s)')
ax2.set_ylabel('Real-time Processing Throughput (KB/s)')

# 图例设置在图表内左上角
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines = lines1 + lines2
labels = labels1 + labels2
ax1.legend(lines, labels, loc='upper left')

plt.show()

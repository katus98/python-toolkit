"""
@:filename random-region.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2021-01-13
"""
import random

if __name__ == '__main__':
    # region_range = [-74.275, -73.7347, 40.49167, 40.91945]   # 45.93, 47.48
    region_range = [2899872.74, 20037508.34, 141016.18, 14218719.91]
    time_range = [1388505600000, 1451577599000]
    factor_ranges = [(0.0001, 0.0005), (0.0005, 0.001), (0.001, 0.005), (0.005, 0.01), (0.01, 0.05), (0.05, 0.1)]
    number = 50000
    filename = r'D:\Data\regions2-50000.tsv'
    file = open(filename, 'w')
    i = 0
    for factor_range in factor_ranges:
        i += 1
        for n in range(number):
            factor = [random.uniform(factor_range[0], factor_range[1]),
                      random.uniform(factor_range[0], factor_range[1]),
                      random.uniform(factor_range[0], factor_range[1])]
            interval = [(region_range[1] - region_range[0]) * factor[0],
                        (region_range[3] - region_range[2]) * factor[1],
                        (time_range[1] - time_range[0]) * factor[2]]
            start = [random.uniform(region_range[0], region_range[1] - interval[0]),
                     random.uniform(region_range[2], region_range[3] - interval[1]),
                     random.randint(time_range[0], int(time_range[1] - interval[2]))]
            ps = [(str(start[0]), str(start[1])), (str(start[0] + interval[0]), str(start[1])),
                  (str(start[0] + interval[0]), str(start[1] + interval[1])),
                  (str(start[0]), str(start[1] + interval[1]))]
            wkt = 'POLYGON (('
            for j in range(4):
                wkt += ps[j][0] + ' ' + ps[j][1] + ','
            wkt += ps[0][0] + ' ' + ps[0][1] + '))'
            line = str(i) + '\t' + str(n) + '\t' + wkt + '\t' + str(start[2]) + '\t' + str(start[2] + int(interval[2])) + '\n'
            file.writelines(line)
    file.close()

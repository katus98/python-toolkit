import random

if __name__ == '__main__':
    # region_range = [-74.275, -73.7347, 40.49167, 40.91945]   # 45.93, 47.48
    region_range = [2899872.74, 20037508.34, 141016.18, 14218719.91]
    time_range = [1388505600000, 1451577599000]
    number = 1000
    filename = r'D:\Data\points2.tsv'
    file = open(filename, 'w')
    for n in range(number):
        point = [random.uniform(region_range[0], region_range[1]),
                 random.uniform(region_range[2], region_range[3]),
                 random.randint(time_range[0], time_range[1])]
        line = str(n) + '\t' + str(point[0]) + '\t' + str(point[1]) + '\t' + str(point[2]) + '\n'
        file.writelines(line)
    file.close()

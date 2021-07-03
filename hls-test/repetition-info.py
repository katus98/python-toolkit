"""
@:filename repetition-info.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2021-01-27
"""
import TrajectoryNode as tN

if __name__ == '__main__':
    filename = r'D:\Data\hls-test\repetition_final\data_ratio-0.05_max-10_ord.csv'
    lst = []
    dictT, dictX, dictY = dict(), dict(), dict()
    with open(filename, 'r') as file:
        for line in file:
            node = tN.TrajectoryNode(line)
            lst.append(node)
            dictT[node.timestamp] = dictT.get(node.timestamp, 0) + 1
            dictX[node.x] = dictX.get(node.x, 0) + 1
            dictY[node.y] = dictY.get(node.y, 0) + 1
    print('T repetition ratio:', 1 - (len(dictT) / len(lst)))
    print('T repetition max:', max(dictT.values()))
    print('X repetition ratio:', 1 - (len(dictX) / len(lst)))
    print('X repetition max:', max(dictX.values()))
    print('Y repetition ratio:', 1 - (len(dictY) / len(lst)))
    print('Y repetition max:', max(dictY.values()))

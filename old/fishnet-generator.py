if __name__ == '__main__':
    file_polygon = r'D:\Data\polygon.csv'
    file_linestring = r'D:\Data\linestring.csv'
    extent = [73.62, 134.77, 16.7, 53.56]
    pieces = [10, 6]
    buffer_error = 0.01
    interval = [(extent[1] - extent[0] + buffer_error) / pieces[0], (extent[3] - extent[2] + buffer_error) / pieces[1]]
    print('interval:', interval)
    points = {}
    for i in range(pieces[0] + 1):
        x = extent[0] - buffer_error / 2 + i * interval[0]
        for j in range(pieces[1] + 1):
            y = extent[2] - buffer_error / 2 + j * interval[1]
            points[(i, j)] = (round(x, 3), round(y, 3))
    polygons = []
    lines = []
    for i in range(pieces[0]):
        for j in range(pieces[1]):
            ps = []
            p1 = points.get((i, j))
            ps.append((str(p1[0]), str(p1[1])))
            p2 = points.get((i + 1, j))
            ps.append((str(p2[0]), str(p2[1])))
            p3 = points.get((i + 1, j + 1))
            ps.append((str(p3[0]), str(p3[1])))
            p4 = points.get((i, j + 1))
            ps.append((str(p4[0]), str(p4[1])))
            cors = ''
            for ele in ps:
                cors += ele[0] + ' ' + ele[1] + ','
            cors += ps[0][0] + ' ' + ps[0][1]
            polygons.append(str(i * pieces[1] + j) + '\tPOLYGON ((' + cors + '))\n')
            lines.append(str(i * pieces[1] + j) + '\tLINESTRING (' + cors + ')\n')
    # for i in range(pieces[0] + 1):
    #     line = 'LINESTRING ('
    #     line += str(points[(i, 0)][0]) + ' ' + str(points[(i, 0)][1]) + ','
    #     line += str(points[(i, pieces[1])][0]) + ' ' + str(points[(i, pieces[1])][1]) + ')\n'
    #     lines.append(line)
    # for j in range(pieces[1] + 1):
    #     line = 'LINESTRING ('
    #     line += str(points[(0, j)][0]) + ' ' + str(points[(0, j)][1]) + ','
    #     line += str(points[(pieces[0], j)][0]) + ' ' + str(points[(pieces[0], j)][1]) + ')\n'
    #     lines.append(line)
    file1 = open(file_polygon, 'w')
    file1.writelines(polygons)
    file1.close()
    file2 = open(file_linestring, 'w')
    file2.writelines(lines)
    file2.close()
    print("All Finished!")

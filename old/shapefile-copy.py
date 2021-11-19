import shapefile as shp
import math
import utils.process as pr

if __name__ == '__main__':
    # Set the parameter
    # 数据路径
    oriFilename = r'F:\data\gis\cky\sm\sm.shp'
    desFilename = r'F:\data\gis\cky\result\polygon4test2.shp'
    # 输出数据覆盖范围
    corRange = {'x1': -180.0, 'x2': 180.0, 'y1': -90.0, 'y2': 90.0}
    # 复制行列数
    numRange = {'x': 20, 'y': 10}
    # 复制缩放系数
    xScale, yScale = 60, 56

    # Generate other parameter
    oriShp = shp.Reader(oriFilename)
    # 原始数据跨度
    xr = math.floor((oriShp.bbox[2] - oriShp.bbox[0]) * 10000 + 1) / 10000
    yr = math.floor((oriShp.bbox[3] - oriShp.bbox[1]) * 10000 + 1) / 10000
    print(xr, yr)
    # print(int((corRange.get('x2') - corRange.get('x1')) / xr), int((corRange.get('y2') - corRange.get('y1')) / yr))
    # 输出数据单块跨度
    deltaX = (corRange.get('x2') - corRange.get('x1')) / numRange.get('x')
    deltaY = (corRange.get('y2') - corRange.get('y1')) / numRange.get('y')
    print(deltaX, deltaY)

    # Processing
    print('Processing...')
    desShp = shp.Writer(desFilename)
    desShp.fields = oriShp.fields[1:]
    for i in range(numRange.get('x')):
        for j in range(numRange.get('y')):
            for w in range(len(oriShp)):
                newShape = oriShp.shape(w)
                points = oriShp.shape(w).points
                for p in range(len(points)):
                    points[p] = ((points[p][0] - oriShp.bbox[0]) * xScale + i * deltaX + corRange.get('x1'),
                                 (points[p][1] - oriShp.bbox[1]) * yScale + j * deltaY + corRange.get('y1'))
                newShape.points = points
                desShp.shape(newShape)
                desShp.record(*oriShp.record(w))
            pr.process_bar((i * numRange.get('y') + j + 1) / (numRange.get('x') * numRange.get('y')),
                           start_str='', end_str='100.0%', total_length=100)
    desShp.close()
    print('\nAll finished!')

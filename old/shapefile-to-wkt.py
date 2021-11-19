from osgeo import ogr

if __name__ == '__main__':
    shapefiles = [r'F:\data\gis\cky\result\polygon4test1.shp', r'F:\data\gis\cky\result\polygon4test2.shp']
    out_filename = r'F:\data\gis\cky\result\polygon4test.tsv'
    out_file = open(out_filename, 'w')
    count = 0
    driver = ogr.GetDriverByName('ESRI Shapefile')
    for shapefile in shapefiles:
        dataSource = driver.Open(shapefile, 0)
        layer = dataSource.GetLayer()

        layerDefinition = layer.GetLayerDefn()
        # 获取字段名称列表
        fields = []
        for i in range(layerDefinition.GetFieldCount()):
            fields.append(layerDefinition.GetFieldDefn(i).GetName())
        print(fields)

        # 获取字段值和相应的几何
        for feature in layer:
            BSM = feature.GetField('BSM')
            YSDM = feature.GetField('YSDM')
            TBYBH = feature.GetField('TBYBH')
            TBBH = feature.GetField('TBBH')
            DLBM = feature.GetField('DLBM')
            DLMC = feature.GetField('DLMC')
            QSXZ = feature.GetField('QSXZ')
            QSDWMC = feature.GetField('QSDWMC')
            GDPDJ = feature.GetField('GDPDJ')
            TBMJ = feature.GetField('TBMJ')
            XZDWMJ = feature.GetField('XZDWMJ')
            AREA = feature.GetField('AREA')
            geom = feature.GetGeometryRef()
            geomwkt = geom.ExportToWkt()
            out_file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (
            BSM, YSDM, TBYBH, TBBH, DLBM, DLMC, QSXZ, QSDWMC, GDPDJ, TBMJ, XZDWMJ, AREA, geomwkt))
            count += 1
            if count % 10000 == 0:
                print(count)
    out_file.close()
    print(count)

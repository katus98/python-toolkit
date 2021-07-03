"""
@:filename info_table.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2021-02-04
"""

if __name__ == '__main__':
    table_create_sql = """DROP TABLE IF EXISTS range_test;
CREATE TABLE range_test(
    index_name ENUM('STR-Tree', 'STR*-Tree', 'QuadTree', 'KdTree'),   -- 索引名称
    data_size BIGINT,   -- 数据量
    space_dimension SMALLINT,   -- 数据空间维度
    has_time BOOLEAN,   -- 是否具有时间
    range_level INT,   -- 测试框大小级别
    range_id INT,   -- 测试框所在级别的ID
    query_time BIGINT,   -- 查询时间
    result_size BIGINT   -- 查询结果数量
);
DROP TABLE IF EXISTS knn_test;
CREATE TABLE knn_test(
    index_name ENUM('STR-Tree', 'STR*-Tree', 'QuadTree', 'KdTree'),   -- 索引名称
    data_size BIGINT,   -- 数据量
    space_dimension SMALLINT,   -- 数据空间维度
    has_time BOOLEAN,   -- 是否具有时间
    point_id INT,   -- 测试点ID
    knn_number INT,   -- 最邻近查询个数
    query_time BIGINT,   -- 查询时间
    result_size BIGINT   -- 查询结果数量
);
"""
    output_filename = r'D:\Data\hls-test\testT-ns.sql'
    base_dir = r'D:\Data\hls-test\results-ns\t'
    # result_names = ['point', 'tpoint', 'line', 'tline', 'polygon']
    result_names = ['point', 'line']
    level_max = 11
    data_sizes = [10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]
    # space_dimensions = ['0', '0', '1', '1', '2']
    space_dimensions = ['0', '1']
    # has_times = ['false', 'true', 'false', 'true', 'false']
    has_times = ['true', 'true']
    base_insert_sql = ["INSERT INTO range_test(index_name, data_size, space_dimension, has_time, range_level," +
                       " range_id, query_time, result_size) VALUES('{}', {}, {}, {}, {}, {}, {}, {});\n",
                       "INSERT INTO knn_test(index_name, data_size, space_dimension, has_time, point_id," +
                       " knn_number, query_time, result_size) VALUES('{}', {}, {}, {}, {}, {}, {}, {});\n"]
    output_file = open(output_filename, 'w')
    # output_file.write(table_create_sql)
    for i in range(len(result_names)):
        for size_level in range(level_max):
            filename = base_dir + result_names[i] + str(size_level+1) + '.txt'
            file = open(filename, 'r')
            lines = file.readlines()
            file.close()
            # str_lines1 = lines[6:6006]
            # for line in str_lines1:
            #     items = line[:-1].split(',')
            #     insert_sql = base_insert_sql[0].format('STR-Tree', data_sizes[size_level], space_dimensions[i],
            #                                            has_times[i], items[0], items[1], items[2], items[3])
            #     output_file.write(insert_sql)
            # str_lines2 = lines[6008:9008]
            # for line in str_lines2:
            #     items = line[:-1].split(',')
            #     insert_sql = base_insert_sql[1].format('STR-Tree', data_sizes[size_level], space_dimensions[i],
            #                                            has_times[i], items[0], items[1], items[2], items[3])
            #     output_file.write(insert_sql)
            # str_star_lines1 = lines[9013:15013]
            # for line in str_star_lines1:
            #     items = line[:-1].split(',')
            #     insert_sql = base_insert_sql[0].format('STR*-Tree', data_sizes[size_level], space_dimensions[i],
            #                                            has_times[i], items[0], items[1], items[2], items[3])
            #     output_file.write(insert_sql)
            # str_star_lines2 = lines[15015:18015]
            # for line in str_star_lines2:
            #     items = line[:-1].split(',')
            #     insert_sql = base_insert_sql[1].format('STR*-Tree', data_sizes[size_level], space_dimensions[i],
            #                                            has_times[i], items[0], items[1], items[2], items[3])
            #     output_file.write(insert_sql)
            # quad_lines1 = lines[18020:24020]
            quad_lines1 = lines[6:6006]
            for line in quad_lines1:
                items = line[:-1].split(',')
                insert_sql = base_insert_sql[0].format('QuadTree', data_sizes[size_level], space_dimensions[i],
                                                       has_times[i], items[0], items[1], items[2], items[3])
                output_file.write(insert_sql)
            # quad_lines2 = lines[24022:27022]
            quad_lines2 = lines[6008:9008]
            for line in quad_lines2:
                items = line[:-1].split(',')
                insert_sql = base_insert_sql[1].format('QuadTree', data_sizes[size_level], space_dimensions[i],
                                                       has_times[i], items[0], items[1], items[2], items[3])
                output_file.write(insert_sql)
            if i < 1:
                # kd_lines1 = lines[27027:33027]
                kd_lines1 = lines[9013:15013]
                for line in kd_lines1:
                    items = line[:-1].split(',')
                    insert_sql = base_insert_sql[0].format('KdTree', data_sizes[size_level], space_dimensions[i],
                                                           has_times[i], items[0], items[1], items[2], items[3])
                    output_file.write(insert_sql)
                # kd_lines2 = lines[33029:36029]
                kd_lines2 = lines[15015:18015]
                for line in kd_lines2:
                    items = line[:-1].split(',')
                    insert_sql = base_insert_sql[1].format('KdTree', data_sizes[size_level], space_dimensions[i],
                                                           has_times[i], items[0], items[1], items[2], items[3])
                    output_file.write(insert_sql)
    output_file.close()

import os


def main():
    table_create_sql = """
DROP TABLE IF EXISTS basic_info;
CREATE TABLE basic_info(
    index_name ENUM('STR-Tree', 'STR*-Tree', 'Quad-Tree', 'KdTree'),   -- 索引名称
    data_size BIGINT,   -- 数据量
    space_dimension SMALLINT,   -- 数据空间维度
    has_time BOOLEAN,   -- 是否具有时间
    build_time BIGINT,   -- 索引构建时间(微秒)
    space_size BIGINT,   -- 索引占用空间
    remark VARCHAR(10)   -- 备注
);
DROP TABLE IF EXISTS range_test;
CREATE TABLE range_test(
    index_name ENUM('STR-Tree', 'STR*-Tree', 'Quad-Tree', 'KdTree'),   -- 索引名称
    data_size BIGINT,   -- 数据量
    space_dimension SMALLINT,   -- 数据空间维度
    has_time BOOLEAN,   -- 是否具有时间
    range_level INT,   -- 测试框大小级别
    range_id INT,   -- 测试框所在级别的ID
    query_time BIGINT,   -- 查询时间
    result_size BIGINT,   -- 查询结果数量
    remark VARCHAR(10)   -- 备注
);
DROP TABLE IF EXISTS knn_test;
CREATE TABLE knn_test(
    index_name ENUM('STR-Tree', 'STR*-Tree', 'Quad-Tree', 'KdTree'),   -- 索引名称
    data_size BIGINT,   -- 数据量
    space_dimension SMALLINT,   -- 数据空间维度
    has_time BOOLEAN,   -- 是否具有时间
    point_id INT,   -- 测试点ID
    knn_number INT,   -- 最邻近查询个数
    query_time BIGINT,   -- 查询时间
    result_size BIGINT,   -- 查询结果数量
    remark VARCHAR(10)   -- 备注
);
"""
    output_filename = r'D:\Data\hls-test\result50000-ns.sql'
    base_dir = r'D:\Data\hls-test\result50000-ns'
    result_names = [r'\point', r'\spoint', r'\stpoint', r'\sline', r'\stline', r'\spolygon']
    level_max = 11
    # data_sizes = [10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000]
    space_dimensions = ['-1', '0', '0', '1', '1', '2']
    has_times = ['true', 'false', 'true', 'false', 'true', 'false']
    base_insert_sql = [
        "INSERT INTO basic_info(index_name, data_size, space_dimension, has_time, build_time, space_size, remark) VALUES('{}', {}, {}, {}, {}, {}, '{}');\n",
        "INSERT INTO range_test(index_name, data_size, space_dimension, has_time, range_level, range_id, query_time, result_size, remark) VALUES('{}', {}, {}, {}, {}, {}, {}, {}, '{}');\n",
        "INSERT INTO knn_test(index_name, data_size, space_dimension, has_time, point_id, knn_number, query_time, result_size, remark) VALUES('{}', {}, {}, {}, {}, {}, {}, {}, '{}');\n"
    ]
    output_file = open(output_filename, 'w')
    output_file.write(table_create_sql)
    for i in range(len(result_names)):
        for size_level in range(level_max):
            filename = base_dir + result_names[i] + str(size_level + 1) + '.txt'
            if os.path.exists(filename):
                file = open(filename, 'r')
                lines = file.readlines()
                file.close()
                index_name = ''
                build_time = 0
                space_size = 0
                data_size = 0
                space_dimension = -1
                has_time = 'false'
                base_sql_index = 0
                remark = ''
                for line in lines:
                    if 'Total Data Size' in line:
                        data_size = int(line[line.index(':')+2:-1])
                        space_dimension = space_dimensions[i]
                        has_time = has_times[i]
                        continue
                    if ' =========== ' in line:
                        if i == 0:
                            index_name = line[13:len(line)-15]
                            remark = line[14+len(index_name):len(line)-13]
                            if remark == 't':
                                has_time = 'true'
                                space_dimension = -1
                            else:
                                has_time = 'false'
                                space_dimension = 0
                        else:
                            index_name = line[13:len(line)-13]
                            remark = ''
                        continue
                    if 'Time:' in line:
                        build_time = int(line[line.index(':')+2:-1])
                        continue
                    if 'Size:' in line:
                        space_size = int(line[line.index(':')+2:-1])
                        if i == 0:
                            output_file.write(base_insert_sql[0].format(index_name, data_size, space_dimension, has_time, build_time, space_size, remark))
                        else:
                            output_file.write(base_insert_sql[0].format(index_name, data_size, space_dimension, has_time, build_time, space_size, ''))
                        continue
                    if 'Range Search Test' in line:
                        base_sql_index = 1
                        if i != 0:
                            remark = line.split(' ')[0]
                        continue
                    if 'KNN Search Test' in line:
                        base_sql_index = 2
                        if i != 0:
                            remark = line.split(' ')[0]
                        continue
                    if 'resultSize' in line:
                        continue
                    items = line[:-1].split(',')
                    insert_sql = base_insert_sql[base_sql_index].format(index_name, data_size, space_dimension, has_time, items[0], items[1], items[2], items[3], remark)
                    output_file.write(insert_sql)
                print(filename + " finished!")
    output_file.close()


if __name__ == '__main__':
    main()

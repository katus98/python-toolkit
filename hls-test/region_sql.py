"""
@:filename region_sql.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2021-01-25
"""

if __name__ == '__main__':
    input_filename = r'D:\Data\hls-test\regions.tsv'
    output_filename = r'D:\Data\hls-test\regions.sql'
    output_file = open(output_filename, 'w')
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            items = line[:-1].split('\t')
            new_line = "INSERT INTO region1(level, id, wkt, start_time, end_time) VALUES ({}, {}, '{}', {}, {});\n"\
                .format(items[0], items[1], items[2], items[3], items[4])
            output_file.write(new_line)
    output_file.close()

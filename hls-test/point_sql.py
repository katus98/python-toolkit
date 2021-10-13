if __name__ == '__main__':
    input_filename = r'D:\Data\hls-test\points.tsv'
    output_filename = r'D:\Data\hls-test\points.sql'
    output_file = open(output_filename, 'w')
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            items = line[:-1].split('\t')
            new_line = "INSERT INTO point1(id, x, y, time) VALUES ({}, {}, {}, {});\n" \
                .format(items[0], items[1], items[2], items[3])
            output_file.write(new_line)
    output_file.close()

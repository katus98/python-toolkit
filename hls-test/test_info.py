if __name__ == '__main__':
    output_filename = r'D:\Data\hls-test\infoT-ns.txt'
    base_dir = r'D:\Data\hls-test\results-ns\t'
    # result_names = ['point', 'tpoint', 'line', 'tline', 'polygon']
    result_names = ['point', 'line']
    level_max = 11
    output_file = open(output_filename, 'w')
    for name in result_names:
        for i in range(1, level_max + 1):
            filename = base_dir + name + str(i) + '.txt'
            file = open(filename, 'r')
            lines = file.readlines()
            output_file.write(filename + '\n')
            for line in lines:
                if ':' in line:
                    output_file.write(line)
            output_file.write('\n')
    output_file.close()

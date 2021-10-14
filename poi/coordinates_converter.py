import json
import multiprocessing as mp
import urllib.request
import utils.file_tool as fm

num_pro = int(mp.cpu_count())


def coordinates_cov():
    global num_pro
    base_filename = r'data\poi\poi_info_'
    data_set = set()
    for i in range(16):
        filename = base_filename + str(i) + '.tsv'
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                data_set.add('\t'.join(line[:-1].split('\t')[1:]))
    all_data_list = list(data_set)
    size, interval = len(data_set), len(data_set) // num_pro
    start, end = 0, 0
    pool = mp.Pool()
    for processor_index in range(num_pro):
        start = end
        if processor_index == num_pro - 1:
            end = size
        else:
            end += interval
        pool.apply_async(single_cov, args=([processor_index, all_data_list[start: end]]))
    pool.close()
    pool.join()


def single_cov(processor_index, data_list):
    print('Processor ' + str(processor_index) + ' started!')
    count = 0
    output_filename = r'data\poi\poi_info_cov-' + str(processor_index) + '.tsv'
    output_file = open(output_filename, 'a', encoding='UTF-8')
    for data in data_list:
        items = data.split('\t')
        items[4].split(';')
        url = 'https://api.map.baidu.com/geoconv/v1/?coords={},{}&from=6&to=5&ak=FjTG88NYVp3wbNqq4KdR0KNE8DrgsEnd'.format(
            float(items[6]) / 100.0, float(items[7]) / 100.0)
        pos = json.load(urllib.request.urlopen(url))
        if pos['status'] == 0:
            x, y = pos['result'][0]['x'], pos['result'][0]['y']
        else:
            continue
        types = ['', '']
        temp = items[4].split(';')
        if len(temp) >= 2:
            types = temp[:2]
        elif len(temp) == 1:
            types[0] = temp[0]
        line_list = items[:4] + types[:2] + items[5:]
        line_list.append(str(x))
        line_list.append(str(y))
        line = '\t'.join(line_list) + '\n'
        output_file.write(line)
        count += 1
        output_file.flush()
        print('Processor ' + str(processor_index) + ' finished ' + str(count) + ' lines!')
    output_file.close()
    print('Processor ' + str(processor_index) + ' all finished!')


def convert_to_sql():
    global num_pro
    base_sql = "INSERT INTO hn_poi(name, address, area_name, di_tag, kind, type, phone, x, y, lon, lat) VALUES (" \
               "'{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {})"
    output = r'data\poi\poi_info_cov-final.sql'
    o_file = open(output, 'w', encoding='UTF-8')
    for index in range(num_pro):
        filename = r'data\poi\poi_info_cov-' + str(index) + '.tsv'
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                items = line[:-1].split("\t")
                n_line = base_sql.format(items[0], items[1], items[2], items[3], items[4], items[5], items[6], items[7],
                                         items[8], items[9], items[10])
                o_file.write(n_line + '\n')
    o_file.flush()
    o_file.close()


if __name__ == '__main__':
    coordinates_cov()
    filenames = []
    for i in range(num_pro):
        filenames.append(r'data\poi\poi_info_cov-' + str(i) + '.tsv')
    output_filename = r'data\poi\poi_info_cov-final.tsv'
    fm.merge_files(filenames, output_filename)

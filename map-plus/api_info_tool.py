import json
import urllib.request


def main():
    file = open(r'F:\data\form\mp.tsv', 'w', encoding='UTF-8')
    list_url = 'https://mt.mapplus.cn/v1.0/product/?order_by=name'
    request = urllib.request.Request(list_url)
    page = urllib.request.urlopen(request)
    list_json = json.load(page)
    file.write('guid\tproduct_name\ttime\tread_level\tstate\tcomposite1\tcomposite2\tlayer_num\t' +
               '1layer_name\t1tile_format\t1ratio\t1storage\t1file_format\t1min_z\t1max_z\t1tile_range_p1y\t1tile_range_p1x\t1tile_range_p2y\t1tile_range_p2x\t' +
               '2layer_name\t2tile_format\t2ratio\t2storage\t2file_format\t2min_z\t2max_z\t2tile_range_p1y\t2tile_range_p1x\t2tile_range_p2y\t2tile_range_p2x\n')
    for data in list_json['data']:
        line_ls = []
        line_ls.append(str(data['guid']))
        line_ls.append(str(data['product_name']))
        line_ls.append(str(data['time']))
        line_ls.append(str(data['read_level']))
        line_ls.append(str(data['state']))
        line_ls.append(str(data['composite'][0]))
        line_ls.append(str(data['composite'][1]))
        line_ls.append(str(len(data['layers'])))
        for layer in data['layers']:
            line_ls.append(str(layer['layer_name']))
            line_ls.append(str(layer['tile_format']))
            line_ls.append(str(layer['ratio']))
            line_ls.append(str(layer['storage']))
            line_ls.append(str(layer['file_format']))
            line_ls.append(str(layer['min_z']))
            line_ls.append(str(layer['max_z']))
            line_ls.append(str(layer['tile_range'][0][0]))
            line_ls.append(str(layer['tile_range'][0][0]))
            line_ls.append(str(layer['tile_range'][1][1]))
            line_ls.append(str(layer['tile_range'][1][1]))
        num = (2 - len(data['layers'])) * 11
        for i in range(num):
            line_ls.append('')
        file.write('\t'.join(line_ls) + '\n')
    file.close()


if __name__ == '__main__':
    main()

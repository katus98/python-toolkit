import json
import urllib
import urllib.request
import multiprocessing as mp

import poi.poi_keywords


def content_to_str(content, poi_type):
    str_ls = []
    x, y = float(content['diPointX']), float(content['diPointY'])
    tel = ''
    if 'tel' in content:
        tel = content['tel']
    str_ls.append(poi_type)
    str_ls.append(content['name'])
    str_ls.append(content['addr'])
    str_ls.append(content['area_name'])
    str_ls.append(content['di_tag'])
    str_ls.append(content['std_tag'])
    str_ls.append(tel)
    str_ls.append(str(x))
    str_ls.append(str(y))
    return '\t'.join(item for item in str_ls) + '\n'


def download_poi():
    types = ['car', 'catering', 'entertainment', 'traffic']
    pool = mp.Pool()
    for poi_type in types:
        pool.apply_async(single_downloader, args=([poi_type]))
    pool.close()
    pool.join()


def download_all_poi():
    lines = []
    with open(r'data\keywords-2\keywords-2-final.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line)
    num_pro = int(mp.cpu_count())
    size, interval = len(lines), len(lines) // num_pro
    start, end = 0, 0
    pool = mp.Pool()
    for processor_index in range(num_pro):
        start = end
        if processor_index == num_pro - 1:
            end = size
        else:
            end += interval
        pool.apply_async(single_all_downloader, args=([processor_index, lines[start: end]]))
    pool.close()
    pool.join()


def single_downloader(poi_type):
    print(poi_type + ': start!')
    filename = r'data\keywords-2\keywords-2-' + poi_type + ".txt"
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            poi_name, url, wd = line[:-1].split('|')
            page_num = 0
            has_next_page = True
            while has_next_page:
                data = []
                url = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd={}&c=289&pn={}'.format(
                    urllib.request.quote(wd), page_num)
                page_num += 1
                request = urllib.request.Request(url)
                try:
                    page = urllib.request.urlopen(request)
                    res = json.load(page)
                    if 'content' in res:
                        contents = res['content']
                        if 'acc_flag' in contents[0]:
                            for content in contents:
                                if str(content['area_name']).__contains__('嘉兴市海宁市'):
                                    data.append(content_to_str(content, poi_type))
                            if len(contents) < 10:
                                has_next_page = False
                        else:
                            has_next_page = False
                    else:
                        has_next_page = False
                    poi.poi_keywords.write2txt(data, r'data\poi\poi_info_' + poi_type + '.tsv')
                except:
                    has_next_page = False
                finally:
                    print(poi_type, wd, page_num, len(data), url)


def single_all_downloader(processor_index, keywords_list):
    print(processor_index, 'start!')
    for line in keywords_list:
        poi_type, url, wd = line[:-1].split('|')
        page_num = 0
        has_next_page = True
        while has_next_page:
            data = []
            url = 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd={}&c=334&pn={}'.format(
                urllib.request.quote(wd), page_num)
            page_num += 1
            request = urllib.request.Request(url)
            try:
                page = urllib.request.urlopen(request)
                res = json.load(page)
                if 'content' in res:
                    contents = res['content']
                    if 'acc_flag' in contents[0]:
                        for content in contents:
                            if str(content['area_name']).__contains__('嘉兴市海宁市'):
                                data.append(content_to_str(content, poi_type))
                        if len(contents) < 10:
                            has_next_page = False
                    else:
                        has_next_page = False
                else:
                    has_next_page = False
                poi.poi_keywords.write2txt(data, r'data\poi\poi_info_' + str(processor_index) + '.tsv')
            except:
                has_next_page = False
            finally:
                print(poi_type, wd, page_num, len(data), url)


if __name__ == '__main__':
    download_all_poi()

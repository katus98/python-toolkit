import urllib
import urllib.request
from bs4 import BeautifulSoup


def write2txt(data, filepath):
    with open(filepath, 'a', encoding='UTF-8') as f:
        for d in data:
            f.write(d)


def get_type_keywords():
    request = urllib.request.Request('https://poi.mapbar.com/jiaxing/')
    page = urllib.request.urlopen(request)
    data = page.read()
    data = data.decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.select('a')
    res = []
    for tag in tags:
        if str(tag['href']).startswith('http://poi.mapbar.com/jiaxing/') & (str(tag['href'])[-5:-4] == '/'):
            res.append(tag['href'] + '|' + tag.get_text() + '\n')
    write2txt(res, r'data\keywords-1\keywords-1.txt')


def get_poi_keywords():
    filename = r'data\keywords-1\keywords-1.txt'
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            url, wd = line.split('|')
            request = urllib.request.Request(url)
            page = urllib.request.urlopen(request)
            data = page.read().decode('utf-8')
            soup = BeautifulSoup(data, 'html.parser')
            tags = soup.select('dd a')
            res = [wd[:-1] + '|' + t['href'] + '|' + t.get_text() + '\n' for t in tags]
            print(url, wd[:-1], len(res))
            write2txt(res, r'data\keywords-2\keywords-2.txt')


def get_poi_keywords_types():
    types = ['car', 'catering', 'entertainment', 'traffic']
    all_count = 0
    for poi_type in types:
        type_count = 0
        filename = r'data\keywords-1\keywords-1-' + poi_type + ".txt"
        print(poi_type + '---------------------------------')
        with open(filename, 'r', encoding='UTF-8') as f:
            for line in f:
                url, wd = line.split('|')
                request = urllib.request.Request(url)
                page = urllib.request.urlopen(request)
                data = page.read().decode('utf-8')
                soup = BeautifulSoup(data, 'html.parser')
                tags = soup.select('dd a')
                res = [wd[:-1] + '|' + t['href'] + '|' + t.get_text() + '\n' for t in tags]
                print(url, wd[:-1], len(res))
                type_count += len(res)
                write2txt(res, r'data\keywords-2\keywords-2-' + poi_type + ".txt")
        print(poi_type + ': ' + str(type_count))
        all_count += type_count
    print('all_count: ' + str(all_count))


if __name__ == '__main__':
    get_poi_keywords()

import json
import urllib.request

import pandas as pd

ak = ''


def reverse_geo_coding():
    global ak
    filename = r'D:\Data\car_roads_points_Jinhua.csv'
    dataset = pd.read_csv(filename, low_memory=False)
    dataset['name_new'] = ''
    count = 0
    for i, row in dataset.iterrows():
        try:
            url = 'https://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json&coordtype=wgs84ll&location={},{}&poi_types=道路'.format(
                ak, row['lat'], row['lon'])
            request = urllib.request.Request(url)
            page = urllib.request.urlopen(request, timeout=0.5)
            res = json.load(page)
            if res['status'] == 0:
                result = res['result']
                addressComponent = result['addressComponent']
                row['name_new'] = addressComponent['street']
                count += 1
                print(count)
            elif res['status'] == 302:
                break
            else:
                print('API-FAILED!', res['status'])
        except:
            print('API-FAILED!', -1)
    dataset.to_csv(r'D:\Data\car_roads_points_Jinhua_1.csv', index=False, sep=',')


if __name__ == '__main__':
    reverse_geo_coding()

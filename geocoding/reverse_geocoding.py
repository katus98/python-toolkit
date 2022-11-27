import json
import urllib.request
import time
import pandas as pd

ak = ''


def reverse_geo_coding():
    global ak
    filename = r'E:\graduation-project\data\roads_ori\car_roads_points_Jinhua.csv'
    dataset = pd.read_csv(filename, low_memory=False)
    dataset['name_new'] = ''
    count = 0
    for i, row in dataset.iterrows():
        try:
            url = 'https://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json&coordtype=wgs84ll&location={},{}&extensions_road={}'.format(
                ak, row['lat'], row['lon'], 'true')
            request = urllib.request.Request(url)
            page = urllib.request.urlopen(request, timeout=0.5)
            res = json.load(page)
            if res['status'] == 0:
                result = res['result']
                roads = result['roads']
                if len(roads) > 0:
                    dataset.iloc[i, -1] = roads[0]['name']
                    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'finish', i)
                    count += 1
                else:
                    dataset.iloc[i, -1] = '-'
                    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'no', i)
            elif res['status'] == 302:
                break
            else:
                print(time.strftime('%Y-%m-%d %H:%M:%S'), 'API-FAILED!', res['status'])
        except:
            print(time.strftime('%Y-%m-%d %H:%M:%S'), 'error', i)
        finally:
            time.sleep(0.1)
    dataset.to_csv(r'E:\graduation-project\data\roads_ori\car_roads_points_Jinhua_res.csv', index=False, sep=',')
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'All Finished!', count, '/', len(dataset))


if __name__ == '__main__':
    reverse_geo_coding()

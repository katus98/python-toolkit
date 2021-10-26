import json
import time
import multiprocessing as mp
import urllib.request
import pandas as pd
import coordinates_transform as ct

ak = ''


def geo_coding():
    global ak
    filename = r'F:\data\form\hn-illegal\csv\hn_accidents.csv'
    dataset = pd.read_csv(filename, low_memory=False)
    pool_results = []
    num_pro = int(mp.cpu_count())
    size, interval = len(dataset), len(dataset) // num_pro
    start, end = -1, -1
    pool = mp.Pool()
    for processor_index in range(num_pro):
        start = end + 1
        if processor_index == num_pro - 1:
            end = size - 1
        else:
            end += interval
        pool_results.append(
            pool.apply_async(single_geo_coding, args=([processor_index, interval, dataset.loc[start:end, :], ak])))
    pool.close()
    pool.join()
    results = []
    for pool_result in pool_results:
        results.append(pool_result.get())
    final_dataset = pd.concat(results)
    print('Result length:', len(final_dataset))
    final_dataset.to_csv(r'F:\data\form\hn-illegal\csv\hn_accidents_geo_1.csv', index=False, sep=',')


def single_geo_coding(processor_index, interval, dataset, l_ak):
    print('Processor ' + str(processor_index) + ' started!')
    for i, row in dataset.iterrows():
        if row['coding_level'] == '-':
            try:
                url = 'https://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&city={}&ret_coordtype=gcj02ll'.format(
                    urllib.request.quote(row['address']), l_ak, urllib.request.quote('嘉兴市'))
                request = urllib.request.Request(url)
                page = urllib.request.urlopen(request, timeout=0.5)
                res = json.load(page)
                if res['status'] == 0:
                    result = res['result']
                    lon, lat = ct.gcj02_to_wgs84(result['location']['lng'], result['location']['lat'])
                    comprehension, coding_level = result['comprehension'], result['level']
                    dataset.iloc[i - processor_index * interval, -4] = lon
                    dataset.iloc[i - processor_index * interval, -3] = lat
                    dataset.iloc[i - processor_index * interval, -2] = comprehension
                    dataset.iloc[i - processor_index * interval, -1] = coding_level
                    time.sleep(0.02)
                elif res['status'] == 302:
                    break
                else:
                    print('API-FAILED!', res['status'])
            except:
                print('API-FAILED!', -1)
        if (i - processor_index * interval + 1) % 200 == 0:
            print('Processor ' + str(processor_index) + ' finished ' + str(
                i - processor_index * interval + 1) + ' lines!')
    print('Processor ' + str(processor_index) + ' all finished!', len(dataset))
    return dataset


if __name__ == '__main__':
    geo_coding()

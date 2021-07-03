"""
@:filename insert-sql.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2020-10-05
"""
from random_words import RandomWords
import utils.process as pr
import random
import codecs

if __name__ == '__main__':
    number = 5000
    outputFilename = r'D:\Data\3S_insert.sql'
    lst = ['基础分析类', '土地资源类', '生态环境类', '气象气候类', '社会经济类', '灾害监测类', '海洋资源类']
    ids = set()
    public = ['TRUE', 'FALSE']
    print('Running...')
    outputFile = codecs.open(outputFilename, 'w', 'utf-8')
    rw = RandomWords()
    for i in range(number):
        item = rw.random_word()
        while item in ids:
            item = rw.random_word()
        ids.add(item)
        new_line = "INSERT INTO tb_paralleltool(ARTIFACT_ID, USAGES, JAR_PATH, XML_PATH, IS_PUBLIC) VALUE"
        new_line += "('" + item + "', '" + lst[int(random.uniform(0, 7))] + "', '/opt/3S/upload/jar/" + item + ".jar', "
        new_line += "'/opt/3S/upload/xml/" + item + ".xml', " + public[int(random.uniform(0, 2))] + ");\n"
        outputFile.write(new_line)
        pr.process_bar(1.0 * i / number, start_str='', end_str='100.0%', total_length=100)
    outputFile.close()
    print('\nAll finished!')

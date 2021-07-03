"""
@:filename words-maker.py
@:description
@:author Keran Sun (katus)
@:version 1.0, 2020-09-18
"""
from random_words import RandomWords
import random

if __name__ == '__main__':
    number = 10000
    lst = [' '] * 9 + ['\n']
    file = open(r'D:\Data\TestData\words1.txt', 'w')
    rw = RandomWords()
    item = rw.random_word()
    for i in range(1, number):
        item += lst[int(random.uniform(0, 10))] + rw.random_word()
        file.write(item)
        item = ''
    file.close()

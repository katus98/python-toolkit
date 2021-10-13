from random_words import RandomWords, RandomEmails
import random

if __name__ == "__main__":
    number = 100
    gender = ["male", "female"]
    rw = RandomWords()
    re = RandomEmails()
    file = open(r'D:\Data\TestData\student2.json', 'w')
    for i in range(1, number + 1):
        item = '{"no": ' + str(i) + ', '
        item += '"name": "' + rw.random_word() + '", '
        item += '"age": ' + str(int(random.uniform(10, 100))) + ', '
        item += '"gender": "' + gender[int(random.uniform(0, 2))] + '", '
        item += '"email": "' + re.randomMail() + '"}\n'
        file.write(item)
    file.close()

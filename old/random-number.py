import random

if __name__ == '__main__':
    min_number, max_number = 1, 2146
    first_prize, first_prize_number = [], 1
    random_prize, random_prize_number = [], 10
    for i in range(first_prize_number):
        first_prize.append(random.randint(min_number, max_number + 1))
    for i in range(random_prize_number):
        random_prize.append(random.randint(min_number, max_number + 1))
    print('First prize: ', first_prize)
    print('Random prize: ', random_prize)

# -*- coding: utf-8 -*-
import random

secret_number = random.randint(1, 20)
print('1から20までの数を当てて下さい')

for guesses_taken in range(1, 7):
    print('数を入力してください')
    guess = int(input())

    if guess < secret_number:
        print('小さいです')
    elif guess > secret_number:
        print('大きいです')
    else:
        break

if guess == secret_number:
    print('あたり！！' + str(guesses_taken) + '回で当たりました')
else:
    print('残念。正解は' + str(secret_number) + 'でした')

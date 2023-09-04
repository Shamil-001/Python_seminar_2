# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('введите количество монеток: '))
coin_zero = 0
coin_one = 0
for i in range(n):
    x = int(input(f'введи 0 или 1 для {i+1}-й монеты\n'))
    if x == 0:
        coin_zero += 1
    if x == 1:
        coin_one += 1
    else: print('нужно вводить 1 или 0!')
if coin_one > coin_zero:
    print(coin_zero)
else:
    print(coin_one)
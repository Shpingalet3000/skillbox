import random

with open('out_file.txt', 'w') as numbers_file:
    numb_sum = 0
    while numb_sum < 777:
        try:
            number = int(input('Введите число: '))
            numb_sum += number
            if random.randint(1, 13) == 13:
                raise Exception("Вас постигла неудача!")
            numbers_file.write(str(number) + '\n')
        except Exception as exe:
            print(exe)
            break
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')




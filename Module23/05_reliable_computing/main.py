import math


def safe_sqrt(number_user):
    try:
        num = float(number_user)
        try:
            if num < 0:
                raise ValueError('Отрицательное число.')
            print(math.sqrt(num))
        except ValueError as ve:
            print(f'Ошибка: {ve}')
        except Exception as exe:
            print(f'Неизвестная ошибка: {exe}.')
    except ValueError:
        print("Ошибка: Не удалось преобразовать в число.")


while True:
    number = input("\nВведите число: ")
    safe_sqrt(number)

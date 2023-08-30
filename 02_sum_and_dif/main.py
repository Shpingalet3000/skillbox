def sum_digits(number):
    digits = str(number)
    summa = 0
    for digit in digits:
        summa += int(digit)
    return summa

def count_digits(number):
    digits = str(number)
    return len(digits)

print("Первый вариант решения задачи")
number = int(input("Введите число: "))
summa = sum_digits(number)
count = count_digits(number)
diff = summa - count

print("Сумма чисел:", summa)
print("Количество цифр в числе:", count)
print("Разность суммы и количества цифр:", diff)

def sum_digits(number):
    summa = 0
    while number > 0:
        digit = number % 10
        summa += digit
        number = number // 10
    return summa

def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count

print("\nВторой вариант решения задачи")
number = int(input("Введите число: "))

summa = sum_digits(number)
count = count_digits(number)

diff = summa - count

print("Сумма чисел:", summa)
print("Количество цифр в числе:", count)
print("Разность суммы и количества цифр:", diff)

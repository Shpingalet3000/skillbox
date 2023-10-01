numbers = []
number = int(input("Количество цифр в списке: "))
for i in range(number):
    num = int(input(f"Введите {i + 1} число: "))
    numbers.append(num)
print("Изначальный список целых чисел:", numbers)
print("Четные числа из списка в обратном порядке:", end=' ')
for i in range(len(numbers) - 1, -1, -1):
    if int(numbers[i]) % 2 == 0:
        print(numbers[i], end=" ")



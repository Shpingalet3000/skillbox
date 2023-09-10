# numbers = [1, 4, -3, 0, 10]
numbers = []
number = int(input("Количество цифр в списке: "))
for i in range(number):
    num = int(input(f"Введите {i + 1} число: "))
    numbers.append(num)
print("Изначальный список:", numbers)

swapped = True
while swapped is True:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True
print("Отсортированный список:", numbers)


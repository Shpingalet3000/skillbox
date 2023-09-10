num_list = []
number = int(input("Введите число: "))
for num in range(1, number + 1):
    if num % 2 != 0:
        num_list.append(num)
print("Список из нечётных чисел от одного до N(" + str(number) + "):", num_list)

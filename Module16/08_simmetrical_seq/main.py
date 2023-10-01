number_count = int(input("Количество чисел: "))
number_list = []
reverse_number_list = []

for _ in range(number_count):
    number = int(input("Число: "))
    number_list.append(number)
print("\nПоследовательность:", number_list)

for index in range(len(number_list) - 1, -1, -1):
    reverse_number_list.append(number_list[index])

symmetric_sequence = []
while number_list != reverse_number_list:
    symmetric_sequence.insert(0, number_list[0])
    reverse_number_list = reverse_number_list[:-1]
    number_list = number_list[1:]

print("Нужно приписать чисел:", len(symmetric_sequence))
print("Сами числа:", symmetric_sequence)

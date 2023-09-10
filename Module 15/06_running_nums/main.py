print("Первый вариант")
shift = int(input("Сдвиг: "))
# original_list = [1, 2, 3, 4, 5]
original_list = [1, 4, -3, 0, 10]
shifted_list = []
if shift > len(original_list):
    print("Сдвиг привышает длину списка")
else:
    shifted_list = original_list[-shift:] + original_list[:-shift]

    print("Изначальный список:", original_list)
    print("Сдвинутый список:", shifted_list)


print("\nВторой вариант")

shifted_list = []
for i in range(len(original_list)):
    shifted_list.append(original_list[-shift + i])

print("Изначальный список:", original_list)
print("Сдвинутый список:", shifted_list)






def smallest_divisor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return i

number = int(input("Введите число: "))
divisor = smallest_divisor(number)

print("Наименьший делитель, отличный от единицы:", divisor)

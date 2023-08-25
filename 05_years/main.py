def check_special_years(first_year, second_year):
    for year in range(first_year, second_year + 1):
        digits = str(year)
        if digits[0] == digits[1] == digits[2]:
            print(year)
        elif digits[1] == digits[2] == digits[3]:
            print(year)
        elif digits[0] == digits[2] == digits[3]:
            print(year)
        elif digits[0] == digits[1] == digits[3]:
            print(year)


print("Первый вариант решения задачи")
first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))
print("\nГоды от", first_year, "до", second_year, "с тремя одинаковыми цифрами:")
special_years = check_special_years(first_year, second_year)


def check_special_years(first_year, second_year):
    special_years = []
    for year in range(first_year, second_year + 1):
        digits = [int(digit) for digit in str(year)]
        if digits[0] == digits[1] == digits[2]:
            special_years.append(year)
        elif digits[1] == digits[2] == digits[3]:
            special_years.append(year)
        elif digits[0] == digits[2] == digits[3]:
            special_years.append(year)
        elif digits[0] == digits[1] == digits[3]:
            special_years.append(year)
    return special_years


print("\nВторой вариант решения задачи")
first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))

special_years = check_special_years(first_year, second_year)
if len(special_years) != 0:
    print("\nГоды от", first_year, "до", first_year, "с тремя одинаковыми цифрами:")
    for year in special_years:
        print(year)
else:
    print("\nВо временном интервале " + str(first_year) + "-" + str(
        first_year) + " гг. нет года с тремя одинаковыми цифрами.")



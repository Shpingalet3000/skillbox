def count_uppercase_lowercase(string):
    uppercase_string = 0
    lowercase_string = 0

    for char in string:
        if char.isupper():
            uppercase_string += 1
        elif char.islower():
            lowercase_string += 1

    return uppercase_string, lowercase_string


text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)

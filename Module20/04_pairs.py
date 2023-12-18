import random

original_list = [random.randint(0, 10) for _ in range(10)]
print(f"Оригинальный список: {original_list}")

# First variable
new_list = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]
print(f'Новый список, {new_list}')

# Second variable
new_list = list(zip(original_list[::2], original_list[1::2]))
print(f'Новый список, {new_list}')
def is_prime(number):
    divider_counter = 0
    if number < 2:
        return False
    for i_num in range(1, number + 1):
        if number % i_num == 0:
            divider_counter += 1
            if divider_counter > 2:
                return False
    return True


def crypto(checking_list):
    return [element for index, element in enumerate(checking_list) if is_prime(index)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))


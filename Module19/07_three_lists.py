def common_elements(common_element_1, common_element_2, common_element_3):
    # Solution without using sets
    common = []
    for elem in common_element_1:
        if elem in common_element_2 and elem in common_element_3:
            common.append(elem)
    print("Решение без множеств:", ", ".join(str(elem) for elem in sorted(common)))

    # Solution using sets
    set_1 = set(common_element_1)
    set_2 = set(common_element_2)
    set_3 = set(common_element_3)
    common = set_1.intersection(set_2, set_3)
    print("Решение с множествами:", ", ".join(str(elem) for elem in sorted(common)))


def unique_elements(unique_element_1, unique_element_2, unique_element_3):
    # Solution without using sets
    unique = []
    for elem in unique_element_1:
        if elem not in unique_element_2 and elem not in unique_element_3:
            unique.append(elem)
    print("Решение без множеств:", ", ".join(str(elem) for elem in sorted(unique)))

    # Solution using sets
    set_1 = set(unique_element_1)
    set_2 = set(unique_element_2)
    set_3 = set(unique_element_3)
    unique = set_1.difference(set_2, set_3)
    print("Решение с множествами:", ", ".join(str(elem) for elem in sorted(unique)))


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print("Задача 1:")
common_elements(array_1, array_2, array_3)

print("Задача 2:")
unique_elements(array_1, array_2, array_3)

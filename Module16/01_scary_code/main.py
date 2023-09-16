main_list = [1, 5, 3]
first_secondary_list = [1, 5, 1, 5]
second_secondary_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_secondary_list)
print("Количество цифр 5 при первом объединении:", main_list.count(5))

for i_element in main_list:
    if i_element == 5:
        main_list.remove(i_element)

main_list.extend(second_secondary_list)
print("Количество цифр 3 при втором объединении:", main_list.count(3))
print("Итоговый список:", main_list)


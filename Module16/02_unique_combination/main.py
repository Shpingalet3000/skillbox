def sorted_lists(sorted_list):
    for j_mn in range(len(sorted_list)):
        for curr in range(j_mn, len(sorted_list)):
            if sorted_list[curr] < sorted_list[j_mn]:
                sorted_list[curr], sorted_list[j_mn] = sorted_list[j_mn], sorted_list[curr]


def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    merged_list.extend(list1)
    sorted_lists(merged_list)
    for j_mn in range(len(merged_list)):
        for k_mn in merged_list:
            if merged_list.count(k_mn) > 1:
                merged_list.remove(k_mn)


count_first_list = int(input('Введите количество чисел первого списка: '))
count_second_list = int(input('Введите количество чисел второго списка: '))
first_list = []
second_list = []
merged_list = []

if count_first_list > 0:
    print()

for i_mn in range(count_first_list):
    number = int(input(f'Введите {i_mn + 1} число для первого списка: '))
    first_list.append(number)
    sorted_lists(first_list)

if count_second_list > 0:
    print()

for i_mn in range(count_second_list):
    number = int(input(f'Введите {i_mn + 1} число для второго списка: '))
    second_list.append(number)
    sorted_lists(second_list)

print('Первый первый список:', first_list)
print('Второй первый список:', second_list)

merge_sorted_lists(first_list, second_list)
print('\nCписок с уникальными элементами:', merged_list)

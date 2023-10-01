count_roller_skates = int(input('Количество роликов: '))
roller_skate_list = []
foot_size_list = []
count = 0

for i in range(count_roller_skates):
    roller_skate_size = int(input(f'Размер пары {i + 1}: '))
    roller_skate_list.append(roller_skate_size)

count_people = int(input('\nКоличество людей: '))
for i in range(count_people):
    foot_size = int(input(f'Размер ноги человека {i + 1}: '))
    foot_size_list.append(foot_size)

for size in foot_size_list:
    for j in range(len(roller_skate_list)):
        if roller_skate_list[j] == size:
            roller_skate_list.remove(roller_skate_list[j])
            count += 1
            break

print('Наибольшее количество людей, которые могут взять ролики:', count)

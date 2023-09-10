containers = []

while True:
    number_containers = int(input("Количество контейнеров: "))
    if number_containers <= 200:
        break
    else:
        print("Ошибка! Количество контейнеров не должено превышать 200.")

for _ in range(number_containers):
    while True:
        weight = int(input("Введите вес контейнера: "))
        if weight <= 200:
            break
        else:
            print("Ошибка! Вес контейнера не должен превышать 200.")
    containers.append(weight)

while True:
    new_weight = int(input("Введите вес нового контейнера: "))
    if new_weight <= 200:
        break
    else:
        print("Ошибка! Вес нового контейнера не должен превышать 200.")

index = 0
for i in range(len(containers)):
    if containers[i] < new_weight:
        index = i + 1
        break

print("Номер, который получит новый контейнер:", index)


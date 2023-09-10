videocard_list = []
new_videocard_list = []
number_videocards = int(input("Количество видеокарт: "))

for i in range(1, number_videocards + 1):
    number_videocards = int(input("Видиокарта " + str(i) + ": "))
    videocard_list.append(number_videocards)
print('Старый список видеокарт:', videocard_list)    

max_value = max(videocard_list)

for card in videocard_list:
    if card != max_value:
        new_videocard_list.append(card)
print('Новый список видеокарт: ', new_videocard_list)

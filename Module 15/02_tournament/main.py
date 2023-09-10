names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
participants_list = []
for i in range(0, len(names), 2):
    participants_list.append(names[i])
print("Первый день:", participants_list)
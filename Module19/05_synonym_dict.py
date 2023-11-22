sinonims_dict = dict()

number_pairs = int(input('Введите количество пар слов: '))

for i in range(1, number_pairs + 1):
    sinonims = input(f'{i}-я пара: ').lower().split(' - ')
    sinonims_dict[sinonims[0]] = sinonims[1]
    sinonims_dict[sinonims[1]] = sinonims[0]

while True:
    word = input('Введите слово (для выхода введите "0"):  ').lower()
    if word == "0":
        break
    elif word in sinonims_dict:
        print('Синоним:', sinonims_dict[word])
    else:
        print('Такого слова в словаре нет.')

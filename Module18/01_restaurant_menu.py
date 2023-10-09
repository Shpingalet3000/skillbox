# first solution to the problem
available_menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
print('Доступное меню:', available_menu + ".")
menu_list = available_menu.split(";")
print('Актуальное меню:', (', '.join(menu_list)) + ".")

# second solution to the problem
print('')
available_menu = input('Доступное меню: ').split(';')
print('Актуальное меню:', ', '.join(available_menu))

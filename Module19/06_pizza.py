order_dict = dict()
number_orders = int(input('Введите количество заказов: '))
for i in range(1, number_orders + 1):
    order = input(f'{i}-й заказ: ').split()
    if order[0] in order_dict:
        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = order[2]
    else:
        order_dict[order[0]] = dict({order[1]: int(order[2])})

for name in sorted(order_dict):
    print(f'{name} :')
    for pizza in sorted(order_dict[name]):
        print(f'{pizza} : {order_dict[name][pizza]}')

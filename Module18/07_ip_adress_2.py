ip = input('Введите IP: ').split('.')

if len(ip) < 4:
    print('Адрес - это четыре числа, разделённые точками.')
else:
    numeric = 0
    for i_ip in ip:
        if i_ip.isdigit():
            numeric += 1
            if int(i_ip) > 255:
                print(i_ip, 'превышает 255.')
                break
        else:
            print(i_ip, '- не целое число.')
            break

    if numeric == 4:
        print('IP-адрес корректен.')

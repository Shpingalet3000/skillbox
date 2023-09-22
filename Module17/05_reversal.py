string = input('Введите строку: ')

reversed_substring = string[(string.rindex('h') - 1):string.index('h'):-1]
print('Развёрнутая последовательность между первым и последним h:', reversed_substring)

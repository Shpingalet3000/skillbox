numbers_file = open('numbers.txt', 'r')
str_list = numbers_file.read().split()
numb_list = [int(i_elem) for i_elem in str_list]
summa = 0
for i_numb in numb_list:
    summa += i_numb
numbers_file.close()

file_in = open("answer.txt", "w", encoding="utf8")
file_in.write(str(summa))
file_in.close()

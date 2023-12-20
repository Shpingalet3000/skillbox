def shortest_seq_range(string, tpl):
    return min(len(string), len(tpl))


sym_str = 'abcd'
num_tpl = (10, 20, 30, 40, 50)

pairs = ((sym_str[i_elem], num_tpl[i_elem]) for i_elem in range(shortest_seq_range(sym_str, num_tpl)))
print(pairs)
for i_elem in pairs:
    print(i_elem)


def my_zip(*args):
    min_len = min(len(arg) for arg in args)
    pairs = ((arg[i] for arg in args) for i in range(min_len))
    return pairs


a = (True, False, True, False)
b = [1, 2, 3, 4, 5]
c = ['a', 'b', 'c', 'd']

print(my_zip(a, b, c))

for elem in my_zip(a, b, c):
    print(tuple(i_elem for i_elem in elem))


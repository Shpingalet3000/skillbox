# First variable
def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


# Second variable
def tpl_sort2(tpl):
    if all(isinstance(i_tpl, int) for i_tpl in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl


tpl = (6, 3, -1, 8, 4, 10, -5)

print(tpl_sort(tpl))
print(tpl_sort2(tpl))



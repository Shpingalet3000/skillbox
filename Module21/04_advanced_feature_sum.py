def advanced_sum(*args):
    result = 0
    for arg in args:
        if not isinstance(arg, (list, tuple)):
            result += arg
        else:
            result += advanced_sum(*arg)
    return result


print(advanced_sum([[1, 2, [3]], [1], 3]))
print(advanced_sum(1, 2, 3, 4, 5))

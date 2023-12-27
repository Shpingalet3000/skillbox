def external_list(struct):
    new_list = []
    for item in struct:
        if not isinstance(item, list):
            new_list.append(item)
        else:
            new_list.extend(external_list(item))
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],[[11, 12, 13], [14, 15], [16, 17, 18]]]

print(external_list(nice_list))

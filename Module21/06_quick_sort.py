
def auxiliary_function(list_elements):
    support_element = list_elements[-1]
    list_of_smaller_elements = []
    list_of_equal_elements = []
    list_of_large_elements = []
    for element in list_elements:
        if element < support_element:
            list_of_smaller_elements.append(element)
        elif element == support_element:
            list_of_equal_elements.append(element)
        else:
            list_of_large_elements.append(element)
    return list_of_smaller_elements, list_of_equal_elements, list_of_large_elements


def quick_sort(list_of_numbers):
    if len(list_of_numbers) <= 1:
        return list_of_numbers
    else:
        all_lists = auxiliary_function(list_of_numbers)
        return quick_sort(all_lists[0]) + all_lists[1] + quick_sort(all_lists[2])


list_of_numbers = [4, 9, 2, 7, 5]
sorted_array = quick_sort(list_of_numbers)
print(sorted_array)

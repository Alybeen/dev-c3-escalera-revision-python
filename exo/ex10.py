import re


def is_number(arg):
    try:
        int(arg)
        is_number = True
    except ValueError:
        is_number = False
    return is_number


def sort_by_insertion(numbers: list):
    if len(numbers) == 0:
        return 'liste vide'
    else:
        is_number_list = list(filter(lambda x: is_number(x), numbers))
        if is_number_list:
            for i in range(len(is_number_list)):
                x = int(is_number_list[i])
                j = i
                while j > 0 and int(is_number_list[j - 1]) > x:
                    is_number_list[j] = int(is_number_list[j - 1])
                    j = j - 1
                is_number_list[j] = x
            return is_number_list
        return 'il n\'y pas de nombres dans cette liste'

print(sort_by_insertion(["p"]))

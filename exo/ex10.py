import re


def is_number(arg):
    try:
        int(arg)
        is_number = True
    except ValueError:
        is_number = False
    return is_number


def sort_by_insertion(numbers: list):
    not_number_list = re.search(r'\d', ''.join(str(e) for e in numbers))
    if len(numbers) == 0 or not_number_list is None:
        return 'cette liste est vide ou n\'est pas une liste de nombres'
    else:
        is_number_list = list(filter(lambda x: is_number(x), numbers))
        for i in range(len(is_number_list)):
            x = int(is_number_list[i])
            j = i
            while j > 0 and int(is_number_list[j - 1]) > x:
                is_number_list[j] = int(is_number_list[j - 1])
                j = j - 1
            is_number_list[j] = x
        return is_number_list

print(sort_by_insertion(["p"]))

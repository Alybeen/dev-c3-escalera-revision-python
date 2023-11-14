def is_number(arg):
    try:
        int(arg)
        is_number = True
    except ValueError:
        is_number = False
    return is_number

def calculate (numbers:list):
    if len(numbers) == 10:
        return [n*n if int(n) != 0 else 1 for n in filter(lambda x: is_number(x), numbers)]
    else:
        return

print(calculate([1,-2,9,5,8,0,4,7,6,9]))
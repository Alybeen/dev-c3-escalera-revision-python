def is_number(arg):
    try:
        int(arg)
        is_number = True
    except ValueError:
        is_number = False
    return is_number

def calculate (numbers:list):
    if len(numbers) == 10:
        return [n*n for n in numbers if is_number(n) and int(n) >0]
    else:
        return

print(calculate([1,7,9,5,8,0,4,7,3,9]))
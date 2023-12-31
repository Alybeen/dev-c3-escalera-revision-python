import re


def multiply(A:int, B:int):
    return str(A * B)


def divide(A:int, B:int):
    return str(A/B)

def addition(A:int, B:int):
    return str(A+B)

def soustraction(A:int,B:int):
    return str(A-B)

# recursive function for priority calcul if it has
def calcul_priority(input:str):
    #find a priority calcul
    has_priority = re.search("\d*[Xx/]\d*", input)
    if has_priority:
        numbers = re.split('[Xx/]', has_priority.group(0))
        numA = int(numbers[0])
        numB = int(numbers[1])
        res = ''
        if has_priority.group(0).find('x')!=-1:
            res = multiply(numA, numB)
        elif has_priority.group(0).find('X') != -1:
            res = multiply(numA, numB)
        elif has_priority.group(0).find('/') != -1:
            res = divide(numA, numB)
        if res is not None:
            try:
                return calcul_priority(re.sub(has_priority.group(0), res, input))
            except:
                print("une erreur est survenue")
                return
        else:
            return
    else:
        return input

#recursive function for other calcul than mutliply or divide
def calcul(input:str):
    cal = re.search("\d*(?:\+|\-)\d*", input)
    if cal:
        res = ''
        numbers = re.split('[+-]', cal.group(0))
        numA = int(numbers[0])
        numB = int(numbers[1])
        group=""
        if cal.group(0).find('+') != -1:
            group = re.sub("\+", '\+', cal.group(0))
            res = addition(numA, numB)
        elif cal.group(0).find('-') != -1:
            group = re.sub("\-", '\-', cal.group(0))
            res = soustraction(numA,numB)
        return calcul(re.sub(group, res, input))
    else:
        return input


#start to calculate
is_valid = False
while not is_valid:
    operation = input("Entrez une opération :")
    # todo : check comma etc.
    if operation:
        is_valid = True
        priorityResult=None
        try:
            priorityResult = calcul_priority(operation)
        except ZeroDivisionError as e:
            print(e)
            is_valid= False
        except ValueError as e:
            print(e)
            is_valid= False
        except TypeError as e:
            print(e)
            is_valid= False
        if priorityResult is not None:
            try:
                print(f'{calcul(priorityResult)}')
            except ValueError as e:
                print(e)
                is_valid = False
            except TypeError as e:
                print(e)
                is_valid = False
    else:
        operation = input("Entrez une opération :")

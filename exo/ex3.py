import re
def multiplication(numA:int, numB:int):
    return (numA*numB)

def division(numA:int, numB:int):
    print(numA//numB)

def calcul(operation: str):
    m=0
    a=0
    s=0
    d=0
    if operation.find("x".lower()) !=-1:
        m = multiplication(int(operation[operation.find("x") - 1]), int(operation[operation.find("x") + 1]))
    if operation.find("/") != -1:
        numA = int(operation[operation.find("/") - 1])
        numB = int(operation[operation.find("/") + 1])
        d = division(numA, numB)


operation = input("Entrez l'opération voulue:")

print(calcul(operation))
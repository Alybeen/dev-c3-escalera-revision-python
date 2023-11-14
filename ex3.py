import re
def multiplication(numA:int, numB:int):
    return (numA*numB)

def calcul(operation: str):
    result = 0
    if operation.find("x".lower()):
        result = multiplication(int(operation[operation.find("x") - 1]), int(operation[operation.find("x") + 1]))

operation = input("Entrez l'opération voulue:")


calcul(operation)
students = {
    "Alice Dupond": 9,
    "william Burrough": 19,
    "Bob Marley": 'P',
    "william Wallace": 19,
}


def is_number(arg):
    try:
        int(arg)
        is_number = True
    except ValueError:
        is_number = False
    return is_number


def find_best_students(students: dict):
    if len(students) > 0:
        max_note = 0
        name = ''
        for elem in sorted(students.items()):
            if is_number(elem[1]):
                if int(elem[1]) > max_note:
                    max_note = elem[1]
                    name = elem[0]
                elif elem[1] == max_note:
                    if name > elem[0]:
                        name = elem[0]
            else:
                return f' Erreur dans la notation de {elem[0]}'
        return f'{name} : {max_note}'

    return "il n'y a pas d'étudiant dans cette liste"


print(find_best_students(students))

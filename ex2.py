import string


def display_sentence(sentence: string):
    print(f'Voici votre phrase en lettres majuscules : {sentence.upper()}')
    print(f'Voici votre phrase en lettres minuscules : {sentence.lower()}')


validate_input = False

while not validate_input:
    sentence = input("Entrez une phrase :")
    if len(sentence) > 0 and not sentence.isdigit():
        validate_input = True
        display_sentence(sentence)

import os
import random
from time import sleep

HANGMANPICS = ['''
    +---+
        |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========''']

# Leemos el archivo data.txt para obtener las palabras y 
# retornamos una al azar
def read():
    with open("archivos/data.txt", "r", encoding="utf-8") as f:
        # APLICANDO LIST COMPREHENSION
        word = random.choice([word.strip() for word in f])
    return word.upper()

# Funcion que sirve para eliminar tildes en las palabras
def replace_accent(word):
    dict_accent = {
        'Á': "A",
        "É": "E",
        "Í": "I",
        "Ó": "O",
        "Ú": "U"
    }
    # APLICANDO LAMBDAS
    new_word = "".join(list(map(lambda x: dict_accent.get(x, x), word)))
    return new_word


def run():
    word = replace_accent(read())
    secret_word = ["_" for i in word]
    errors = 0

    while True:
        # INTERFAZ INICIAL
        os.system("cls")
        print(f"""
        ** JUEGO DEL AHORCADO **
Instrucciones: Introduce una y sólo una letra a la vez
para tratar de adivinar la palabra oculta

-- Lleva {errors} {"error" if errors == 1 else "errores"} --
> {" ".join(secret_word)} <
    {HANGMANPICS[errors]}
""")

        # CÓDIGO
        if errors == 7 or word == "".join(secret_word).upper():
            break
        else:
            try:
                user_input = input(f'Adivina la palabra ({len(word)} letras): ')
                user_input = replace_accent(user_input.upper())

                if len(user_input) != 1:
                    raise ValueError('Sólo se permite una letra a la vez')
                elif user_input in word:
                    for index, value in enumerate(word):
                        if value == user_input:
                            secret_word[index] = user_input
                else:
                    errors += 1

            except ValueError as e:
                print(f'ERROR: {e}')
                errors += 1
                sleep(3)

    # INTERFAZ DE SALIDA
    print(f"""  
-- {"FELICIDADES, GANASTE" if word == "".join(secret_word).upper() 
    else "LO SIENTO, PERDISTE"} --
> La palabra era {word} <
""")
        

if __name__ == "__main__":
    run()
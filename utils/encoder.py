import random
from termcolor import colored
import os

def clean_terminal():
    sistema_operativo = os.name

    if sistema_operativo == "posix":  
        os.system("clear")
    elif sistema_operativo == "nt":
        os.system("cls")

def display_encrypted(ENCRYPTED):
    """
    Muestra el contenido de la matriz encriptada respetando las filas y columnas.
    
    Parameters:
    - ENCRYPTED (list): Matriz que representa el texto encriptado.
    """
    for row in ENCRYPTED:
        for value in row:
            if value == 0:
                continue
            elif value == "/":
                print()
                return
            color = 'blue' if isinstance(value, str) else 'white'
            newValue = value.upper() if isinstance(value, str) else value
            
            print(colored(newValue, color), end=" ")
        print()

def save_dictionary(letter_numbers, known_letters, used_numbers, ENCRYPTED):
    """
    Lee un archivo de texto, asigna números a letras, selecciona una palabra aleatoria,
    y encripta el texto utilizando una matriz.

    Parameters:
    - letter_numbers (dict): Diccionario que asigna números a letras.
    - known_letters (list): Lista de letras conocidas.
    - used_numbers (list): Lista de números utilizados.
    - ENCRYPTED (list): Matriz para almacenar el texto encriptado.
    """
    with open("files/input.txt", "r", encoding="utf-8") as f:
        text = f.read().upper()

    random_word_result = random_word(text)

    for letter in text:
        if letter not in letter_numbers:
            letter_numbers[letter] = "|" if letter == " " else "/" if letter == "\n" else assign_unique_number(used_numbers)
            
    known_letters.extend(set(random_word_result) - set(known_letters))
    
    encrypt(text, letter_numbers, known_letters, ENCRYPTED)

def assign_unique_number(used_numbers):
    """
    Asigna un número único no utilizado previamente.

    Parameters:
    - used_numbers (list): Lista de números utilizados.

    Returns:
    - int: Número único asignado.
    """
    number = random.randint(1, 27)
    while number in used_numbers:
        number = random.randint(1, 27)
    used_numbers.append(number)
    return number

def random_word(text):
    """
    Selecciona una palabra aleatoria del texto dividido en palabras.

    Parameters:
    - texto (str): Texto del cual se seleccionará una palabra.

    Returns:
    - str: Palabra aleatoria seleccionada.
    """
    words = text.split()
    return random.choice(words)

def encrypt(text, letter_numbers, known_letters, ENCRYPTED):
    """
    Encripta el texto utilizando una matriz y asigna números a las letras.

    Parameters:
    - text (str): Texto que se va a encriptar.
    - letter_numbers (dict): Diccionario que asigna números a letras.
    - known_letters (list): Lista de letras conocidas.
    - ENCRYPTED (list): Matriz para almacenar el texto encriptado.
    """
    row, position = 0, 0

    for letter in text:
        if letter_numbers[letter] == "/":
            row += 2
        else:
            ENCRYPTED[row][position] = letter_numbers[letter]
            
            if letter in known_letters:
                ENCRYPTED[row + 1][position] = f"{letter} " if letter_numbers[letter] >= 10 else f"{letter}"
            elif letter_numbers[letter] == "|":
                ENCRYPTED[row][position] = ENCRYPTED[row + 1][position] = "\u2588"
            else:
                ENCRYPTED[row + 1][position] = "  " if letter_numbers[letter] >= 10 else " "

        position += 1

    ENCRYPTED[row + 1][position] = "/"

def decrypt(selected_number, letter_to_assign, ENCRYPTED):
    clean_terminal()
    """
    Desencripta el texto asignando una letra a un número en la matriz encriptada.

    Parameters:
    - selected_number (int): Número seleccionado para desencriptar.
    - letter_to_assign (str): Letra que se asignará al número desencriptado.
    - ENCRYPTED (list): Matriz que representa el texto encriptado.
    """
   
    # Comprobamos que el numero exista
    if all(selected_number not in row for row in ENCRYPTED): 
        print(colored(f'\nNo existe el número: {selected_number}\n', 'red'))
        return
    
    # Asignamos el valor
    for i, row in enumerate(ENCRYPTED):
        for j, val in enumerate(row):
            if isinstance(val, str) and isinstance(letter_to_assign, str):
                if val.lower() == letter_to_assign.lower() :
                        ENCRYPTED[i][j] = f"  " if ENCRYPTED[i - 1][j] >= 10 else f" "
                        ENCRYPTED[i+1][j] = f"{letter_to_assign} " if ENCRYPTED[i - 1][j] >= 10 else f"{letter_to_assign}"
                        
            elif val == selected_number :
                 ENCRYPTED[i+1][j] = f"{letter_to_assign} " if val >= 10 else f"{letter_to_assign}"
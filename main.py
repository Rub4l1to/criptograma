from utils.encoder import decrypt, save_dictionary, display_encrypted, clean_terminal

# Función principal
def main():
    letter_numbers = {}
    known_letters = []
    used_numbers = []

    with open("files/input.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    ENCRYPTED = [[0 for _ in range(len(contenido) + 1)] for _ in range(len(contenido)+1)]
    
    save_dictionary(letter_numbers, known_letters, used_numbers, ENCRYPTED)
    display_encrypted(ENCRYPTED)   

    while True:
      
        selected_number = int(input("Enter the number to select (0 to close): "))
        if selected_number == 0:
            break
        letter_to_assign = str(input("Enter the letter to assign: "))

        decrypt(selected_number, letter_to_assign, ENCRYPTED)
        
        display_encrypted(ENCRYPTED)
if __name__ == "__main__":
    main()
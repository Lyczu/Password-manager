from cryptography.fernet import Fernet

def load_key():
    key_path = input("Podaj ścieżkę do pliku klucza: ")
    try:
        with open(key_path, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key

KEY = load_key()

print(KEY)


def main():  
    while True:
        print("\nMenedżer haseł:")
        print("1. Dodaj hasło")
        print("2. Pobierz hasło")
        print("3. Usuń hasło")
        print("4. Sprawdź dostępne hasła dla loginu")
        print("5. Sprawdź czy twoje hasła nie wyciekły")
        print("6. Wyjście")
        choice = input("Wybierz opcję: ")
        
        if choice == "1":

        elif choice == "2":

        elif choice == "3":

        elif choice == "4":

        elif choice == "5"

        elif choice == "6"

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

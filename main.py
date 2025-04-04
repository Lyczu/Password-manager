from cryptography.fernet import Fernet
from breaches import breach_manager

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


def main(key=None):  
    while True:
        print("\nMenedżer haseł:")
        print("1. Dodaj hasło")
        print("2. Pobierz hasło")
        print("3. Usuń hasło")
        print("4. Sprawdź dostępne hasła dla loginu")
        print("5. Sprawdź czy twoje hasła nie wyciekły")
        print("6. Wyjście")
        choice = input("Wybierz opcję: ")
        
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                breach_manager()
            case "6":
                pass
            case _:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    key = load_key()
    main(key=key)

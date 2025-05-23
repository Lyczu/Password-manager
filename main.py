from cryptography.fernet import Fernet
from breaches import breach_manager
import json
import getpass
import os
from functools import wraps
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

KEY = load_key()
CIPHER_SUITE = Fernet(KEY)

def auth_required(func):
    """Dekorator wymagający uwierzytelnienia przed wykonaniem operacji."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        password = getpass.getpass("Podaj główne hasło: ")
        if password == "admin123":
            return func(*args, **kwargs)
        else:
            print("Niepoprawne hasło!")
            return None
    return wrapper

def log_operation(func):
    """Dekorator logujący operacje użytkownika."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"Użytkownik dodał wykonał operację : {func.__name__}, status operacji: {result}\n")
        return result
    return wrapper

def encrypt_password(password):
    """Szyfruje hasło za pomocą Fernet."""
    return CIPHER_SUITE.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Deszyfruje hasło za pomocą Fernet."""
    return CIPHER_SUITE.decrypt(encrypted_password.encode()).decode()

def save_passwords(passwords):
    """Zapisuje zaszyfrowane hasła do pliku JSON."""
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

def load_passwords():
    """Ładuje zaszyfrowane hasła z pliku JSON."""
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            return json.load(file)
    return []

@auth_required
@log_operation
def add_password(service, username, password):
    """Dodaje nowe zaszyfrowane hasło do bazy."""
    passwords = load_passwords()
    new_entry = {
        "service": service,
        "username": username,
        "password": encrypt_password(password)
    }
    passwords.append(new_entry)
    save_passwords(passwords)
    return "Hasło dodane."

@auth_required
@log_operation
def get_password(service):
    """Pobiera i deszyfruje hasło dla danej usługi."""
    passwords = load_passwords()
    matching = []
    for entry in passwords:
        if entry["service"] == service:
            matching.append(entry)
    if not matching:
        return "Nie znaleziono hasła."
    print(f"Znaleziono {len(matching)} wpis(y):")
    for i, entry in enumerate(matching, 1):
        print(f"{i}. Login: {entry['username']}, Hasło: {decrypt_password(entry['password'])}")
    return "Pobrano hasła."


@auth_required
@log_operation
def delete_password(service, username):
    """Usuwa hasło dla danego serwisu i loginu."""
    passwords = load_passwords()
    for entry in passwords:
        if entry["service"] == service and entry["username"] == username:
            passwords.remove(entry)
            save_passwords(passwords)
            return "Wpis został usunięty"
    return "Nie znaleziono hasła dla podanych danych"

@auth_required
@log_operation
def check_known_sites():
    """"Sprawdzanie serwisów do których mamy zapisane hasło"""
    password = load_passwords()
    if password == []:
        return "Nie masz żadnych haseł"
    sorted_password = sorted(password, key=lambda x: x['service'])
    for entry in sorted_password:
            print(f"Serwis: {entry['service']} Login: {entry['username']}")
    return "To już wszystkie hasła"

@auth_required
@log_operation
def check_breaches():
    passwords = load_passwords()
    decrypted_passwords = []

    for entry in passwords:
        decrypted_entry = {
            "service": entry["service"],
            "username": entry["username"],
            "password": decrypt_password(entry["password"])
        }
        decrypted_passwords.append(decrypted_entry)

    breach_manager(decrypted_passwords)
    return "Sprawdzanie zakończone."


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
        
        if choice == "1":
            service = input("Podaj nazwę portalu: ")
            username = input("Podaj login: ")
            password = input("Podaj hasło: ")
            print(add_password(service, username, password))
        elif choice == "2":
            service = input("Podaj nazwę usługi: ")
            print(f"{get_password(service)}")
        elif choice == "3":
            service = input("Podaj nazwę usługi: ")
            username = input("Podaj login: ")
            print(delete_password(service, username))
        elif choice == "4":
            print(check_known_sites())
        elif choice == "5":
            check_breaches()
        elif choice == "6":
            break
        else:
                print("Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()

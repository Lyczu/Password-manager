import hashlib
import requests


def check_password_pwned(password: str) -> int:
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}")

    lines = response.text.split("\n")
    hashes = (line.split(':') for line in lines)
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)
    return 0

def breach_manager(decrypted_passwords: list[dict]):
    for entry in decrypted_passwords:
        service = entry['service']
        username = entry['username']
        password = entry['password']
        num_breaches = check_password_pwned(password)
        if num_breaches > 0:
            print(f"!!!! Hasło dla konta '{username}' w serwisie '{service}' wyciekło {num_breaches} razy!!!!")
        else:
            print(f"Hasło dla konta '{username}' w serwisie '{service}' jest bezpieczne.")
    input("Kliknij Enter, by wrócić do menu")

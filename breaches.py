import hashlib
import requests



def get_passwords_from_database() -> list[str]:
    mock_password = {"google": "test", "motorolla": "asasdasd@$!!LLoosd(())"}
    return mock_password

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

def breach_manager():
    passwords = get_passwords_from_database()

    for site in passwords.keys():
        num_breaches = check_password_pwned(passwords[site])
        print(f"Password on {site}, pwned {num_breaches} times")
    input("Kliknij cokolwiek by wrocic")

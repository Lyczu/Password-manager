### Zad 2
#Zaimplementuj dekorator authorize, który sprawdza czy użytkownik ma odpowiednie uprawnienia
#Jeśli użytkownik nie ma uprawnień, funkcja nie powinna się wykonać – zamiast tego wypisz "Brak dostępu"

def authorize(func):
    # Pisz tutaj
    pass

@authorize
def delete_post(user, post_id):
    print(f"Post {post_id} usunięty!")

@authorize
def edit_post(user, post_id, content):
    print(f"Post {post_id} edytowany: {content}")

class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin

admin = User("Admin", True)
guest = User("Gość", False)

delete_post(admin, 123)  # powinno się wykonać
delete_post(guest, 456)  # powinno wypisać "Brak dostępu"
edit_post(admin, 789, "Nowa treść")  # powinno się wykonać
edit_post(guest, 999, "Nielegalna edycja")  # powinno wypisać "Brak dostępu"

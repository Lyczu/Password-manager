### Zad 3
#Twoim zadaniem będzie zaimplementowanie dekoratora call_counter,
#który będzie zliczał, ile razy dana funkcja została wywołana
#Po każdym wywołaniu funkcji powinien wypisywać: "Funkcja <nazwa> została wywołana <X> razy"

# Możesz skorzystać z globalnego słownika ( zainicjować słownik poza funkcjami )


def call_counter(func):
    # TODO
    pass

@call_counter
def greet(name):
    return f"Cześć, {name}!"

@call_counter
def square(x):
    return x * x

print(greet("Ala"))
print(greet("Ola"))
print(square(4))
print(square(5))
print(greet("Ela"))
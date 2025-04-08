### ZADANIE NR 4
# Twoim zadaniem jest stworzenie klasy `InterfaceChecker`, która będzie metaklasą,
# sprawdzającą, czy klasa zawiera wymagane metody i atrybuty.
# Jeśli klasa nie będzie miała odpowiednich metod lub atrybutów, należy rzucić TypeError


class InterfaceChecker(type):
    def __new__(cls, name, bases, dct):
        # Lista wymaganych metod i atrybutów
        required_methods = ['run']
        required_attributes = ['status']

        # TODO sprawdz czy klasa ma metody

        # TODO sprawdz czy klasa ma atrybuty

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InterfaceChecker):
    pass
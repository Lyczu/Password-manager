### ZADANIE NR 1
# Twoim zadaniem bedzie implementacja loggera dla funkcji matematycznych
# Logger nie powinien zmieniać działania funkcji, mają one działać tak jakby go nie było
# Logger ma za zadanie printować nazwe funkcji którą obsługuje, argumenty i wynik


def logger(func):
    # Implementuj tutaj 
    pass # <- to usuń :)

@logger
def add(a, b):
    return a + b

@logger
def subtract(a, b):
    return a - b

@logger
def multiply(a, b):
    return a * b

result_add = add(3, 4)
result_subtract = subtract(10, 4)
result_multiply = multiply(6, 7)

assert result_add == 7, f"Zły wynik: {result_add}"
assert result_subtract == 6, f"Zły wynik: {result_subtract}"
assert result_multiply == 42, f"Zły wynik: {result_multiply}"
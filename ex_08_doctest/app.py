#Napisz doctesty dla poniższych funkcji

def factorial(n):
    """
    Oblicza silnię liczby n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """
    Generuje ciąg Fibonacciego do n-tego elementu.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sum(sequence[-1:-3:-1]))
    return sequence


def is_prime(n):
    """
    Sprawdza, czy liczba jest liczbą pierwszą.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def contain_uniques(lst):
    """
    Zwraca listę unikalnych elementów z listy.
    """
    return (set(lst)) == len(lst)



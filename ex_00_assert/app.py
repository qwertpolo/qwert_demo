from functools import reduce

# Dla poniższej funkcji napisz testy sprawdzające czy:
# funkcja poprawnie wykonuje dodawanie dwóch argumentów
# funkcja poprawnie wykonuje mnożenie dwóch argumentów
# funkcja poprawnie wykonuje potęgowanie dwóch argumentów
# funkcja poprawnie wykonuje dodawanie wielu argumentów
# funkcja poprawnie wykonuje mnożenie wielu argumentów
# funkcja poprawnie wykonuje potęgowanie wielu argumentów
# czy każda z powyższych operacji jest asocjatywna - czyli czy możemy zamieniać argumentów
# czy domyślnie wykonywane jest doddawanie


def ass(*args: int | float, operator: str = "+") -> int | float:
    """Takes arguments and does designated associative operation. Default operation is addition."""
    dic = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "**": lambda a, b: a**b,
    }
    return reduce(dic[operator], args)

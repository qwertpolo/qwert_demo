# sprawdź czy funkcja wyświetla odwrócone werotści:
# - dla jednego argumentu
# - dla wielu argumentów
# - dla argumentów nie bedących stringami
# - argument 'end' ma się wyświetlić na końcu, a nie na początku, sprawdź czy tak jest 

def reverse_print(*args, **kwargs): print(*(str(arg)[::-1] for arg in args[::-1]), **kwargs)


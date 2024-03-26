import random

_n_ = input("Level:")

try:
    x = random.randrange(1, int(_n_))
    while True:
        if int(_n_) < x:
            print("Too small!")
            _n_ = input("Geuss:")
        elif int(_n_) > x:
            print("Too large!")
            _n_ = input("Geuss:")
        elif int(_n_) == x:
            print("Just right!")
            break
except (ValueError, TypeError):
    _n_ = input("Level:")

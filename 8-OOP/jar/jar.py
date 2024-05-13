class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number of cookies cannot be negative.")
        if self._cookies + n > self._capacity:
            raise ValueError("Cookie amount exceeds jar capacity!")
        self._cookies += n  # checks for errors with cap and size then adds to size

    def withdraw(
        self, n
    ):  # reads from size and cap in self, and uses n(the inputed data)
        # to then minus from n to reformat, catching errors in the way
        if n < 0:
            raise ValueError("Number of cookies cannot be negative.")
        if self._cookies - n < 0:
            raise ValueError("Not enough cookies to take!")
        self._cookies -= n

    @property  # sets capacity again, so that any call for capacity in self leads to cap
    def capacity(self):
        return self._capacity

    @property  # ^^^^
    def size(self):
        return self._cookies

    @size.setter  # actually creates the property of self
    def size(self, value):
        if value < 0 or value > self._capacity:
            raise ValueError("Invalid size: must be between 0 and capacity.")
        self._cookies = value


def tester():
    jar = Jar()
    jar.deposit(11)
    print(jar)


tester()

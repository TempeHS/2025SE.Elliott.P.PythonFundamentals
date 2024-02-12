x = float(input("what is your first number?"))
y = input("what is your operator")
z = float(input("what is your second number!?"))

x = round(x, 1)
z = round(z, 1)


def changer():

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/" or y == "%":
        print(x / z)
    elif y == "*" or y == "x":
        print(x * z)


changer()

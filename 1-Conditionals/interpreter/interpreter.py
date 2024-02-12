x = float(input("what is your first number?"))
y = input("what is your operator")
z = float(input("what is your second number!?"))

x = round(x, 1)
z = round(z, 1)


def changer():
    # match y:
    # case "+":
    # print(x + z)
    # case "-":
    # print(x - y)
    # case "*":
    # print(x * z)
    # case "/" | "%":
    # print(x / z)
    # case _:
    # print("syntax error")
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/" or y == "%":
        print(x / z)
    elif y == "*" or y == "x":
        print(x * z)
    else:
        print("SYNTAx eRROR!")


changer()

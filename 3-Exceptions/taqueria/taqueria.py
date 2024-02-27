taqueria_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

order = input("what would you like from the taqueria?")
total = 0
try:
    while order != "control-d":
        if order in taqueria_menu:
            total = float(total) + float(taqueria_menu[order])
            print(total)
            print(order)
            order = input("anything else?")

        if order == "control-d":
            break


except EOFError:
    print("WRONG")

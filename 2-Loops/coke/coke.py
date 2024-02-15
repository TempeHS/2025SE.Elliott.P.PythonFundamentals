def vending_machine():
    total = 0
    while total < 50:
        coin = int(
            input(
                "Insert a coin (accepted denominations: 25 cents, 10 cents, 5 cents): "
            )
        )
        if coin not in [5, 10, 25]:
            print(
                "Coin of ",
                coin,
                " cents is not accepted. Please insert a coin: 25, 10 or 5 cents",
            )
            continue
        else:
            total += coin
            due = 50 - total
            if due > 0:
                print("Amount due: ", due, " cents")
                continue
            elif due <= 0:
                change = total - 50
                print("*Coke can dispensed*")
                print("Your change is ", change, " cents")
                break


# Call the program
vending_machine()

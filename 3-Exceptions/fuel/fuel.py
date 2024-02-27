while True:
    try:
        amount = input("Enter the fractional tank amount in the format 'fuel/tank': ")
        feul, tank = amount.split("/")
        feul = int(feul)
        tank = int(tank)

        if tank == 0:
            print(
                "The tank amount cannot be zero. Please enter a valid fractional amount."
            )
            continue

        percent = (feul / tank) * 100

        if 100 >= percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        elif percent > 100:
            print("Incorrect amount. The fuel amount can't be more than the tank size.")
            continue
        else:
            print(f"The tank is {percent}% full.")
        break

    except (ValueError, ZeroDivisionError):
        print(
            "Invalid input. Please make sure both the fuel and tank amounts are integers. and not 0"

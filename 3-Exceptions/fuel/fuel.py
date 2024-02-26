while True:
    try:

        amount = input("Enter how much fuel is in the tank (only as a fraction) ")
        x, y, z = [fuel for fuel in amount]
        x = int(x)
        z = int(z)
        percent = (x / z) * 100
        if 100 >= percent >= 99:
            print("F")
        elif percent <= 1:
            print("E")
        elif percent > 100:
            print("Incorrect amount")
            continue
        else:
            print(percent, "%")
        break

    except (ValueError, ZeroDivisionError):
        print("Input is not an integer")
        continue

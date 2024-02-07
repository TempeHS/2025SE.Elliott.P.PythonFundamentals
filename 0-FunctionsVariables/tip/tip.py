def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    dollars = dollars.strip("$")
    return float(dollars)


def percent_to_float(percent):
    percent = percent.strip("%")
    return float(percent) / 100


main()

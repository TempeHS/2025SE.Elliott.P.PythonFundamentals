def main():
    # input
    time = input("Enter time: ")
    # convert into readable numbers
    converted_time = convert(time)
    # check if time is 7> and <8 and so on
    if 7 <= converted_time <= 8:
        print("It's breakfast time.")
    elif 12 <= converted_time <= 13:
        print("It's lunch time.")
    elif 18 <= converted_time <= 19:
        print("It's dinner time.")


def convert(time):
    # turns "7:30" into "7" : "30"
    hours, minutes = time.split(":")
    # return int("7") + float("30)/60,
    return int(hours) + float(minutes) / 60


main()

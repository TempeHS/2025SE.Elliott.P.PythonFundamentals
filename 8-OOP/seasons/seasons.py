from datetime import date, datetime
import sys
import inflect


def main():
    user_input = input("Please enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(
            user_input, "%Y-%m-%d"
        ).date()  # try to turn user date into datetime obj, strptime takes out all available numbers
    except ValueError:  # if doesnt fit then exit
        print("Invalid date format. Please use YYYY-MM-DD format.")
        sys.exit(1)

    today_date = date.today()
    if birth_date > today_date:  # catch "incorect" date errors
        print("Birth date cannot be in the future.")
        sys.exit(1)

    total_minutes = calculate_minutes(
        birth_date, today_date
    )  # calls calculate minutes, start=birth, end= today
    print_minutes_in_words(total_minutes)


def calculate_minutes(
    start_date, end_date
):  # minute calculator for the time since birth, import start and end
    delta = end_date - start_date  # total days since birth
    total_minutes = (
        delta.days * 24 * 60
    )  # days * hours * minutes = total minutes form days
    return total_minutes


def print_minutes_in_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes)
    print(f"You are {words} minutes old.")  # inflect will handle all the grammar,


if __name__ == "__main__":
    main()

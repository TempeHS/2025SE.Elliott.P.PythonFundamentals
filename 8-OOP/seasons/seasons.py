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
    today_date = datetime.today()
    if birth_date > today_date:  # catch "incorect" date errors
        print("Birth date cannot be in the future.")
        sys.exit(1)

    class Minutes:

        def calculate_minutes(start, end):
            delta = start - end
            total_minutes = (
                delta.day * 24 * 60
            )  # days * hours * minutes = total minutes form days
            return total_minutes

        def print_minutes_in_words(minutes):
            p = inflect.engine()
            words = p.number_to_words(minutes)
            print(
                f"You are {words} minutes old."
            )  # inflect will handle all the grammar,

    total_minutes = Minutes.calculate_minutes(today_date, birth_date)
    # calls calculate minutes, start=birth, end= today
    Minutes.print_minutes_in_words(total_minutes)


if __name__ == "__main__":
    main()

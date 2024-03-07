def outdated():
    month_mapping = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }
    while True:
        date_input = input(
            "Enter a date in MM/DD/YYYY or Month DD, YYYY format: "
        ).strip()
        if "/" in date_input:
            month, day, year = date_input.split("/")
            if validate_date(month, day, year):
                print(year.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2))
                return
        elif "," in date_input:
            month, day_year = date_input.split(" ", 1)
            day, year = day_year.replace(",", "").split()
            month = month_mapping[month]
            if validate_date(month, day, year):
                print(year.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2))
                return
        print("Invalid date. Please try again.")


def validate_date(month, day, year):
    return 1 <= int(month) <= 12 and 1 <= int(day) <= 31


if __name__ == "__main__":
    outdated()

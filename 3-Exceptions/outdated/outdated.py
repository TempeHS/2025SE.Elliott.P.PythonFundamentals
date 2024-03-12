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
        if "/" in date_input:  # if 1/2/3333
            month, day, year = date_input.split("/")
            if validate_date(month, day, year):
                print(year.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2))
                return
        elif "," in date_input:  # if January the second, 3333
            month, day_year = date_input.split(" ", 1)  # [January] { } [second]
            day, year = day_year.replace(",", "").split()  # [second] {,} [3333]
            month = month_mapping[month]  # month_mapping[January] >>>1
            if validate_date(month, day, year):
                print(year.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2))
                return
        print("Invalid date. Please try again.")


def validate_date(month, day, year):
    return 1 <= int(month) <= 12 and 1 <= int(day) <= 31
    # return if value is <= 12 or value is <=31
    # if it isnt it will return false


if __name__ == "__main__":
    outdated()

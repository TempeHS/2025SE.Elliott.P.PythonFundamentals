from tabulate import tabulate


def main():
    userFile = input("What file? file path from /2025SE.Elliott.P.PythonFundamentals")
    try:
        with open(userFile, "r") as file:
            headers = file.readline().rsplit(",")
            table = []
            for line in file:
                item = line.rsplit(",")
                table.append(item)

            print(tabulate(table, headers, tablefmt="grid"))
    except (FileNotFoundError, FileExistsError):
        print("this file does not exsist")


if __name__ == "__main__":
    main()

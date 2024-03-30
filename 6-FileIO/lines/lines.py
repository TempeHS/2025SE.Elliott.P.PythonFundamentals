query = input("What is the name of the file? ")
i = 0
blankLine = 0


def lineCheck(line):
    global blankLine
    if line.startswith("#") or line.isspace():
        blankLine = blankLine + 1
    return blankLine


try:
    with open(query, "r") as file:
        lines = file.readlines()
        for line in lines:
            lineCheck(line)
            i = i + 1
    i = i - lineCheck(line)
    print(f"There are: {i} number of lines")

except FileNotFoundError:
    raise SystemExit

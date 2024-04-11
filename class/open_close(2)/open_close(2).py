import sys


# while True:
print("hello welcome to text edito")
command = input(
    "what would you like to do to object!?"
    "1. read file conents?"
    "2. change file contents?"
    "3. close?"
)

if command == "1":
    with open("class/open_close(2)/myText.txt", "r") as file:
        for line in file:
            print(line)
elif command == "3":
    print("k")
    sys.exit
elif command == "2":
    change = input(
        "how would u like to change"
        "1. input a number to put in?"
        "2. increment by x?"
        "3.close?"
    )
    if change == "1":
        newLines = []
        lines = []
        with open("class/open_close(2)/myText.txt", "r") as file:  # read the file
            for line in file:  # for (every line) in (mytxt)
                lines.append(line)
                print(line)
                newLine = input("what do u wana put in!?")  # define the input
                newLines.append(newLine)  # put each input in a list
        with open("class/open_close(2)/myText.txt", "w") as file:
            for i in range(len(newLines)):
                file.write(newLines[i])
                file.write("\n")
    elif change == "2":
        x = input("what is x?")

        with open("class/open_close(2)/myText.txt", "r") as file:  # read the file
            for line in file:  # for (every line) in (mytxt)
                number = int(line)  # assign number to waht the line says
                answer = number + int(x)  #  inc
                # stop reading(!!)
        with open(
            "class/open_close(2)/myText.txt", "w"
        ) as file:  # now CREATE THE FILE AGAINf
            file.write(f"{answer}")  # WITH EACH LINE REMADE!!

with open("myText.txt", "r") as file:
    for line in file:
        number = int(line)
        answer = number + 1

with open("myText.txt", "w") as file:
    file.write(f"{answer}")

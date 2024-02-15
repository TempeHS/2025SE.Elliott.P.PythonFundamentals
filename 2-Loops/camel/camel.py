name = input("input camelcase var")
print("snake case ver is: ", end="")


for letter in name:

    if letter.isupper():
        print("_" + letter, end="")

    else:
        print(letter, end="")

print()

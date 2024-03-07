list = {}

while True:
    try:
        item = input("what would you like to add to the list !?")
        item = item.lower().lstrip()
        if item in list:
            list[item] + 1
        elif item not in list:
            list[item] = 1
    except EOFError:
        break
num = 0
it = 0
for it, num in list.items():
    print(f"{num} {it}")

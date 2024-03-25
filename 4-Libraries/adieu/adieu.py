import inflect

p = inflect.engine()
names = []
while True:
    try:
        print("Enter names: ")
        names.append(input())
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names)}")

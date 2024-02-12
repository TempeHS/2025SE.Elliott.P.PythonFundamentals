poopFingleBottom = input("what is the answer to the universe")
poopFingleBottom = poopFingleBottom.strip(" ").lower()
if (
    poopFingleBottom.__contains__("42")
    or poopFingleBottom.__contains__("fortytwo")
    or poopFingleBottom.__contains__("forty-two")
):
    print("Yes.")
else:
    print("end your life")

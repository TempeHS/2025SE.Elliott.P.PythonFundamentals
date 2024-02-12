variable = input("say hello")
variable = variable.strip(",").lower()

if variable.startswith("h") and variable.__contains__("hello"):
    print("0$")
elif variable.startswith("h"):
    print("20$")
else:
    print("$100")

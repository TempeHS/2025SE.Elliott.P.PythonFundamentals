from pyfiglet import Figlet

figler = True
while figler:

    f = Figlet(font="chunky")
    text = input(
        "if you want to change font start with -f or --font, start with what do you want to render!?"
    )
    if text.startswith("-f"):
        text = text.removeprefix("-f ")
        print("selected font:", text)
        f = Figlet(font=text)
        second = input("now what to render?")
        print(f.renderText(second))
    elif text.startswith("--font"):
        text.removeprefix("--font")
        print(text)
        f = Figlet(font=text)
        second = input("now what to render?")
        print(f.renderText(second))
    elif text == "sys.exit":
        break
    else:
        print(f.renderText(text))
print("sorry! close succesful")

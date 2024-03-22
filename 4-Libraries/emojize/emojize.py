import emoji

text = input("INSERT YOUR EMOJI IN :xxx:")

if text.isalpha:
    print(emoji.emojize(text, language="alias"))
else:
    print("INVALID")

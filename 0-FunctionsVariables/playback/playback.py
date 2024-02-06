# defome input string as returning "replace" with every " " as a "..."
def playback(input_str):
    return input_str.replace(" ", "...")


# asking user for sentence
user = input("Enter a sentence: ")
# reading conversion
result = playback(user)
# printing converted version
print(result)

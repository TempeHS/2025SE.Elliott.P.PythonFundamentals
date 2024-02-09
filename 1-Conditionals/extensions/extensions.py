def extract_user_input():
    # Empty list to store detected formats
    formats = []

    # strip spaces
    words = user_input.split()
    # keep last 4 letter in string if it is .jog or .gif
    for word in words:
        if (
            word.endswith(".jpg")
            or word.endswith(".gif")
            or word.endswith(".png")
            or word.endswith(".pdf")
            or word.endswith(".txt")
            or word.endswith(".zip")
        ):
            formats.append(word[-4:])
        else:
            print("application/octet-stream")

    return formats


user_input = input("Please enter your string: ")
# print result
print(extract_user_input())

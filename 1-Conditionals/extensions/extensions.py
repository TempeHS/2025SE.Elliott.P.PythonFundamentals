def extract_user_input():
    # Empty list to store detected formats
    formats = []

    # strip spaces
    words = user_input.split()
    # keep last 4 letter in string if it is .jpg or .gif
    for word in words:
        if word.endswith(".jpg") or word.endswith(".jpeg"):
            print("image/jpg")
        elif word.endswith(".png"):
            print("image/png")
        elif word.endswith(".pdf"):
            print("applications/pdf")
        elif word.endswith(".txt"):
            print("applications/txt")
        elif word.endswith(".zip"):
            print("applications/zip")

        else:
            print("application/octet-stream")

    return formats


user_input = input("Please enter your string: ")
# print result
print(extract_user_input())

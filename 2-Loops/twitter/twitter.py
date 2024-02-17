# file name: twttr.py


def remove_vowels(text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = "".join([char for char in text if char not in vowels])
    return result


user_input = input("Please enter your text: ")
print(remove_vowels(user_input))

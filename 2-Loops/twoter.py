# file name: twttr.py


def remove_vowels(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = "".join([char for char in text if char not in vowels])
    return result


user_input = input("Please enter your text: ")
user_input = user_input.lower()
print(remove_vowels(user_input))

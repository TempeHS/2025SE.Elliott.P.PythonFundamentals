import random


# def main():
def get_level():
    level = input("select a number, 1, 2 or 3")
    if level == "1" or "2" or "3":
        return level
    else:
        get_level()


print(get_level())

def generate_integer(level):
    


# if __name__ == "__main__":
# main()

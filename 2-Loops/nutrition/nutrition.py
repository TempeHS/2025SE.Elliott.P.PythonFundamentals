def main():
    fruit = input("please enter your fruit")
    fruit = fruit.lower().lstrip()
    # make dictionary of fruits : calories
    Fruits_calories = {
        "strawberries": "50",
        "lime": "20",
        "banana": "110",
        "apple": "130",
        "grapefruit": "60",
        "grapes": "90",
        "pear": "100",
        "kiwifruit": "90",
        "lemon": "15",
        "cantaloupe": "50",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "honeydew melon": "50",
        "pineapple": "50",
        "plums": "70",
        "avocado": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }
    if fruit in Fruits_calories:
        # print from dict [the value of what ever key represented by input]
        print(Fruits_calories[fruit])


main()

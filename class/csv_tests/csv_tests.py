with open("class/csv_tests/students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        # ROW= LINE.REMOVE WHITE, REMOVOVE COMMA
        # print( {first array val}) is in {second array val}

name = input("what is your name?")
# "w" opens the folder BRANDNEW to write
# "a" APPENDS to the file
# with opens the folder then closes once done with everything
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# HOW TO READ A FILEIO FOLDER!!!!!
# read opens the folder, no editing!!
with open("names.txt", "r") as file:
    # STORES ALL THE DATA IN THE FOLDER IN A
    # VARIABLE CALLED LINES
    lines = file.readlines()
for line in lines:
    print(line)
    # TO THEN STORE THIS DATA WE CAN JUST
    # with open("names.txt" #no op) as file:
    # for line in file:
    # list.append(line)!!!

# documentation has more methods!!

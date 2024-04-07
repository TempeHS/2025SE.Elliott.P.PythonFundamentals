import csv
import sys

if len(sys.argv) > 3:
    print("too many command line args")
    sys.exit
elif len(sys.argv) < 3:
    print("too few command line args")
    sys.exit
input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    with open(input_file, "r") as csv_file:
        # read and store the file
        recipiants = list(csv.reader(input_file))
        # reader will store each row with split stuff
        recipiants.pop(0)
except IOError:
    print("file does not exsist, or cannot be read")
    sys.exit

    try:
        with open(input_file, "w") as csv_file:
            writer = csv.writer(input_file)
            writer.writerow("first name, last name, house")
            for recipiant in recipiants:
                name, house = recipiant
                first_name, last_name = name.split(", ")
                writer.writerow([last_name, first_name, house])

    except IOError:
        print("couldnt write to that file")
        sys.exit

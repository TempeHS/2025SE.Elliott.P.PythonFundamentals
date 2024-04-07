import csv
import sys

# Verify the correct number of command-line arguments
if len(sys.argv) != 3:
    print("Usage: python scourgify.py input.csv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the input CSV file
try:
    with open(input_file, "r") as csv_file:
        students = list(csv.reader(csv_file))
        students.pop(0)  # remove the header
except IOError:
    print("Unable to open", input_file)
    sys.exit(1)

# Write to the output CSV file
try:
    with open(output_file, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["first", "last", "house"])
        for student in students:
            name, house = student
            first_name, last_name = name.split(", ")
            writer.writerow(
                [last_name, first_name, house]
            )  # switches the order form the original file
except IOError:
    print("Failed to write to", output_file)
    sys.exit(1)

print("Successfully formatted", input_file, "and wrote to", output_file)

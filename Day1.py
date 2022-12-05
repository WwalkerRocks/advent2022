# Open the file and read the lines into a list
with open("C:/Users/wdawg/OneDrive/Documents/github/Advent-of-Code/numbers.txt", "r") as f:
    lines = f.readlines()
# Creates a list and a session variable
sums = []
session_number = 0
# Reads through the file
for line in lines:
    # Detects if the line is a space, if so it appends the session number to the list and resets the sessions
    if line.strip() == "":
        sums.append(session_number)
        session_number = 0
    else:
        session_number += int(line)
# Appends the final session
sums.append(session_number)
# sorts the list and prints the top 3 added together
sums.sort(reverse = True)
print(sums[0] + sums[1] + sums[2])

# Open rockpaperscissors.txt file
# Read a line, determine the amount of points for the type
# determine the amount of points for W/L/D
# Add points to a total point system
# Move on to next line
# Print at the end

with open("C:/Users/wdawg/OneDrive/Documents/github/Advent-of-Code/rockpaperscissors.txt", "r") as f:
    lines = f.readlines()
# Rock = +1, Paper = +2, Scissors = +3, Z = +6 Y = +3 X = +0
# A = Rock, B = paper, C = Scissors
points = 0
for line in lines:
    if line.strip() == "A X":
        points += 3
    elif line.strip() == "A Y":
        points += 4
    elif line.strip() == "A Z":
        points += 8
    elif line.strip() == "B X":
        points += 1
    elif line.strip() == "B Y":
        points += 5
    elif line.strip() == "B Z":
        points += 9
    elif line.strip() == "C X":
        points += 2
    elif line.strip() == "C Y":
        points += 6
    elif line.strip() == "C Z":
        points += 7
print(points)
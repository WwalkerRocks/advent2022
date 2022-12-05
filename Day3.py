# A progrma that opens rucksack.txt
# reads the first line, divides it into two portions
# finds any duplicates between the two portions
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# adds the priority to a priority counter
# moves onto the next line


with open('c:/Users/wdawg/OneDrive/Documents/github/Advent-of-Code/rucksack.txt', 'r') as rucksack_file:
    # Initialize a counter to keep track of the total priority
    total_priority = 0

    # Iterate through each line in the file
    for line in rucksack_file:
        # Use the length of the line to split it in half
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        # Use sets to find any duplicates between the two halves
        duplicates = set(first_half) & set(second_half)

        # Iterate through each duplicate and add its priority to the total
        for char in duplicates:
            if char.islower():
                # Lowercase characters have priorities 1 through 26, takes the ascii version of the character, subtracts
                # the lowest character in the lower/upper ascii line, then adds 1 or 27 to make it work
                total_priority += ord(char) - ord('a') + 1
            elif char.isupper():
                # Uppercase characters have priorities 27 through 52
                total_priority += ord(char) - ord('A') + 27

    # Print the total priority
    print(total_priority)
# Problem Set 2019 - Problem 9
# Peter McGowan
# Started 2019-03-22

# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

import sys # Import sys to allow taking filename as command line argument

inputFile = sys.argv[1] # Import file from command line argument

i = 1 # Iterator to allow checking if lines are even or odd numbered, initialised as 1 for Line 1
with open(inputFile, 'r') as f:  # Open file from command line argument to read only and name it "f"
    for l in f.readlines(): # For loop to iterate through each line (l) of the input file
        if i % 2 != 0 : # Check if line is odd numbered - to print every alternate line from Line 1
            print(l.rstrip('\n')) # Print line with the newline character \n stripped from the end
        i += 1 # Increment i by 1

    f.close() # closing file at end
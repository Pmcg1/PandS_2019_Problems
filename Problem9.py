# Problem Set 2019 - Problem 9
# Peter McGowan
# Started 2019-03-22

# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

import sys

inputFile = sys.argv[1] # import file from command line argument

with open(inputFile, 'r') as f:

    for l in f:
        print(l.rstrip('\n'))
        if l == f: # if statement attempting to fix odd lines end problem, not currently working
            break
        else:
            next(f)

    f.close() # closing file at end



# Problem Set 2019 - Problem 3
# Peter McGowan
# Started 2019-02-02

# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

# Set iterator to 1000
i = 1000

while i <= 10000: # run through loop, stopping when i reaches 10000

    # if and else, both increase iterator by i
    # check two conditions together, that the remainder of i/6 is 0 and that the remainder of 1/12 is not zero
    if ((i % 6 == 0) and (i % 12 != 0)) :
        print(i) # If both conditions are met then i is printed
        i += 1
    else:
        i += 1
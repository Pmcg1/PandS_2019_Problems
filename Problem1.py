# Problem Set 2019 - Problem 1
# Peter McGowan
# Started 2019-01-30

# Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

# user input, explicitly expects an integer, otherwise returns an error
i = int(input('Input any positive integer: '))

# Set output counter to 0
j = 0

# if a positive integer is detected, print result of while loop
if i > 0:
    while i > 0:  # repeat loop as long as i is a minimum of 1
        j = j + i # updated j by adding current value of i
        i = i - 1 # decrement i by 1 until it reaches 1
    print("Output: ",j)

# if a negative integer is input, print the following
else:
    print("You have not entered a positive integer!")


# Problem Set 2019 - Problem 4
# Peter McGowan
# Started 2019-02-02

# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

# User input, explicitly expects an integer, otherwise returns an error
i = int(input('Please enter a positive integer: '))

# Check that integer is positive
if i > 0:

    # While loop will repeat as long as i is not egual to 1
    while i != 1:
        # Print i and end print statement with a space rather than a newline
        # Explicitly print i as an integer as the odd/even check will convert it to a float
        print(int(i), end=' ')
        # Check if i is an even number
        if i % 2 == 0:
            i = i/2 # If so, divide i by 2

        # If i is odd do the following
        else:
            i = (3 * i)+1 # Multiply i by 3 and add 1

    print (int(i)) # Print the final result of the calculations

else:
    print("That is not a positive integer")
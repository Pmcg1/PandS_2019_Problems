# Problem Set 2019 - Problem 7
# Peter McGowan
# Started 2019-02-22

# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

import math # Import the math module, for sqrt function

# user input, explicitly expects a positive floating point number, otherwise returns an error
i = float(input('Please enter a positive number: '))

# Check that float is positve
if i < 0:
    print("That is not a positive number") # If negative, print this message

elif i == 1:
    print("The square root of 1 is 1") # If input number is 1 then print this

else:
    print("The square root of ", i, " is approx. ",round(math.sqrt(i),1),".",sep='') # In all other cases, print the message with the square root calculated by the math.sqrt function, rounded to 1 decimal place






# Problem Set 2019 - Problem 7
# Peter McGowan
# Started 2019-02-22

# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

j = 1.0 # Initial guess for calculation

# user input, explicitly expects a positive floating point number, otherwise returns an error
i = float(input('Please enter a positive number: '))

# Check that float is positve
if i < 0:
    print("That is not a positive number") # If negative, print this message

elif i == 1:
    print(f"The square root of 1 is 1") # Print only if 1 is input as the square

else:
    while abs((j * j) - i) > 0.01: # WHile loop will iterate until difference between estimate squared and the input number is 0.01 or less
        j -= ((j * j) - i) / (2 * j) # Implementation of Newton's method for approximating a square root

    print(f"The square root of {i} is approx. {round(j,5)}") # In all other cases, print this approximation of the square root, rounded to 5 decimal places


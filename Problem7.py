# Problem Set 2019 - Problem 7
# Peter McGowan
# Started 2019-02-22

# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# user input, explicitly expects a positive floating point number, otherwise returns an error
userInput = float(input('Please enter a positive number: '))

# Check that float is positve
if userInput < 0:
    print("That is not a positive number") # If negative, print this message

elif userInput == 1:
    print(f"The square root of 1 is 1") # Print only if 1 is input as the square

else:
    currentApprox = 0.5 * userInput # Initial guess for calculation

    while abs((currentApprox**2)-userInput) > 0.01: # While loop will iterate until difference between estimate squared and the input number is 0.01 or less
        currentApprox = 0.5 * (currentApprox+(userInput/currentApprox)) # Implementation of Newton's method for approximating a square root

    print(f"The square root of {userInput} is approx. {round(currentApprox,3)}") # In all other cases, print this approximation of the square root, rounded to 3 decimal places
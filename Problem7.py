# Problem Set 2019 - Problem 7
# Peter McGowan
# Started 2019-02-22

# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# user input, explicitly expects a positive floating point number, otherwise returns an error
i = float(input('Please enter a positive integer: '))

# Check that integer is a positive integer
if i > 0:
    if i == 1:
        print("That is a prime")

    else:

        for j in range (2, i):
            if i % j == 0:
                print("That is not a prime")
                break

            else:
                print("That is a prime")
                break

    

else:
    print("That is not a positive integer")






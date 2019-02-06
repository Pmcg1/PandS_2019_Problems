# Problem Set 2019 - Problem 5
# Peter McGowan
# Started 2019-02-02

# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

# user input, explicitly expects an integer, otherwise returns an error
i = int(input('Please enter a positive integer: '))

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






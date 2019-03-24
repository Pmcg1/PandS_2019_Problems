# Problem Set 2019 - Problem 5
# Peter McGowan
# Started 2019-02-02

# Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

# user input, explicitly expects an integer, otherwise returns an error
i = int(input('Please enter a positive integer: '))

# Check that integer is a positive integer
if i > 0:
    if i == 1: # Simple check for '1'
        print("That is a prime")

    else: # If input number isnt '1' then the for loop is initiated

        for j in range(2, i): # For-Else loop initiated starting at 2 and ending when the iterator equals i
            if (i % j) == 0: # Check to see if any facotrs other than 1 and i exist
                print("That is not a prime")
                break # Break out of for-else loop if number is found to not be a prime

        else:
            print("That is a prime") # Prints only when all iterations are complete and no factors other than 1 and i have been found

else:
    print("That is not a positive integer")

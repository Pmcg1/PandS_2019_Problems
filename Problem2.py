# Problem Set 2019 - Problem 2
# Peter McGowan
# Started 2019-02-01

# Write a program that outputs whether or not today is a day that begins with the letter T.

# Import datetime module
import datetime as dt

# Generate current date and time
now = dt.datetime.now()

# Extract Day from datetime as a string
Day = now.strftime("%a")

# Check if the first letter of Day is equal to T.
if Day[0] == "T":
    print("Yes - today begins with a T.") # If yes, print this

else:
    print("No - today does not begin with a T.") # If no, print this



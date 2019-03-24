# Problem Set 2019 - Problem 8
# Peter McGowan
# Started 2019-03-10

# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

from datetime import datetime as dt # import datetime module

i = dt.now() # current datetime is set as value of i

def suffix(d): # if statement to set correct suffix for the date
    if d in (1, 21, 31):
        return "st"    
    elif d in (2, 22):
        return "nd"
    elif d in (3, 23):
        return "rd"    
    else:
        return "th"

currentDate = i.strftime("%d") # extract current date from current datetime, to allow for removal of any leading zero
currentHour = i.strftime("%I") # extract current hour from current datetime, to allow for removal of any leading zero

print(f'{i.strftime("%A, %B ")}{int(currentDate)}{suffix(i.day)} {i.year} at {int(currentHour)}{i.strftime(":%M%p")}')

# f-string consisting of (full name of day), (full name of month) (date) (date suffix) (year) at (hour in 12hr clock):(minutes)(AM/PM)
# both the current date and current hour are explicitly declared as integers in order to remove any leading zero they may have


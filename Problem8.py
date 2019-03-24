# Problem Set 2019 - Problem 8
# Peter McGowan
# Started 2019-03-10

# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

from datetime import datetime as dt # import datetime module

i = dt.today() # current datetime is set as value of i

def suffix(d): # if statement to set correct suffix for the date
    if d in (1, 21, 31):
        return "st"    
    elif d in (2, 22):
        return "nd"
    elif d in (3, 23):
        return "rd"    
    else:
        return "th"

print(f'{i.strftime("%A, %B %d")}{suffix(i.day)} {i.year} at {i.strftime("%I:%M%p")}')


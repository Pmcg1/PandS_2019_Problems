# Problem Set 2019 - Problem 8
# Peter McGowan
# Started 2019-03-10

# Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

import datetime

todaysDate = datetime.datetime.now()
print(todaysDate) 


if todaysDate.strftime("%d") in (1, 21, 31):
    suffix = "st"

elif todaysDate.strftime("%d") in (2, 22):
    suffix = "nd"

elif todaysDate.strftime("%d") in (3, 23):
    suffix = "rd"    

else:
    suffix = "th"

print(todaysDate.strftime("%A, %B %d %Y at %I:%M%p"))
f(todaysDate.strftime("%A, %B %d {suffix} %Y at %I:%M%p")) #repair f string implementation

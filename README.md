# Programming and Scripting 2019 Problem Set
## g00190832 Peter McGowan

## Introduction

This contains my solutions to the Programming and Scripting 2019 Problem Set.

## License

This project is licensed under the Apache License 2.0 - see [LICENSE.md] for details.

## Prerequisites

This code was created in MS Visual Studio Code v1.32.3 using Python 3.7.1.
You will need to have Python 3.7.1 (or higher) installed to run these programmes.

Some of the programmes require the following libraries:
* datetime
* sys
* numpy
* matplotlib

The Anaconda Distribution is recommended. It can be downloaded from [here](https://www.anaconda.com/distribution/#download-section)

## Problem 1
> Write a program that asks the user to input any positive integer and outputs the
sum of all numbers between one and that number.

### Solution
[Problem1.py]
A user input is read from the command prompt ('Input any positive integer: '), explicitly declared as an integer and stored as the variable 'i'.
Another variable, 'j' is initialised as 0.

An if statement is used to check that the input is positive. If true, then a while loop is initiated. For each loop, 'j' is updated with the current value of 'i' and then 'i' is decremented by 1. The loop ends when 'i' is at 0, printing 'j'.

If the if statement is false, then the user is informed that they have not entered a positive integer.

### References

## Problem 2
> Write a program that outputs whether or not today is a day that begins with the
letter T. An example of running this program on a Thursday is as follows.

### Solution


### References

## Problem 3
> Write a program that prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.


### Solution


### References

## Problem 4
> Write a program that asks the user to input any positive integer and outputs the
successive values of the following calculation. At each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
it by three and add one. Have the program end if the current value is one.

### Solution


### References

## Problem 5
> Write a program that asks the user to input a positive integer and tells the user
whether or not the number is a prime.

### Solution


### References

## Problem 6
> Write a program that takes a user input string and outputs every second word.

### Solution


### References


## Problem 7
> Write a program that that takes a positive floating point number as input and outputs
an approximation of its square root.

### Solution


### References


## Problem 8
> Write a program that outputs today’s date and time in the format ”Monday, January
10th 2019 at 1:15pm”.

### Solution


### References


## Problem 9
> Write a program that reads in a text file and outputs every second line. The program
should take the filename from an argument on the command line.

### Solution


### References


## Problem 10
> Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

### Solution


### References


##General References

* [Stack Overflow](https://stackoverflow.com/)
* [W3 Schools](https://www.w3schools.com/python/default.asp)
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)



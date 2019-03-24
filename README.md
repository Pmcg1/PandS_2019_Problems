# Programming and Scripting 2019 Problem Set
## g00190832 Peter McGowan

## Introduction

This contains my solutions to the Programming and Scripting 2019 Problem Set.

## License

This project is licensed under the Apache License 2.0 - see [LICENSE.md](LICENSE) for details.

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
[Problem1.py](Problem1.py)

A user input is read from the command prompt ('Input any positive integer: '), explicitly declared as an integer and stored as the variable 'i'.
Another variable, 'j' is initialised as 0.

An if statement is used to check that the input is positive. If true, then a while loop is initiated. For each loop, 'j' is updated with the current value of 'i' and then 'i' is decremented by 1. The loop ends when 'i' is at 0, printing 'j'.

If the if statement is false, then the user is informed that they have not entered a positive integer.

### References
N/A

## Problem 2
> Write a program that outputs whether or not today is a day that begins with the
letter T. An example of running this program on a Thursday is as follows.

### Solution
[Problem2.py](Problem2.py)
Datetime module is imported to allow access to its functions.
The current date and time is assigned to a variable 'now', and the day is extracted from this using strftime.

The check is performed using an if statement. This checks is the first indexed element of the string 'Day' is equivalent to the letter 'T'.
The answer printed is then dependant of whether the if statement evaluates to true or false.

### References
* [W3 Schools](https://www.w3schools.com/python/python_datetime.asp)

## Problem 3
> Write a program that prints all numbers between 1,000 and 10,000 that are divisible
by 6 but not 12.

### Solution
[Problem3.py](Problem3.py)
This problem is solved using a while loop to iterate through the given range.

An initial value of 1000 is assigned to the iterator and the while loop runs until this reached 10000. On each iteration it uses an if statement to check to conditions (with the binary operator 'and'). The remainder of the iterator value divided by 6 is checked to make sure that it is true, and the remainder of the iterator divided by 12 is checked to make sure that it is false.

If this is evaluated as true, then the current value of the iterator is printed. Whether true or false, the iterator is incremented by 1.

### References
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)

## Problem 4
> Write a program that asks the user to input any positive integer and outputs the
successive values of the following calculation. At each step calculate the next value
by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
it by three and add one. Have the program end if the current value is one.

### Solution
[Problem4.py](Problem4.py)
Similarly to Problem 1, the user is asked to input a positive integer. The same if statement from Problem 1 is used to assess if the integer is positive.

The calculations are implemented as a while loop embedded into the if statement that will iterate until the value being assessed is equal to 1.
The while loop will first print the value, explicitly declaring it as an integer as the later checks can convert it to a float. The print statement includes the following parameter: `end=' '`.This allows all values to be printed on the same line.

An if statement is then implemented inside the while loop. It assesses if the value is positive using `if i % 2 == 0:`. If true, the value is halved, and if false the value is added to itself multiplied by 3. A final print statement is included following completion of the while loop to print the final value.

### References
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)

## Problem 5
> Write a program that asks the user to input a positive integer and tells the user
whether or not the number is a prime.

### Solution
[Problem5.py](Problem5.py)


### References

## Problem 6
> Write a program that takes a user input string and outputs every second word.

### Solution
[Problem6.py](Problem6.py)


### References


## Problem 7
> Write a program that that takes a positive floating point number as input and outputs
an approximation of its square root.

### Solution
[Problem7.py](Problem7.py)


### References


## Problem 8
> Write a program that outputs today’s date and time in the format ”Monday, January
10th 2019 at 1:15pm”.

### Solution
[Problem8.py](Problem8.py)


### References


## Problem 9
> Write a program that reads in a text file and outputs every second line. The program
should take the filename from an argument on the command line.

### Solution
[Problem9.py](Problem9.py)


### References


## Problem 10
> Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

### Solution
[Problem10.py](Problem10.py)


### References


##General References

* [Stack Overflow](https://stackoverflow.com/)
* [W3 Schools](https://www.w3schools.com/python/default.asp)
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)



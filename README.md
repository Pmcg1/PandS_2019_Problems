# Programming and Scripting 2019 Problem Set
## G00190832 Peter McGowan

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
> Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

### Solution
[Problem1.py](Problem1.py)

A user input is read from the command prompt ('Input any positive integer: '), explicitly declared as an integer and stored as the variable 'i'.
Another variable, 'j' is initialised as 0.

An if statement is used to check that the input is positive. If true, then a while loop is initiated. For each loop, 'j' is updated with the current value of 'i' and then 'i' is decremented by 1. The loop ends when 'i' is at 0, printing 'j'.

If the if statement is false, then the user is informed that they have not entered a positive integer.

### References
N/A

## Problem 2
> Write a program that outputs whether or not today is a day that begins with the letter T. An example of running this program on a Thursday is as follows.

### Solution
[Problem2.py](Problem2.py)

Datetime module is imported to allow access to its functions.
The current date and time is assigned to a variable 'now', and the day is extracted from this using strftime.

The check is performed using an if statement. This checks is the first indexed element of the string 'Day' is equivalent to the letter 'T'.
The answer printed is then dependant of whether the if statement evaluates to true or false.

### References
* [W3 Schools](https://www.w3schools.com/python/python_datetime.asp)

## Problem 3
> Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

### Solution
[Problem3.py](Problem3.py)

This problem is solved using a while loop to iterate through the given range.

An initial value of 1000 is assigned to the iterator and the while loop runs until this reached 10000. On each iteration it uses an if statement to check to conditions (with the binary operator 'and'). The remainder of the iterator value divided by 6 is checked to make sure that it is true, and the remainder of the iterator divided by 12 is checked to make sure that it is false.

If this is evaluated as true, then the current value of the iterator is printed. Whether true or false, the iterator is incremented by 1.

### References
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)

## Problem 4
> Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

### Solution
[Problem4.py](Problem4.py)

Similarly to Problem 1, the user is asked to input a positive integer. The same if statement from Problem 1 is used to assess if the integer is positive.

The calculations are implemented as a while loop embedded into the if statement that will iterate until the value being assessed is equal to 1.
The while loop will first print the value, explicitly declaring it as an integer as the later checks can convert it to a float. The print statement includes the following parameter: `end=' '`.This allows all values to be printed on the same line.

An if statement is then implemented inside the while loop. It assesses if the value is positive using `if i % 2 == 0:`. If true, the value is halved, and if false the value is added to itself multiplied by 3. A final print statement is included following completion of the while loop to print the final value.

### References
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)

## Problem 5
> Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.

### Solution
[Problem5.py](Problem5.py)

Similarly to Problem 1, the user is asked to input a positive integer. The same if statement from Problem 1 is used to assess if the integer is positive.

A nested if statement then checks whether the number is equal to 1 or not. Where 1 has been input, the programme ends and returns "That is a prime" to the user.
Where the number is not 1, a for-else loop is used to assess it. This iterates over the range [2, Input Number] as a prime must only have factors of itself and 1. An if statement inside the for loop checks if the input number divided by the current iterator number is an even number. IF this is true, then the number is not a prime and the programme will print this. Additionally it uses 'break' to exit the loop. The else portion of the loop allows the situation where the number is a prime to be printed.

The use of 'else' combined with a 'for' loop is not implemented within many other programming languages. Python implements it (and allows it in 'while' loops also) to provide an event that will occur only if the for loop is executed normally without an interruption i.e. from a 'break' statement or similar.

### References
* [Programiz](https://www.programiz.com/python-programming/examples/prime-number)
* [Medium.com: for-else loops](https://medium.com/@s16h/the-forgotten-optional-else-in-python-loops-90d9c465c830)

## Problem 6
> Write a program that takes a user input string and outputs every second word.

### Solution
[Problem6.py](Problem6.py)

The user is requested to type a sentence, which is stored as a string (inputSentence). It is explicitly declared as a string.

A list of punctuation is included as a list (punctuation). A for loop is run for the number of items in the punctuation list. On each iteration, the input sentence is checked for an element in the punctuation list and if found it is replaced with an empty character using `replace()`.

The input sentence is not split into a list of strings for each word, using spaces as separators.
A new list is created that takes as its elements every second word from the previous list.

A for loop is used to print out the final list to give it the appearance of a single string. It iterates through each word in the list and prints it, using the `end=' '` parameter to prevent newlines from being created.

### References
* [Tutorials Point: replace()](https://www.tutorialspoint.com/python/string_replace.htm)

## Problem 7
> Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

### Solution
[Problem7.py](Problem7.py)

This programme implements Newton's Method to approximate the square root of the input to 3 decimal places.

The user is asked to input a float - this is explicitly declared and stored as 'userInput'.

An if statement is used to split the analysis into three different cases:

1. If the userInput is < 0 then the user is informed that they have not entered a positive number.
2. If the userInput is 1 then the programme returns the value of 1, being its own square.
3. In all other cases, a 'while' loop is used to implement Newton's method. The inital approximation of the root is set to userInput/2. The loop then does the following:
    * Sets the loop conditions such that it will iterate as long as the absolute value of the current approximation squared minus the userInput is greater than 0.001.
    * Assigns the current approximation (currentApprox) to:
        > 0.5 * (currentApprox + (userInput/currentApprox))

Once the while loop is complete, an f-string is used to format the output. As the approximations could contain a substantial number of digits after the decimal place, the output is rounded to three decimal places using round().

### References
* [Interactive Python: Newton's Method](http://interactivepython.org/runestone/static/thinkcspy/MoreAboutIteration/Newton%27sMethod.html)
* [Python Tutorial: F-Strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

## Problem 8
> Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

### Solution
[Problem8.py](Problem8.py)

Much like Problem 2, the datetime module is imported for this programme.

The current date and time is extracted to a variable, 'i' using `dt.now()`.

Several operations are carried out prior to outputting the date and time in the correct format:
1. An if statement checks the date value and assigns a suffix (st, nd, rd, th) depending on its value.
2. The date is extracted from the datetime string and stored as an integer, thereby stripping out any leading zero.
3. The hour is extracted from the datetime string and stored as an integer, thereby stripping out any leading zero.

Finally, an f-string is used to format the output overall, along with the `strftime()` function to extract formatted elements of the date and time.
The date and hour value are included directly as integers (see 2. and 3. above) in order to remove leading zeroes, and the correct suffix is appended to the date.

### References
* [Python Documentation: Datetime](https://docs.python.org/3/library/datetime.html)
* [Python Tutorial: F-Strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

## Problem 9
> Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

### Solution
[Problem9.py](Problem9.py)

This programme imports sys in order to use sys.argv. The input file is read as an argument from the command line (`sys.argv[1]`) and stored as a string 'inputFile'.

The file is opened (read only) as 'f' and a for loop is used to iterate through each line in it. As the iterator is set to 1 initially, an if statement within the loop checks whether the iterator is odd or even on that iteration, and if odd it prints the line. `.rstrip('\n')` is used to remove newline characters and thereby correctly format the output. The iterator is incremented by 1 on each iteration.

The input file is closed again after all lines have been read by the programme.

### References
* [Python for Beginners: sys.argv](https://www.pythonforbeginners.com/system/python-sys-argv)
* [Stackabuse: Reading a file line by line](https://stackabuse.com/read-a-file-line-by-line-in-python/)

## Problem 10
> Write a program that displays a plot of the functions x, x<sup>2</sup> and 2<sup>x</sup> in the range [0, 4].

### Solution
[Problem10.py](Problem10.py)

This programme imports two libraries:
1. matplotlib: to use pyplot for plotting graphs
2. numpy: to simplify mathematical operations

Three plots are created, one for each function:
1. y = x
    * This is coloured red and given the marker style 4 (CARETLEFT)
2. y = x<sup>2</sup>
    * This is coloured green and given the marker style 6 (CARETUP)
    * numpy `np.square()` is used to generate the squares of the input range
3. y = 2<sup>x</sup>
    * This is coloured blue and given the marker style 7 (CARETDOWN)
    * numpy `np.power()` is used to generate 2 to the power of the input range

Rather than list out the range of values given, `range(0,3)` is simply passed as a parameter for each plot as required.

Each plot is given a distinct marker style in order to provide clarity where they overlap. They are also goven a label for inclusion in the legend.

The x and y axes are labelled and a grid is displayed on the plot. The plot size is not explicitly declared to allow for dynamic sizing.

A legend is displayed using the labels declared for each plot, and the graph is given a title.

The final line of code generates the overall plot, which includes the three plots created above on one graph.

### References
* [Matplotlib pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)
* [Matplotlib marker styles](https://matplotlib.org/api/markers_api.html)
* [Numpy Square](https://docs.scipy.org/doc/numpy/reference/generated/numpy.square.html)
* [Numpy Power](https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html)

## General References
* [Stack Overflow](https://stackoverflow.com/)
* [W3 Schools](https://www.w3schools.com/python/default.asp)
* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)

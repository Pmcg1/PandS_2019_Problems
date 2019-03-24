# Problem Set 2019 - Problem 10
# Peter McGowan
# Started 2019-03-24

# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import matplotlib.pyplot as plt # Import pyplot for plotting graphs
import numpy as np # Import numpy for convenient manipulation of lists

plt.plot(range(0,4), range(0,4), label='y = x', color='red', marker = 4) # plot y = x for the given range and colour it red
plt.plot(range(0,4), np.square(range(0,4)), label='y = $x^2$', color='green', marker = 6) # plot y = x^2 for the given range (using numpy) and colour it green
plt.plot(range(0,4), np.power(2,range(0,4)), label='y = $2^x$', color='blue', marker = 7) # plot y = 2^x for the given range (using numpy) and colour it blue
plt.xlabel('x') # Label x-axis
plt.ylabel('y') # Label x-axis
plt.grid(True) # Display grid
plt.legend() # Display legend
plt.suptitle('Plot of the functions x, $x^2$ and $2^x$ in the range [0, 4]') # Plot title
plt.show() # Generate the plot
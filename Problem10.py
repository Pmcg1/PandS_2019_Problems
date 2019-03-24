# Problem Set 2019 - Problem 10
# Peter McGowan
# Started 2019-03-24

# Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

import matplotlib.pyplot as plt
import numpy as np

valueRange = list(range(0,4))
print(valueRange)
'''
plt.figure(1, figsize=(18, 5))

plt.subplot(131)
plt.plot(valueRange, valueRange, color='red')
plt.xlabel('x')
plt.ylabel('x')
plt.title("x vs x")
plt.grid(True)

plt.subplot(132)
plt.plot(valueRange, np.square(valueRange), color='green')
plt.xlabel('x')
plt.ylabel('$x^2$')
plt.title("x vs $x^2$")
plt.grid(True)

plt.subplot(133)
plt.plot(valueRange, np.power(2,valueRange), color='blue')
plt.xlabel('x')
plt.ylabel('$2^x$')
plt.title("x vs $2^x$")
plt.grid(True)

plt.suptitle('Problem 10')
plt.show()
'''


fig, ax = plt.subplots()
plt.plot(valueRange, valueRange, label='y = x', color='red')
plt.plot(valueRange, np.square(valueRange), label='y = $x^2$', color='green')
plt.plot(valueRange, np.power(2,valueRange), label='y = $2^x$', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

ax.legend()
plt.suptitle('Problem 10')
plt.show()
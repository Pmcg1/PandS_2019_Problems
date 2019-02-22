# Problem Set 2019 - Problem 6
# Peter McGowan
# Started 2019-02-20

# Write a program that takes a user input string and outputs every second word.

inputSentence = str(input('Please enter a sentence: ')) # Ask user to type a sentence. Explicitly expect a string.

punctuation = [".", ",", "?", "!", ";", ":"] # List of punctuation to strip from input string.

i=0 # Initialise iterator for loop.

for i in range(len(punctuation)): # Run loop for the numebr of items in the punctuation list.
   inputSentence = inputSentence.replace(punctuation[i],"") # On each iteration strip an item from the punctuation list out of the input string.

# print(inputSentence) # Error check, print input sentence - disabled.

allWords = inputSentence.split( ) # Split input sentence into a list of strings for each word - SPACE as separator.

secondWords = allWords[1::2] # Extract every second word into a new list, starting with the second word.

# print(allWords) # Error check, list of all words - disabled.
# print(secondWords) # Error check, print list of second words - disabled.

for x in secondWords: # Iterate through the list of second words
    print (x, end=' ') # Print each word on the same line with a space between each.







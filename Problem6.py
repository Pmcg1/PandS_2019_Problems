# Problem Set 2019 - Problem 6
# Peter McGowan
# Started 2019-02-20

# Write a program that takes a user input string and outputs every second word.



#need to iterate through words in list and delete punctuation

inputSentence = str(input('Please enter a sentence: '))


#for x in (".", ",", "?", "!", ";"), ("","","","",""):
 #   inputSentence = inputSentence.replace(*x) ### broken - too many variables

print(inputSentence)

allWords = inputSentence.split( )

#s = "The quick brown fox jumps over the lazy dog"
#for r in (("brown", "red"), ("lazy", "quick")):
#    s = s.replace(*r)

secondWords = allWords[1::2]

print(secondWords)
print(allWords)

for x in secondWords:
    print (x)

#outputSentence
#for x in allWords


#print(inputSentence.split( ))






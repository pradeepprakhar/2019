#!/usr/bin/python


filename = "pradeep.txt"
numLines = 0
numWords = 0
numChars = 0

with open(filename, 'r') as file:
	for line in file:
		wordsList = line.split()
		numLines += 1
		numWords += len(wordsList)
		numChars += len(line)


print(numLines,numWords,numChars)


import re
import sys

#Takes arguments from command line and set input and output files
inputTextfile = sys.argv[1]
outputFile = sys.argv[2]

#opens file to read
inputFile = open(inputTextfile, "r")

#Dictionary created to store words
wordDict = dict()

#Goes through file line by line
for line in inputFile:
    #gets rid of any characters for new line
    line = line.strip()
    #this splits at any punctuation or whitespace
    wordsInLine = re.split('[ \t]',line)

    #This iterates through each word in every line read
    for word in wordsInLine:
        if word in wordDict:
           # word = word.strip(".,!?:;'\")
            #increments the word count if word is already in the dictionary
            wordDict[word] = wordDict[word]+1
        else:
            #adds the new  word to the  dictionary
            wordDict[word] = 1

wordList = list(wordDict.keys())
wordList.sort()

#Tests out that some list prints out
for key in wordList:
    print(key, ":", wordDict[key])

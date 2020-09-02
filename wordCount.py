import re
import sys

#Takes arguments from command line and set input and output files
inputTextfile = sys.argv[1]
outputTextfile = sys.argv[2]

#opens file to read
inputFile = open(inputTextfile, "r")

#Dictionary created to store words and word  count
wordDict = dict()

#Goes through file line by line
for line in inputFile:
    #removes any whitespace and makes all words lowercase
    line = line.strip()
    line = line.lower()
    
    #this splits at any punctuation
    wordsInLine = line.split()
    
    #This iterates through each word in every line read
    for word in wordsInLine:
        #Removes any white space or punctuation
        word = re.sub('[^A-Za-z0-9]+','',word)

        if word in wordDict:
            #increments the word count if word is already in the dictionary
            wordDict[word] = wordDict[word]+1

        else:
            #adds the new  word to the  dictionary
            wordDict[word] = 1

wordList = list(wordDict.keys())
wordList.sort()


outputFile = open(outputTextfile, 'w')

#Writes sorted words and counter to file
for key in sorted(wordDict):
    #converts line with word and counter to string so it becomes writable
    wordDictString = str(key)+ " " + str(wordDict[key])
    outputFile.write(wordDictString)
    outputFile.write("\n")
   # outputFile.write(key)
   # outputFile.write(wordDict[key])

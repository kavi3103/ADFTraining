from collections import Counter
import re
import logging
import configparser

'''
    Configuring logging set to level info and save log info in file "Info.log"
'''
logging.basicConfig(filename='Info.log', level=logging.INFO)


class FileHandle:

    def __init__(self, inputFile, outputFile):
        self.readObj = open(inputFile, "r")  # open file in read mode
        self.writeObj = open(outputFile, "a")  # open file in write mode
        self.listWords = []

        logging.info(f"Created file object for reading {inputFile} and writing {outputFile}")

    def splitUsingSpace(self):
        # splits words by space
        for row in self.readObj:
            for word in row.split():
                self.listWords.append(word)

        logging.info("Split words using space")

    def splitUsingVowel(self):
        # splits words by vowels
        for row in self.readObj:
            for word in re.split("a|e|i|o|u|A|E|I|O|U", row):
                if word != '' and word != ' ':
                    self.listWords.append(word)

        logging.info("Split words using vowels")

    def writeData(self, string):
        self.writeObj.write(string)


class StringManipulation(FileHandle):
    def __init__(self, inputFile, outputFile):
        super().__init__(inputFile, outputFile)  # call super class constructor
        # initialise some instance variables
        self.startWith = 0
        self.endWith = 0
        self.maxRepWords = []
        self.palindromeWords = []
        self.dictWords = {}
        self.uniqueWords = []

    def checkStartswithTo(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingSpace()
        for word in self.listWords:
            # words starting with "To"
            if word.startswith("To"):
                self.startWith += 1

        self.writeData("The number of words having prefix with “To” in the input file: "+str(self.startWith))

        logging.info(f"Found The number of words having prefix with To {self.startWith}")

    def checkEndWithIng(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingSpace()
        for word in self.listWords:
            # words ending with "ing"
            if word.endswith("ing"):
                self.endWith += 1

        self.writeData("\n\nThe number of words ending with “ing” in the input file: "+str(self.endWith))

        logging.info(f"Found The number of words ending with ing {self.endWith}")

    def createWordDict(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingSpace()
        # store as a Word dict with counter as key
        for counter in range(len(self.listWords)):
            self.dictWords[counter] = self.listWords[counter]

        self.writeData("\n\nWord dict with Key as counter index and value as the words present in file: ")
        for (key, value) in self.dictWords.items():
            self.writeData("\n" + str(key) + " - " + str(value))

        logging.info("Created Word Dictionary")

    def getUniqueWords(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingSpace()
        self.uniqueWords = list(set(self.listWords))  # stores unique words

        self.writeData("\n\n Unique Words: ")
        for word in self.uniqueWords:
            self.writeData("\n"+word)

        logging.info("Created Unique words list")

    @staticmethod
    def checkPalindrome(string):
        """
            input: string
            output: boolean whether it is palindrome or not
        """
        word = string.lower()  # converts to lower case
        reverse = word[::-1]  # reverse the word
        if word == reverse:
            return True
        return False

    def findPalindromeWords(self):
        if len(self.uniqueWords) == 0:
            self.getUniqueWords()
        for i in self.uniqueWords:
            # check palindrome for the words
            if self.checkPalindrome(i):
                self.palindromeWords.append(i)

        self.writeData("\n\nThe palindrome present in the file: ")
        for i in self.palindromeWords:
            self.writeData("\n"+i)

        logging.info("Found palindrome words")

    def findMaximumRepWord(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingSpace()
        frequency = Counter(self.listWords)  # find frequency of words
        max_freq = max(frequency.values())  # frequency with largest value
        for (key, value) in frequency.items():
            if value == max_freq:
                # append words that has frequency with largest value
                self.maxRepWords.append(key)
        self.writeData("\n\nThe word that was repeated maximum number of times: ")
        for i in self.maxRepWords:
            self.writeData("\n"+i)

        logging.info("Found maximum Repeated words")

    def capitaliseNthLetter(self, n):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingVowel()
        for i in range(len(self.listWords)):
            word = self.listWords[i]
            # capitalise n-th Letter of every word
            if len(word) >= n:
                self.listWords[i] = word.replace(word[n-1], word[n-1].upper())

        logging.info(f"capitalise {n}-th Letter of every word")

    def replaceBlankToDash(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingVowel()
        for i in range(len(self.listWords)):
            word = self.listWords[i]
            # Replace blank spaces with "-"
            self.listWords[i] = word.replace(' ', '-')

        logging.info("Replace blank spaces with '-'")

    def capitaliseNthWord(self, n):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingVowel()
        for i in range(len(self.listWords)):
            word = self.listWords[i]
            # capitalise every nth word
            if (i+1)%n == 0:
                self.listWords[i] = word.upper()

        logging.info(f"capitalise every {n}th word")

    def replaceNewlineWithSemiColon(self):
        if len(self.listWords) == 0:  # if words are not split
            self.splitUsingVowel()
        for i in range(len(self.listWords)):
            word = self.listWords[i]
            # replace new line character with ;
            self.listWords[i] = word.replace("\n", ";")

        logging.info("replace new line character with ;")

    def performVariousWriteFile(self, letter, word):
        self.capitaliseNthLetter(letter)
        self.replaceBlankToDash()
        self.capitaliseNthWord(word)
        self.replaceNewlineWithSemiColon()
        for i in self.listWords:
            self.writeData(i+" ")
            

try:
    configParser = configparser.RawConfigParser()
    configFilePath = "config.txt"
    configParser.read(configFilePath)

    input1 = configParser.get('for-Obj-1', 'input')
    output1 = configParser.get('for-Obj-1', 'output')
    #print(input1, output1)
    f1 = StringManipulation(input1, output1)
    f1.checkStartswithTo()
    f1.checkEndWithIng()
    f1.getUniqueWords()
    f1.findPalindromeWords()
    f1.findMaximumRepWord()
    f1.createWordDict()
    input2 = configParser.get('for-Obj-2', 'input')
    output2 = configParser.get('for-Obj-2', 'output')
    f2 = StringManipulation(input2, output2)
    f2.performVariousWriteFile(3, 5)


except (FileNotFoundError, IOError):
    print("Wrong file or file path")





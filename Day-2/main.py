import sys
from collections import Counter
import re

def checkPalingdrome(string):
    '''
        input: string
        output: boolean whether it is palingdrome or not
    '''
    word = string.lower() #converts to lower case
    reverse = word[::-1] #reverse the word
    if(word == reverse):
        return True
    return False


def cap3rdRepBlank(word):
    '''
        Capitalise every 3rd letter
        Replace white spaces with "-"
    '''
    if (len(word) >= 3):
        modifiedword = word.replace(word[2], word[2].upper())
    else:
        modifiedword = word
    return modifiedword.replace(' ','-')

#main

#initialisation
startwith = 0
endwith = 0
listWords = []
maxRepWords = []
palindromeWords = []
dictWords = {}
counter = 0
try:
    fileName = sys.argv[1]

    with open(fileName,"r") as file:
        for row in file:
            for word in row.split():

                listWords.append(word)

                # words starting with "To"
                if(word.startswith("To")):
                    startwith += 1

                #words ending with "ing"
                if(word.endswith("ing")):
                    endwith += 1

                #store as a Word dict with counter as key
                dictWords[counter] = word
                counter += 1


    #to find the word that was repeated maximum number of times.
    frequency = Counter(listWords) # find frequency of words
    maxFreq = max(frequency.values()) # frequency with largest value
    for (key,value) in frequency.items():
        if(value == maxFreq):
            #append words that has frequency with largest value
            maxRepWords.append(key)

    # stores unique words
    uniqueWords = list(set(listWords))

    for i in uniqueWords:
        # check palingdrome for the words
        if (checkPalingdrome(i)):
            palindromeWords.append(i)

    #output
    print("The number of words having prefix with “To” in the input file: ",startwith)
    print("The number of words ending with “ing” in the input file: ",endwith)
    print("The word that was repeated maximum number of times: ")
    for i in maxRepWords:
        print(i)
    print("The palindrome present in the file: ")
    for i in palindromeWords:
        print(i)
    print("Unique Words: ")
    for i in uniqueWords:
        print(i)
    print("Word dict with Key as counter index and value as the words present in file: ",dictWords)

    count = 0
    write = open("output.txt","a")
    with open(fileName, "r") as file:
        for row in file:
            for word in re.split("a|e|i|o|u|A|E|I|O|U",row): #split using vowels
                if(word != '' and word != ' '):
                    count += 1
                    modifiedword = cap3rdRepBlank(word) #Capitalise every 3rd letter and Replace white spaces with "-"
                    #capitalise every 5th word
                    if(count%5 == 0):
                        modifiedword = modifiedword.upper()
                    #add semicolon for every new line
                    modifiedword = modifiedword.replace("\n",";")
                    write.write(modifiedword+" ")

    #write.write(";\n")


except (FileNotFoundError, IOError):
    print("Wrong file or file path")
except IndexError:
    print("Give File Name")


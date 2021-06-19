'''
    1.	Program to read a file and store the unique words in a list sorted based on the length of word in a new file
    along with each word length appended to it.
'''
list = []
# read a file and store the unique words in a list
with open("input.txt","r") as file:
    for row in file:
        for word in row.split():
            # stores unique words
            if(word not in list):
                list.append(word)

#sort based on length
length = len(list)
for i in range(length - 1):
    for j in range(0, length - i - 1):
        if len(list[j]) > len(list[j + 1]):
            list[j], list[j + 1] = list[j + 1], list[j]

# write the unique words in list along with length
with open("output.txt","a") as write:
    for word in list:
        write.write(word + " " + str(len(word)) + "\n")
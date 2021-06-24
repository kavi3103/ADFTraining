"""
 using pytest, pylint, pycoverage
"""
from collections import Counter
import re
import logging
import configparser

logging.basicConfig(filename='Info.log', level=logging.INFO)


class FileHandle:
    """
        handles file
    """
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.list_words = []
        logging.info("Created file object for reading %s and writing %s", input_file, output_file)

    def split_using_space(self):
        """
        splits words by space
        """
        with open(self.input_file, "r") as read_obj:
            for row in read_obj:
                for word in row.split():
                    self.list_words.append(word)
        logging.info("Split words using space")

    def split_using_vowel(self):
        """
        splits words by vowels
        """
        with open(self.input_file, "r") as read_obj:
            for row in read_obj:
                for word in re.split("[aeiouAEIOU]", row):
                    if word not in ('', ' '):
                        self.list_words.append(word)
        logging.info("Split words using vowels")

    def write_data(self, string):
        """
        writes data
        """
        with open(self.output_file, "a") as write_obj:
            write_obj.write(string)


class StringManipulation(FileHandle):
    """
    operations to be done on input file and write into output file
    """
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)  # call super class constructor
        # initialise some instance variables
        self.start_with = 0
        self.end_with = 0
        self.max_rep_words = []
        self.palindrome_words = []
        self.dict_words = {}
        self.unique_words = []

    def check_starts_with_to(self):
        """
         checks number of words starting with "To"
        """
        if len(self.list_words) == 0:
            self.split_using_space()
        for word in self.list_words:
            # words starting with "To"
            if word.startswith("To"):
                self.start_with += 1
        self.write_data("The number of words having prefix with To:{}".format(str(self.start_with)))
        logging.info("Found The number of words having prefix with To %s", str(self.start_with))

    def check_end_with_ing(self):
        """
        checks number of words ending with "ing"
        """
        for word in self.list_words:
            # words ending with "ing"
            if word.endswith("ing"):
                self.end_with += 1
        self.write_data("\n\nThe number of words ending with ing:{}".format(str(self.end_with)))
        logging.info("Found The number of words ending with ing %s", str(self.end_with))

    def create_word_dict(self):
        """
        create word dict
        """
        # store as a Word dict with counter as key
        for counter in range(len(self.list_words)):
            self.dict_words[counter] = self.list_words[counter]
        self.write_data("\n\nWord dict : ")
        for (key, value) in self.dict_words.items():
            self.write_data("\n {} - {}".format(str(key), str(value)))
        logging.info("Created Word Dictionary")

    def get_unique_words(self):
        """
           find unique words list
        """
        self.unique_words = list(set(self.list_words))  # stores unique words
        self.write_data("\n\nUnique Words: ")
        for word in self.unique_words:
            self.write_data("\n{}".format(word))
        logging.info("Created Unique words list")

    @staticmethod
    def check_palindrome(string):
        """
            input: string
            output: boolean whether it is palindrome or not
        """
        word = string.lower()  # converts to lower case
        reverse = word[::-1]  # reverse the word
        if word == reverse:
            return True
        return False

    def find_palindrome_words(self):
        """
         find palindrome words
        """
        for i in self.unique_words:
            # check palindrome for the words
            if self.check_palindrome(i):
                self.palindrome_words.append(i)
        self.write_data("\n\nThe palindrome present in the file: ")
        for i in self.palindrome_words:
            self.write_data("\n{}".format(i))
        logging.info("Found palindrome words")

    def find_maximum_rep_word(self):
        """
            find maximum repeated word
        """
        frequency = Counter(self.list_words) # find frequency of words
        if frequency.values():
            max_freq = max(frequency.values())  # frequency with largest value
            for (key, value) in frequency.items():
                if value == max_freq:
                    # append words that has frequency with largest value
                    self.max_rep_words.append(key)
            self.write_data("\n\nThe word that was repeated maximum number of times: ")
            for i in self.max_rep_words:
                self.write_data("\n{}".format(i))
        logging.info("Found maximum Repeated words")

    def capitalise_nth_letter(self, num):
        """
        capitalise every nth letter of the word
        """
        if len(self.list_words) == 0:
            self.split_using_vowel()
        for i in range(len(self.list_words)):
            word = self.list_words[i]
            # capitalise n-th Letter of every word
            if len(word) >= num:
                self.list_words[i] = word.replace(word[num-1], word[num-1].upper())
        logging.info("capitalise %s-th Letter of every word", str(num))

    def replace_blank_to_dash(self):
        """
        replace blank spaces with -
        """
        for i in range(len(self.list_words)):
            word = self.list_words[i]
            # Replace blank spaces with "-"
            self.list_words[i] = word.replace(' ', '-')
        logging.info("Replace blank spaces with '-'")

    def capitalise_nth_word(self, num):
        """
            capitalise every nth word in th file
        """
        for i in range(len(self.list_words)):
            word = self.list_words[i]
            # capitalise every nth word
            if (i+1) % num == 0:
                self.list_words[i] = word.upper()
        logging.info("capitalise every %s th word", str(num))

    def replace_newline_with_semicolon(self):
        """
        add semicolon to end of line
        """
        for i in range(len(self.list_words)):
            word = self.list_words[i]
            # replace new line character with ;
            self.list_words[i] = word.replace("\n", ";")
        logging.info("replace new line character with ;")

    def perform_various_write_file(self, letter, word):
        """
        perform all operations
        """
        self.capitalise_nth_letter(letter)
        self.replace_blank_to_dash()
        self.capitalise_nth_word(word)
        self.replace_newline_with_semicolon()
        for i in self.list_words:
            self.write_data("{} ".format(i))

    def perform_other_operations(self):
        """
         call all methods
        """
        self.check_starts_with_to()
        self.check_end_with_ing()
        self.get_unique_words()
        self.find_palindrome_words()
        self.find_maximum_rep_word()
        self.create_word_dict()


config_parser = configparser.RawConfigParser()
CONFIG_FILE_PATH = "config.txt"
config_parser.read(CONFIG_FILE_PATH)
input1 = config_parser.get('for-Obj-1', 'input')
output1 = config_parser.get('for-Obj-1', 'output')
f1 = StringManipulation(input1, output1)
f1.perform_other_operations()
input2 = config_parser.get('for-Obj-2', 'input')
output2 = config_parser.get('for-Obj-2', 'output')
f2 = StringManipulation(input2, output2)
f2.perform_various_write_file(3, 5)

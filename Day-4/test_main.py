import pytest
from main import StringManipulation


class TestStringManipulation:

    def test_write_data(self):
        s = StringManipulation("input1.txt", "output1.txt")
        s.write_data("Hi Hello")
        s.write_data(" good")
        with open("output1.txt", "r") as file:
            read = file.read()
        assert "Hi Hello good" in read

    @pytest.mark.parametrize("string, expected",
                             [("", []), ("To all morning goog ing mum To",
                                         ['To', 'all', 'morning', 'goog', 'ing', 'mum', 'To'])])
    def test_split_using_space(self, string, expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        s = StringManipulation("input1.txt", "output1.txt")
        assert s.list_words == []
        s.split_using_space()
        assert s.list_words == expected

    @pytest.mark.parametrize("string, expected", [("", []),
                                                  ("Tollgoodmorning how are you",
                                                   ['T', 'llg', 'dm', 'rn', 'ng h', 'w ', 'r', ' y'])])
    def test_split_using_vowel(self, string, expected):
        with open("input2.txt", "w") as file:
            file.write(string)
        s = StringManipulation("input2.txt", "output2.txt")
        s.split_using_vowel()
        assert s.list_words == expected

    def test_initial(self):
        s = StringManipulation("input1.txt", "output1.txt")
        assert s.list_words == []
        assert s.start_with == 0
        assert s.end_with == 0
        assert s.max_rep_words == []
        assert s.palindrome_words == []
        assert s.dict_words == {}
        assert s.unique_words == []

    @pytest.mark.parametrize("string, expected",
                             [("", 0), ("To all morning goog ing mum Tomorrow", 2)])
    def test_check_starts_with_to(self,string,expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        s = StringManipulation("input1.txt", "output1.txt")
        s.check_starts_with_to()
        assert s.start_with == expected

    @pytest.mark.parametrize("string, expected",
                             [("", 0), ("To all morning goog ing mum Tomorrow", 2)])
    def test_check_end_with_ing1(self,string,expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        s = StringManipulation("input1.txt", "output1.txt")
        s.split_using_space()
        s.check_end_with_ing()
        assert s.end_with == expected

    @pytest.mark.parametrize("string, expected",
                             [("", {}), ("To all morning goog ing mum Tomorrow",
                                         {0:'To', 1:'all', 2:'morning', 3:'goog', 4:'ing', 5:'mum', 6:'Tomorrow'})])
    def test_create_word_dict(self,string,expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        f = StringManipulation("input1.txt", "output1.txt")
        f.split_using_space()
        f.create_word_dict()
        assert f.dict_words == expected

    @pytest.mark.parametrize("string, expected",
                             [("", []), ("To all morning goog ing mum Tomorrow To",
                                         ['To', 'all', 'morning', 'goog', 'ing', 'mum', 'Tomorrow'])])
    def test_get_unique_words(self, string, expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        f = StringManipulation("input1.txt", "output1.txt")
        f.split_using_space()
        f.get_unique_words()
        assert len(f.unique_words) == len(expected) and f.unique_words.sort() == expected.sort()

    @pytest.mark.parametrize("string, expected", [("mum", True), ("kavitha", False), ("", True)])
    def test_check_palindrome(self, string, expected):
        assert StringManipulation.check_palindrome(string) == expected

    @pytest.mark.parametrize("string, expected",
                             [("", []), ("To all morning goog ing mum Tomorrow To",
                                         ['goog', 'mum'])])
    def test_find_palindrome_words(self, string, expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        f = StringManipulation("input1.txt", "output1.txt")
        f.split_using_space()
        f.get_unique_words()
        f.find_palindrome_words()
        assert len(f.palindrome_words) == len(expected) and f.palindrome_words.sort() == expected.sort()

    @pytest.mark.parametrize("string, expected",
                             [("", []), ("To all morning goog ing mum Tomorrow To",
                                         ['To'])])
    def test_find_maximum_rep_word(self, string, expected):
        with open("input1.txt", "w") as file:
            file.write(string)
        f = StringManipulation("input1.txt", "output1.txt")
        f.split_using_space()
        f.find_palindrome_words()
        assert f.max_rep_words.sort() == expected.sort()

    @pytest.mark.parametrize("string, expected", [("", ""),
                                                  ("Tollgoodmorning how are you",
                                                   "T llG dm rn NG-H w- r -y")])
    def test_perform_various_write_file(self,string,expected):
        with open("input2.txt", "w") as file:
            file.write(string)
        s = StringManipulation("input2.txt", "output2.txt")
        s.perform_various_write_file(3,5)
        with open("output2.txt","r") as f:
            read = f.read()
        assert expected in read

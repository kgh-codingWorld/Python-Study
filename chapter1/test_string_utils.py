# test_string_utils
from string_utils import reverse_string,count_vowels,is_palindrome

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    
def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("python") == 1
    assert count_vowels("aeiou") == 5

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("hello") == False
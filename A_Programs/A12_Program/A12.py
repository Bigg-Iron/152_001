# Is some text a palindrome?
import re

def palindrome(s):
    """Returns True if the string parameter contains a palindrome, False otherwise."""
    s = re.sub('[\W_]+', '', s) 
    if len(s) <= 1: 
        return True
    else:
        if s[0] == s[-1]: 
            return palindrome(s[1:-1])
        else: 
            return False
    


def main():
    """DO NOT CHANGE THIS CODE"""
    text = input('text?\n')
    if palindrome(text):
        print("Palindrome")
    else:
        print("Emordnilap") # not a palindrome

if __name__ == '__main__':
	main()

# A12 Program

## Background

A palindrome is a string of text (number, word, phrase, or sentence) that reads the same backward as forwards. Punctuation and spaces are allowed but ignored. Some examples of palindromes include:

12345654321
12,344,321
rotator
never odd or even
Able was I, ere I saw Elba.

## Assignment

This program should determine if any given string is a palindrome or not. This will be done with just one function:

palindrome(s)

Takes a string, and returns True or False. This function must be implemented recursively. You may not use while loops, for loops, or built-in list functions.

You should use multiple base cases and multiple recursive cases to determine if the text is a palindrome.

Recursive cases should skip spaces and punctuation, or compare the remaining string when the end characters match. All comparisons in the function should be case sensitive; "Anna" is not a palindrome, but "anna" is a palindrome.

> [!TIP]
> Helpful Hints:

You can check if a character is alphanumeric with "char".isalnum()

If you want to check a character in a string "s" at position i is alphanumeric, you can use s[i].isalnum().

isalnum() returns a Boolean True of character is alphanumeric, else False

Samples:
Input:

text?
Able was I, ere I saw Elba.
Output:

Emordnilap
Input:

text?
able was I, ere I saw elba.
Output:

Palindrome
Input:

text?
Able was I
Output:

Emordnilap

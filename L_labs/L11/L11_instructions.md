# L11 - Lab

Plan
This lab covers dictionaries more in-depth. (Modifying, Getting Elements, Looping, and Nesting)
This program should:

Count the number of occurrences of each alphabet letter in any given text file.
write readLettersFromFile() to read the file
write countLetters() to count the occurrences and place them in a dictionary
write sortByCount() to sort the final dictionary

The files you read will all contain only uppercase letters A-Z. Each letter is separated by a single white-space (do not count the whitespaces). The file may or may not contain newlines (do not count the newlines).
Here are the specifications for the three functions:

readLettersFromFile(filename)

Takes a string of a filename, and returns a list containing every character in the file.
For example, a file with the contents "A B R A K A D A B R A" will return ['A', 'B', 'R', 'A', 'K', 'A', 'D', 'A', 'B', 'R', 'A']
Hint: what is the difference between string.split() and string.split(" ")
Hint: what is the difference between file.read() and file.readlines() and file.readline()

countLetters(lettersFromFile)

Takes a list of characters, and returns a dictionary, where the keys are the letters and the value is the number of times that character appeared in the list
For example, given ['A', 'B', 'R', 'A', 'K', 'A', 'D', 'A', 'B', 'R', 'A'], it will return {'A': 5, 'B': 2, 'R': 2, 'K': 1, 'D': 1}

sortByCount(count)

Takes a dictionary and returns a list of tuples in ascending sorted order. This function should sort by the count of each letter, then (if the counts are the same) by the letter alphabetically.
For example, given {'A': 5, 'B': 2, 'R': 2, 'K': 1, 'D': 1}, it will return [(1, 'D'), (1, 'K'), (2, 'B'), (2, 'R'), (5, 'A')]
Hint:
Loop over the key-value pairs of the dictionary.
Create a new list that holds a tuple of the value and the key: (value, key)
Then sort and return the new list.
Example Input
Note: Don't forget to provide a filename in the smaller input box below.
sample.txt contains:

A P P L E

Example Output:

```python
Letters: ['A', 'P', 'P', 'L', 'E']
Counted Letters: {'A': 1, 'P':2, 'L':1, 'E':1}
Sorted: [(1,'A'), (1, 'E'), (1, 'L'), (2, 'P')]
```

Provided Files
sample.txt
letters1
letters2
letters3

```python

EXPECTED OUTPUT for letters1:
Sorted: [(1, 'D'), (1, 'H'), (1, 'I'), (1, 'K'), (1, 'L'), (1, 'O'), (3, 'B'), (3, 'E'), (3, 'F'), (4, 'G'), (5, 'A'), (5, 'C')]```

```

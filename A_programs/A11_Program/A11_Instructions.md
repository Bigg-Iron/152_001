# A11 Program

Assignment
This program should:

Count the number of word occurrences contained in a file.
Output a table showing the top 20 frequently used words in decreasing order of use (i.e. the most used word is printed first). Words with the same number of occurrences should be sorted in reverse alphabetic order.
Here are the specifications for the functions:

count_words(filename)
Takes the string of a filename and returns a dictionary containing the number of occurrences of each word in the file.
This function reads the contents of the file, as well as counts the words.
Hint: use extract_words()

report_distribution(count)
Takes a dictionary containing the occurrences of every word and returns a properly formatted string containing a header, the total number of words, and only the top 20 words, sorted by greatest frequency. See below for an example of the formatting.

Example Input:
Note: Don't forget to provide your program with a filename in the smaller input box below. It is strongly recommended that you test your code with multiple files.

Given a file containing:

How much wood would a woodchuck chuck if a woodchuck could chuck wood
Example Output:
The first line is a header. The second line is the count of the total number of words (5 digits right-aligned). Each line after contains two columns separated by a space:

the number of the occurrences (5 digits right-aligned)
the word (left-aligned)
count word
   13
    2 woodchuck
    2 wood
    2 chuck
    2 a
    1 would
    1 much
    1 if
    1 how
    1 could
Test Data
The following test files are available for your use during development:

woodchuck (This is the full woodchuck tongue twister. It's a bit longer than the sample above)
mlkdream ("I Have a Dream . . ." speech by Martin Luther King, Jr., 1963)
susanbanthony ("Woman's Rights to the Suffrage" by Susan B. Anthony, 1873)
hamlet (Hamlet by William Shakespeare, written between 1599 and 1602)

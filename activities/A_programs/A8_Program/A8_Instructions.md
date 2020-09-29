# 8.10 A8 Program

Let's write a program that can handle any Madlib. To do that we will read the Madlib from a file. The MadLib will contain words like _name_ or _a_place_ which identify the blanks that must be filled in. Your program should prompt the user for a substitution for each blank in the file before printing the resulting Madlib.

Some code is provided to get you started. There are also comments to guide you.

Sample Input
There are four sample files for you to test your program. You can download these files below.

madlib1
madlib2
madlib3
madlib4
The contents of the madlib4 file are

```txt
_name_ is too cool for _noun_ class.
Instead, they will be attending _an_event_ .
```

Note that there are spaces surrounding each _blank_ in the input file to simplify parsing them.

The same input for the program includes the filename, followed by the values for the _blanks_. Here is some sample input for madlib4.

```txt
madlib4
Jessie
Python
concert
```

Sample Output
The output for the madlib4 file should look like this when given the sample input above.

```txt
MadLib filename?
name?
noun?
an event?
Jessie is too cool for Python class.
Instead, they will be attending concert .
```

Your solution should contain the following functions:

```txt
1. madlib_word(word) - An implementation of this function is already given. This function replaces the blanks in madlib with given word.

2. madlib_line(text) - This function should make a call to madlib_word function for building a sentence/line constituting the words.

3. madlib_file(filename) - This function should make a call to madlib_line to build each sentence of the given madlib and should write each line built in above step to the given madlib filename

4. madlib_print(madlib) - Should print a completed madlib from the given madlib file.
```

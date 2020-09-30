# Lab Assignment

This lab consists of 6 functions that do different things. Each function will perform reading and/or writing to a file.

Note: In zyBooks, much like on your computers, you can read and write files. Think of zyBooks like a computer without any files in it. If you want to test your code that reads a file, you first have to write a file to test.

Here are the specifications for the functions you will be writing:

writeToFile(string, filename)

Takes a string to be written (string), and the name of the file it will be written in (filename)
This function does not need a loop. This function will help you see if your other functions are working correctly. This functino does not return anything.
Example:

writeToFile("Hello, World\nThe world says hello back!", "hello.txt")

hello.txt now contains:

Hello, World
The world says hello back!

printFile(filename)

Takes the name of a file (filename)
Opens the specified file, then prints the text of that file. This function does not need a loop. This function should not return anything. This function will help you see if your other functions are working correctly.
Example:

printFile("numbers.txt")

If numbers.txt contains:

1
2
3
4
The output will be:

1
2
3
4

writeListToFile(a_list, filename)

Takes a list of numbers (a_list), and the name of a file (filename)
Writes each of the numbers in the list to the file. Each number is followed by a newline (\n)
Example:

writeListToFile([1,2,3,4], "myfile.txt")

myfile.txt now contains:

1
2
3
4
writeUserInfo(name, password, filename)

Takes a 3 strings, name, password, and filename
This function will append 2 lines to the file:
The text name= followed by the name parameter
The text password= followed by the password parameter
Example:

writeUserInfo("casey","walrus7","secret_file.txt")

writeUserInfo("riley","python_is_fun","secret_file.txt")

secret_file.txt now contains:

name=casey
password=walrus7
name=riley
password=python_is_fun
sumFile(filename)

Takes the name of a file (filename)
Loop through every line in the file, and cast each line to a float and add it to the total sum of each number
Return the sum
Example:

sumFile("myfile.txt") will return 16, if myfile.txt contains:

1
2
3
10

nameInFile(user, filename)

Takes a username (user) and the name of a file (filename)
Loop over all the lines in the file, if a line contains the username (the line will be name="user") then return True. Otherwise if the name is not in the file return False.
Return True or False (boolean values, not strings)
Example:

nameInFile('casey', 'secret_file') will return True, if secret_file.txt contains:

name=casey
password=walrus7
name=riley
password=python_is_fun
main()

You will not be graded on main, but you should use it to call the functions to test that they are working correctly.

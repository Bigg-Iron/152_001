# Lab 9 Assignment

This lab should:

Open and process a file line by line.
Print the username and account balance of every account-holder.
Round every balance to 2 decimal places.
The outputs must EXACTLY match the example provided including whitespace.
A single line in the file looks like this, where the account balance is the sum of the floating-point numbers.:

FirstName,LastName:1830.20, 12904.1, -123.89, 594.014
Here are the specifications for the functions you will be writing:

processFile(filename)
Takes the name of the file to be processed.
Loops over each line of the file. For every line, call processLine() and print its result.

processLine(line)
Takes one line as a string.
Use string functions to extract relevant information from the line. Call makeUserName() and getAmount() using the information extracted.
The usernames should be 7 spaces right-justified.
Return a formatted string that exactly matches the example shown below. Do NOT print anything in this function.
HINT - You can call string split function with different delimiters. Notice, names and numbers are separated by a colon ":"
Example:

processLine('FirstName,LastName:1830.20, 12904.1, -123.89, 594.014')

 returns Username: Flastna - Account Balance: 15295.21

makeUserName(user_name)
Takes a string (user_name) that contains a first and last name separated by a comma. (First,Last).
Create a username using the first letter of the first name, followed by the first 6 characters of the last name in lowercase.
Return the final username as a string.
Example:

makeUserName('FirstName,LastName')

 returns Flastna

getAmount(amounts)
Takes a string (amounts) containing an unknown amount floating-point numbers separated by commas.
Calculate the sum of the numbers, rounded to 2 decimal places.
Return the sum.
Example Input
Note: Don't forget to provide a filename in the smaller input box below.
sample2.txt contains:

Dave,Matthews:-385109.42360, 18509.2260,94234623, 591923.23626, 589248.236236, 81499.23663
Mridula,Bontha: 1819.92634, 13220.98, -589120.96262, -18510.1452
Rachel,Hirsch: 78240.0453, -2149.9553, 19504.0287, 28931.2343, -5823.0962, 8501.7572
Casey,Key: 89420.23532
Example Output:
filename?
Username: Dmatthe - Account Balance: 95130693.51
Username: Mbontha - Account Balance: -592590.20
Username: Rhirsch - Account Balance: 127204.01
Username:    Ckey - Account Balance: 89420.24
Provided Files
Note: Your code will be tested with other, secret files, in addition to these.

sample1.txt
sample2.txt

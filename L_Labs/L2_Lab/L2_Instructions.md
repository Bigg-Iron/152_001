# Lab Assignment:

For this lab, pretend you are a programmer who is writing a program to help a grocery store manage their inventory. The store manager has asked you to help her organize her fruit department. She has given you this table of information about the fruit.

```text
Fruit       Id      Price       In stock        Color       Amount
Apple	     0	    0.59        True	        Red	          281
Pear	     1	    0.92        False	        Green           0
Blueberry    2	    0.12	    True	        Blue         3499
Orange	     3	    1.07	    True	        Orange          9
Strawberry   4	    0.49	    False	        Red             0
Lime         5	    8.23	    False	        Green           0
Lemon        6	    5.42	    True	        Yellow        324
```

The manager wants to be able to enter any fruit, and then receive that fruit's information. For example when she inputs Apple, the output should exactly match Apple , 0 , 0.59 , True , Red , 281.

This program should:

Prompt the user to "Enter a fruit?".
Ask for input using the prompt shown in the example below.
Store the input in a variable.

Print the information corresponding with the given fruit according to the table above, and in the format shown below.
Create a dictionary called fruit2Id. The keys will be the name of every fruit as a string. The values will be the Id of each fruit, as an integer. For example, if given fruit2Id['Lime'] the returned value will be 5.
Create four lists, one for each category (price, inStock, color, and amount). Each list will contain its respective information for every fruit, in the same order they appear on the table above.
Use the inputted fruit with fruit2Id to get a fruit's Id (index). That Id can then be used to retrieve a fruit's corresponding information from the lists created earlier. Print this information in the exact format shown below. Here's an example of the interaction between the lists and the dictionary:

index = fruit2Id['Apple']
print('Price of apple is ', price[index])

Input Example:
Note: While testing in develop mode, don't forget to provide the program with input values in the smaller box below.

```txt
Apple
Output Example:
Enter a fruit?
Apple , 0 , 0.59 , True , Red , 281
```

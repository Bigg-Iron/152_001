# 10.11 L10 - Lab

This program should:

Use three functions to iterate over 2D lists in different ways. These functions will return the number of times a given thing appears in the rows, columns, or grids of the 2D list. Here is a recommendation for solving these problems:
Write a nested for loop that prints the indices for the desired values.
Use these indices to count the number of things in one unit of the problem (i.e. one row, one column, one grid).
Repeatedly append that count to a list within the for loop. After the for loop, return that list.
Here are the specifications for the three functions:

countInRows(l, thing)
Takes a 2D list of any size and a string thing.
Counts the number of times thing appears in each row.
Returns a list holding the counts of thing for each row.

countInCols(l, thing)
Takes a 2D list of any size and a string thing.
Counts the number of times thing appears in each column.
Returns a list holding the counts of thing for each column.

countIn2x2Grids(l, thing)
Takes a 2D list of any even dimensions and a string thing.
Counts the number of times thing appears in each 2 X 2 grid by calling countInGrid with the upper-left index of every grid, then append that number to the final list.
Returns a list holding the counts of thing for each 2 X 2 grid.

countInGrid(l, thing, start_i, start_j)
Takes a 2D list, a string thing, a start index, and an end index.
Use the start and end indices to isolate one 2x2 grid and count the number of times thing appears only in that 2x2 grid.
Return the count of thing found in the grid as an int.
Example Input:

```python
l =    [ ["A", 1 , 2 , 3 , 4 , 5],
         ["A","A", 2 , 3 , 4 , 5],
         [ 1 , 2 , 3 , 4 , 5 , 5 ],
         ["A","A","A","A","A","A"],
         ["A", 3 ,"A", 4 ,"A","A"],
         [ 1 , 3 , 5 ,"A", 5 ,"A"] ]

```

Example Outputs:
countInRows(l, thing):

countInRows(l, 'A') = [1, 2, 0, 6, 4, 2]
countInCols(l, thing):

countInCols(l, 'A') = [4, 2, 2, 2, 2, 3]
countIn2x2Grids(l, thing):

countIn2x2Grids(l, 'A') = [3, 0, 0, 2, 2, 2, 1, 2, 3]

# 10.12 A10 Program

Assignment
This program should:

Read the 9x9 grid of numbers from a file.
This is done in get_sudoku(), which should return a two-dimensional list containing the 9x9 sudoku.

Determine if each row, column, and subgrid contains all of the digits from 1 to 9.
Each row, column, and subgrid should be checked in their respective function (okrows() checks rows, etc.). Each function will return either True or False.
Hint: Collect the values from a row, column, or subgrid in a list, sort the list, and compare the list with valid defined at the top of the program.
Here are the specifications for the functions you will be writing:

You also are provided with a global variable, valid , that contains an ordered valid line. Use this to compare.

get_sudoku(filename) This is provided for you
Creates a 2D list containing a sudoku grid from a text file.

`okrows(sudoku)`
Takes a 2D list containing a sudoku grid.
Loop over each row in the sudoku to check if it's valid.
Return True (boolean value, not a string) if all rows are valid, False otherwise.

`okcols(sudoku)`
Takes a 2D list containing a sudoku grid.
Loop over each column in the sudoku to check if it's valid.
Return True (boolean value, not a string) if all columns are valid, False otherwise.

`okgrid(sudoku, r, c)`
Takes a 2D list containing a sudoku grid, a row index, and a column index.
Check if the 3x3 grid is valid. r and c represent the upper-left most index of the grid.
Return True (boolean value, not a string) if the 3x3 grid is valid, False otherwise.

`okgrids(sudoku)`
Takes a 2D list containing a sudoku grid.
Checks if all nine 3x3 grids are vaild by calling okgrid.
Return True (boolean value, not a string) if all nine 3x3 grids are valid, False otherwise.
A word of advice: implement the okgrid() function last, after everything else works. It is only worth one point and is not included in the output test comparisons. You can leave it as is to still earn 9/10 points on the assignment.

Example Input
Note: While testing in develop mode, don't forget to provide the program with the name of a file in the smaller box below.

The input files will contain 9 lines with 9 numbers in each line separated by spaces.

grid1 is particularly good for testing rows and columns, as they are ordered for you:
1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
4 5 6 7 8 9 1 2 3
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8

grid2 is a solved version of the puzzle, without ordered rows and columns:
4 3 5 2 6 9 7 8 1
6 8 2 5 7 1 4 9 3
1 9 7 8 3 4 5 6 2
8 2 6 1 9 5 3 4 7
3 7 4 6 8 2 9 1 5
9 5 1 7 4 3 6 2 8
5 1 9 3 2 6 8 7 4
2 4 8 9 5 7 1 3 6
7 6 3 4 1 8 2 5 9

grid3 is a random puzzle:
9 3 8 5 9 7 2 4 1
6 7 6 5 4 3 1 8 2
7 9 6 5 2 1 4 3 8
6 3 9 2 1 4 8 7 5
4 6 2 1 7 9 5 3 8
3 5 8 9 6 2 4 1 7
8 3 2 9 7 4 1 5 6
7 1 2 5 4 6 8 3 9
6 2 5 4 1 8 7 9 3

Example Output
The output shows whether the row, column, and grids were individually valid and whether the puzzle is solved.

Sample output for grid1:
[True, True, False] False

Sample output for grid2:
[True, True, True] True

Sample output for grid3:
[False, False, False] False

/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/A_programs/A10_Program/grid3
Test Data
You DO NOT need to download the text files provided for your program to run. You may download them if you wish, but zybooks can access them whether they are on your computer or not. For zybooks to access a file, you must enter its name in the smaller input box below. The following test files are available for use during your development:

grid1 the first example above.
grid2 the second example above.
grid3 the third example above.
grid4 was not shown above but contains another random puzzle.

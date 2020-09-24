# 9.9 A9 Program

Background
Consider a triangle with sides of lengths a, b, and c where c is the longest side. We can describe the side and angle properties of the triangle using these lengths.

The side properties include:

scalene if all three sides have a different length
isosceles if two of the sides have the same length
equilateral if all three sides have the same length
The Pythagorean Theorem determines the angle properties which include:

acute if all angles are acute (<90 degrees) or a**2 + b**2 > c**2
right if one angle is right (=90 degrees) or a**2 + b**2 = c**2
obtuse if one angle is obtuse *(>90 degrees) or a**2 + b**2 < c**2
NOTE: the sides do not represent a triangle if a + b <= c. Both the side and angle relationships should be none in this case.

Solution
Complete the following program to:

prompt for a filename
print a heading for the output
print a line with the side and triangle properties for each triangle in the file
Example Input
Each line in the file contains 3 numbers separated by spaces that represent the side lengths of the triangle as in the following example. The lengths may be in any order on the line.

5 4 3
4 4 4
Example Output
The side lengths and properties should align with the column headings as in the following example. The side lengths should be right justified and in the same order as the input file, while the properties should be left justified.

111 222 333 angle side
  5   4   3 right scal
  4   4   4 acute equi
Test Data File
There is a single test file, triangles you may use to test your program during development.

3 5 4
3 4 4
3 3 6
4 4 4
2 11 4
6 4 3

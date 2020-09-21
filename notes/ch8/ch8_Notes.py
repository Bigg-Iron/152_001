# Ch8. Notes and Examples

# File system
# print('Opening file myfile.txt.')
# f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/myfile.txt') # create file object

# print('Reading file myfile.txt.')
# contents = f.read()  # read file text into a string

# print('Closing file myfile.txt.')
# f.close()  # close the file

# print('\nContents of myfile.txt:\n', contents)

# import os

# # Open a file with default line-buffering.
# f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/myfile.txt', 'w')

# # No newline character, so not written to disk immediately
# f.write('Write me to a file, please!')

# # Force output buffer to be written to disk
# f.flush()
# os.fsync(f.fileno())

import csv

# with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/test.csv', 'r') as csvfile:
#     grades_reader = csv.reader(csvfile, delimiter=',')

#     row_num = 1
#     for row in grades_reader:
#         print('Row #{}:'.format(row_num), row)
#         row_num += 1




# Figure 8.4.3: Using csv file contents to perform calculations.

# Dictionary that maps student names to a list of scores
grades = {}
# Use with statement to guarantee file closure
with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/test.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted + 
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print('{} earned {:.1f}%'.format(student, score))
    
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
# grades = {}
# # Use with statement to guarantee file closure
# with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/test.csv', 'r') as csvfile:
#     grades_reader = csv.reader(csvfile, delimiter=',')

#     first_row = True
#     for row in grades_reader:
#         # Skip the first row with column names
#         if first_row:
#             first_row = False
#             continue

#         ## Calculate final student grade ##

#         name = row[0]

#         # Convert score strings into floats
#         scores = [float(cell) for cell in row[1:]]

#         hw1_weighted = scores[0]/10 * 0.05
#         hw2_weighted = scores[1]/10 * 0.05
#         mid_weighted = scores[2]/100 * 0.40
#         fin_weighted = scores[3]/100 * 0.50

#         grades[name] = (hw1_weighted + hw2_weighted + 
#                         mid_weighted + fin_weighted) * 100

# for student, score in grades.items():
#     print('{} earned {:.1f}%'.format(student, score))


# 8.5.1: Using command-line arguments to specify the name of an input file.
import sys
import os

# if len(sys.argv) != 2:
#     print('Usage: {} input_file'.format(sys.argv[0]))
#     sys.exit(1)  # 1 indicates error

# print('Opening file {}.'.format(sys.argv[1]))

# if not os.path.exists(sys.argv[1]):  # Make sure file exists
#     print('File does not exist.')
#     sys.exit(1)  # 1 indicates error

# f = open(sys.argv[1], 'r')

# # Input files should contain two integers on separate lines

# print('Reading two integers.')
# num1 = int(f.readline())
# num2 = int(f.readline())

# print('Closing file {}'.format(sys.argv[1]))
# f.close()  # Done with the file, so close it

# print('\nnum1: {}'.format(num1))
# print('num2: {}'.format(num2))
# print('num1 + num2: {}'.format(num1 + num2))



# import datetime

# curr_day = datetime.date(1997, 8, 29)

# num_days = 30
# for i in range(num_days):
#     year = str(curr_day.year)
#     month = str(curr_day.month)
#     day = str(curr_day.day)

#     # Build path string using current OS path separator
#     file_path = os.path.join('logs', year, month, day, 'log.txt')

#     f = open(file_path, 'r')
#     print('{}: {}'.format(file_path, f.read()))
#     f.close()

#     curr_day = curr_day + datetime.timedelta(days=1)
    
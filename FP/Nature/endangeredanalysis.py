import math
import os
import numpy 
import matplotlib
import csv


# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
def county(contents):
    print(contents)
    


# TODO:
# category(): Should return a dictionary containing an entry for each category containing a count of species in each NY listing
def category():
    pass


# TODO:
# group(): Should return a dictionary containing an entry for each Taxonomic Group containing a count of species in each NY Listing
def group():
    pass


# TODO:
# subgroup(): Should return a dictionary containing an entry for each Taxonomic Subgroup containing a count of species in each NY Listing
def subgroup():
    pass



# TODO:
# common(): Should return a dictionary containing an entry for each Common Name containing a count of species in each NY Listing
def common():
    pass



# TODO:
# init()` - This function should parse your CSV file and read all the lines. Lines read by this function should be reused by the rest of the functions. In this way, you avoid reading the file multiple times for each of your functions.
fields = []
rows = []
def init(filename):
    dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP/Nature/', os.O_RDONLY)
    
    with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP/Nature/' + filename, 'r+') as f:
        contents = f.readlines()
        # creating a csv reader object 
        csvreader = csv.reader(contents) 
        # extracting field names through first row 
        fields = next(csvreader) 
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 

    # printing the field names 
    print('Field names are: ') 
    for field in fields:
        print('{}'.format(field))
    #  printing first 5 rows 
    print('\nFirst 5 rows are:\n') 
    for row in rows[:5]: 
        # parsing each column of a row 
        for col in row: 
            print("%10s"%col), 
        print('\n') 
        # reader = csv.reader(contents)
        # print('opened', file=f)
        os.close(dir_fd)  # don't leak a file descriptor
        return contents 


# Function calls to test
# init(filename='endangeredtest.csv')
county(contents=init(filename='testdata.csv'))

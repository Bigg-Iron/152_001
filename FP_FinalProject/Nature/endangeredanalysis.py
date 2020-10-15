import math
import pandas
import os
import numpy 
import matplotlib
import csv


# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
def county(contents):
    counties_List = []
    reader = csv.DictReader(contents)
    for row in reader:
        print('-' * 30)
        print(reader.line_num)
        print('Category: {category}'.format(category=row['Category']))
        print('County: {county}'.format(county=row['County']))
        print('Taxonomic Group: {taxonomicGrp}'.format(taxonomicGrp=row['Taxonomic Group']))
        print('Taxonomic Subgroup: {taxonomicSub}'.format(taxonomicSub=row['Taxonomic Subgroup']))
        print('Scientific Name: {scientificName}'.format(scientificName=row['Scientific Name']))
        print('Common Name: {commonName}'.format(commonName=row['Common Name']))
        
        counties_List.append(row)

        # print('Category: {category}'.format(category=row['Category']))
        # print('Year Last Documented: {}'.format(row['Year Last Documented']))
        # print('NY Listing Status: {}'.format(row['NY Listing Status']))
        # print('Federal Listing Status: {}'.format(row['Federal Listing Status']))
        # print('State Conservation Rank: {}'.format(row['State Conservation Rank']))
        # print('Global Conservation Rank: {}'.format(row['Global Conservation Rank']))
        # print('Distribution Status: {}'.format(row['Distribution Status']))
    # cl = sorted(counties_List,key=len)
    print(dict(counties_List))


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
    dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/', os.O_RDONLY)
    
    with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/' + filename, 'r+') as f:
        contents = f.readlines()
        # creating a csv reader object 
        csvreader = csv.reader(contents) 
        # extracting field names through first row 
        fields = next(csvreader) 
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
        # get total number of rows 
        print("Total no. of rows: {}".format(csvreader.line_num)) 

    # printing the field names 
    print('\nField names are: ') 
    print('-'*24)
    for field in fields:
        print('{:<}'.format(field))
    #  printing first 5 rows 
    print('\nDataset #1:') 
    print('-'*24)
    for row in rows: 
        # parsing each column of a row 
        for col in row: 
            print('{:<}'.format(col)) 
        print('-'*24) 
        # reader = csv.reader(contents)
        # print('opened', file=f)
        os.close(dir_fd)  # don't leak a file descriptor
        return contents 


# Function calls to test
# init(filename='endangeredtest.csv')
county(contents=init(filename='testdata.csv'))

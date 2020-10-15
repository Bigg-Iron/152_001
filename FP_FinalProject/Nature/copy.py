import math
import pandas
import os
import numpy 
import matplotlib
import csv
from collections import Counter


_Endangered = []
_Rare = []
_Threatened = []
_Category = []
_Average = 0
_Total = 0



# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
def county(contents):
    pass
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
def init(filename):
    
    dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/', os.O_RDONLY)
    
    with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/' + filename, 'r+') as f:
        contents = f.readlines()
        # creating a csv reader object 
        reader = csv.DictReader(contents,dialect=csv)
        for row in reader:
            print(row['NY Listing Status'])
            if row['NY Listing Status'] == 'Threatened':
                global _Threatened
                _Threatened.append(row['NY Listing Status'])

            elif row['NY Listing Status'] == 'Endangered':
                global _Endangered
                _Endangered.append(row['NY Listing Status'])
                
            elif row['NY Listing Status'] == 'Rare':
                global _Rare
                _Rare.append(row['NY Listing Status'])

        global _Total
        _Total = len(_Threatened) + len(_Endangered) + len(_Rare)

        headers = '{Endangered:>}  {Rare:>} {Threatened:>}   {Total:>} {Category:>}'

        table = '{Endangered:>10}  {Rare:>4}  {Threatened:>9}  {Total:>6} {Category:>8}'

        print(headers.format(Endangered='Endangered', Rare='Rare', Threatened='Threatened', Total='Total', Category='Category'))
        print(table.format(Endangered=len(_Endangered), Rare=len(_Rare), Threatened=len(_Threatened), Total=_Total, Category='Animal'))


 

        os.close(dir_fd)  # don't leak a file descriptor
        return reader 



# Function calls to test
init(filename='testdata.csv')

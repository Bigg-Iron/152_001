import math
import pandas
import os
import numpy 
import matplotlib
import csv
from collections import Counter


_Endangered = {'Endangered': 0}
_Rare = {'Rare': 0}
_Threatened = {'Threatened': 0}
_Total = 0
_Animal = {}
_Plant = {}
_Category = {'Animal':len(_Animal), 'Plant':len(_Plant)}
_Average = 0



# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
def county():
    pass



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
        e_count = 0
        t_count = 0
        r_count = 0
        for line in reader:
            # print('\n',line['Category'])
            # print(line['NY Listing Status'])
            # print(line['County'])
            # print(line['Taxonomic Subgroup'])
            # print(line['Common Name'])
            # print(line['Taxonomic Group'], '\n')
            # print('-'*30)

            if line['NY Listing Status'] == 'Endangered':
                e_count+=1
                _Endangered.update({'Endangered': e_count})
            elif line['NY Listing Status'] == 'Rare':
                r_count+=1
                _Rare.update({'Rare': r_count})
            elif line['NY Listing Status'] == 'Threatened':
                t_count+=1
                _Threatened.update({'Threatened': t_count})


        print('\n Endangered:{} Rare:{} Threatened:{}'.format(_Endangered.get('Endangered'), _Rare.get('Rare'), _Threatened.get('Threatened')))


        print('done')

 

        os.close(dir_fd)  # don't leak a file descriptor
        return reader 



# Function calls to test
init(filename='testdata.csv')
# category()

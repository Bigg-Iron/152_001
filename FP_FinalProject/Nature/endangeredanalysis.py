import math
import pandas
import os
import numpy 
import matplotlib
import csv
from collections import Counter


ecount = 0
_Endangered = {'Endangered':0}
rcount=0
_Rare = {'Rare':0}
tcount=0
_Threatened = {'Threatened': 0}
_Total = 0
_Category = {}
_Animal = {'Animal':0}
_Plant = {'Plant': 0}
_Average = 0



# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
def county(contents):
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
        for row in reader:
            if row['NY Listing Status'] == 'Threatened':
                global tcount
                tcount+=1
                global _Threatened
                _Threatened.update({'Threatened' : tcount})

            elif row['NY Listing Status'] == 'Endangered':
                global ecount
                ecount+=1
                global _Endangered
                _Endangered.update({'Endangered': ecount})
                
            elif row['NY Listing Status'] == 'Rare':
                global rcount
                rcount+=1
                global _Rare
                _Rare.update({'Rare': rcount})
        


        global _Total
        _Total = _Endangered.get('Endangered') + _Rare.get('Rare') + _Threatened.get('Threatened')

        headers = '\n{Endangered:>}  {Rare:>} {Threatened:>}   {Total:>} {Report:>}'

        table = '{Endangered:>10}  {Rare:>4}  {Threatened:>9}  {Total:>6} {Report:>8}'

        print(headers.format(Endangered='Endangered', Rare='Rare', Threatened='Threatened', Total='Total', Report='Category'))

        print(table.format(Endangered=_Endangered.get('Endangered'), Rare=_Rare.get('Rare'), Threatened=_Threatened.get('Threatened'), Total=_Total, Report='Animal'))

        # print(table.format(Endangered=len(_Endangered), Rare=len(_Rare), Threatened=len(_Threatened), Total=_Total, Category=_Category))

 

        os.close(dir_fd)  # don't leak a file descriptor
        return reader 



# Function calls to test
init(filename='testdata.csv')
# category()

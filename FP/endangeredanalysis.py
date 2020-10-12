import math
import os
import numpy 
import matplotlib


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

    dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP', os.O_RDONLY)
    
    with open(filename, 'w+') as f:
        print('opened', file=f)
        os.close(dir_fd)  # don't leak a file descriptor
        print('Done...')


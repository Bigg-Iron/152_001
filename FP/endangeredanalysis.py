import math
import os

# TODO: 
# county(): should return a dictionary containing an entry for each county containing a count of species in each NY listing
# category(): Should return a dictionary containing an entry for each category containing a count of species in each NY listing
# group(): Should return a dictionary containing an entry for each Taxonomic Group containing a count of species in each NY Listing
# subgroup(): Should return a dictionary containing an entry for each Taxonomic Subgroup containing a count of species in each NY Listing
# common(): Should return a dictionary containing an entry for each Common Name containing a count of species in each NY Listing


dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP', os.O_RDONLY)

def init(filename):
    
    with open(filename, 'w+') as f:
        print('opened', file=f)
        os.close(dir_fd)  # don't leak a file descriptor
        print('Done...')


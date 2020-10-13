import os
import requests


dir_fd = os.open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/ch13', os.O_RDONLY)

with open('output.txt', 'w') as f:
    print('This will be written to somedir/output.txt', file=f)

os.close(dir_fd)  # don't leak a file descriptor
    
    
r = requests

def browse():
    g = r.get(url='https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request')
    os.open('output.txt', mode='r+')
    print(g.text)

browse()
# Ch8. Notes and Examples

# File system
print('Opening file myfile.txt.')
f = open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/ch8/myfile.txt') # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:\n', contents)

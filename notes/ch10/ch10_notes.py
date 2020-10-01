""" 10.1.2: Modify a list.
Modify short_names by deleting the first element and changing the last element to Joe.

Sample output with input: 'Gertrude Sam Ann Joseph'
['Sam', 'Ann', 'Joe'] """

user_input = input()
short_names = user_input.split()

short_names = short_names.pop(0)
short_names[2] = 'Joe'

print(short_names)

# Expected output: ['Sam', 'Ann', 'Joe']



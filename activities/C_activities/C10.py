""" 10.1.2: Modify a list.
Modify short_names by deleting the first element and changing the last element to Joe.

Sample output with input: 'Gertrude Sam Ann Joseph'
['Sam', 'Ann', 'Joe']
 """
 
user_input = input()
short_names = user_input.split()

''' Your solution goes here '''
del short_names[0]
del short_names[-1]
short_names.append('Joe')
print(short_names)

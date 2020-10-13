import re

s = '.rot.at.o.r'
print(s)

result = re.sub('[\W_]+', '', s) 

print(result)

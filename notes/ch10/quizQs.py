# t = [[2, 1, 3], 
#      [3, 4], 
#      [9, 5, 2], 
#      [6, 7]]

# for r in t:
#   r.sort(reverse=True)

# s = 0
# for r in t:
#   s += r[0] - sum(r[1:]) 

# print(s)

def inv(d):
      return 1/d

t = [1,5,4,2,10]
t.sort(key=inv)

print(t)
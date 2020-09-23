# Questions from quizzes

# def f3(s):
#     i = 0
#     r = ''
#     while i < len(s):
#         r = s[i] + r
#         i += 2
#         return r

# print(f3('wake up'))

# s = 0
# v = 0.5
# n = 100

# while n > 1:
#   s += v
#   v /= 2
#   n -= 1

# print(s)

# s = "Rotator"
# t = ""
# i = 0

# while i < len(s):
#   if i % 2 == 0:
#     t = s[i] + t
#   i += 1

# print(t)



# def f1(n):
#     s = 1
#     while n > 1:
#         s *= n
#         n -= 1
#         return s
        
# print(f1(5))

# def f2(s):
#     i = 0
#     while s[i] != ' ':
#         i += 1
#         return i

# print(f2('Colo State Uni'), f2('CSU'))


# s = 0
# for i in range(2, 10, 2):
#   s += i

# print(s)

# s = 0
# l = [5, 4, 3, 2, 1]
# for (i, v) in enumerate(l):
#   s += v - i

# print(s)

# s = 0
# p = 1
# l = [1, 5, 2, 4, 5, 3, 3, 2, 4, 1]
# for v in sorted(l):
#   if v == p:
#     continue
#   s += v
#   p = v

# print(s)


# def f1(s):
#     r = ''
#     for c in reversed(s):
#         if c == ' ':
#             break
#         r = r + c
#     return r

# print(f1('C S U'), f1('CSU'))

# def f2(s):
#     for (i, c) in enumerate(s):
#         if c == " ":
#             return i

# print(f2('Colorado State '), f2 ('CSU'))

# def f3(n,s):
#     for v in range(n, 1, -1):
#         print(v, end='.')
#     print(s)

# f3(3, 'wake up')


# /Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/testfile.txt

# with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/testfile.txt') as r:
#   with open('other', 'w') as w:
#     o = ''
#     for l in r:
#       o = l + o
#     w.write(o)

# with open('other', 'r') as f:
#   print(f.read())
  
# import csv
# with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/a.csv') as f:
#   rdr = csv.reader(f, delimiter=',')
#   word = []
#   i = 1
#   for line in rdr:
#     word.append(line[i % 2])
#     i += 1

# print(word)

import csv
with open('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/notes/b.csv','r') as f:
  rdr = csv.DictReader(f, delimiter=',')
  word = []
  i = 0
  code = ["C","A","B","F","A"]
  for line in rdr:
    word.append(line[code[i]])
    i += 1
print(word)

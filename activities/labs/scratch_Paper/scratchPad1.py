# Quiz questions

# from math import e, pi

# d = {'d':'b', 'c':'a', 'm':'d'}
# q = 3 / 4 == 0.75
# r = 4 > pi > 3 > e > 2
# s = 'a' in d
# t = not q or r and s 

# print(q,  r,  s,  t)


# q = 1
# r = 2
# s = 3
# l = [1, 3, 5, 7, 9, 11, 13]

# e = r
# w = q < r > s 
# x = s in l 
# y = e is not l
# z = not w or x and y

# print(z)


# def g(q, r):
#       if r == 0:
#         return q
#       else:
#         return g(r, q % r)

# print(g(9, 6))


"""
This is a pure Python implementation of the shell sort algorithm
For doctests run following command:
python -m doctest -v shell_sort.py
or
python3 -m doctest -v shell_sort.py
For manual testing run:
python shell_sort.py
"""


def shell_sort(collection):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        for i in range(gap, len(collection)):
            j = i
            while j >= gap and collection[j] < collection[j - gap]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
                j -= gap
    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(shell_sort(unsorted))
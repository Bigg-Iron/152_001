s = 'The quick brown fox jumped over the lazy dog.'
d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for c in s.lower():
    if c in d:
        d[c] += 1
print([t[1] for t in sorted(d.items())])

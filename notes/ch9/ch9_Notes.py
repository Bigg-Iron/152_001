# url = 'http://en.wikipedia.org/wiki/Turing'
# domain = url[7:23] # Read wikipedia from url

# print(domain)

# state = 'New York'
# state_slice = state[0:2]
# print(state_slice)

format_string = '{name:16}{goals:8}'


print(format_string.format(name='Player Name', goals='Goals'))

print('-' * 24)


print(format_string.format(name='Sadio Mane', goals=22))

print(format_string.format(name='Gabriel Jesus', goals=7))

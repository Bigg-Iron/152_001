# C 9.1.2:
# start_index = int(input())
# end_index = int(input())
# rhyme_lyric = 'The cow jumped over the moon.'
# sub_lyric = rhyme_lyric[start_index:end_index]
# print(sub_lyric)


''' 9.2.2: Printing a string.
Write a single statement to print: user_word,user_number. Note that there is no space between the comma and user_number.

Sample output with inputs: 'Amy' 5
Amy,5 '''

# user_word = str(input())
# user_number = int(input())

# ''' Your solution goes here '''
# print('{},{}'.format(user_word,user_number))

# format_string = '{name:7}{goals:4}{games:5}'
# print(format_string.format(name='Jack', games=29, goals=9))	

""" 9.3.2: Format temperature output.
Print air_temperature with 1 decimal point followed by C.

Sample output with input: 36.4158102
36.4C """

# air_temperature = float(input())
''' Your solution goes here '''
# print('{x:.1f}C'.format(x=air_temperature))


""" 9.4.1: Find abbreviation.
Complete the if-else statement to print 'LOL means laughing out loud' if user_tweet contains 'LOL'.

Sample output with input: 'I was LOL during the whole movie!'
LOL means laughing out loud. """

# user_tweet = input()

# ''' Your solution goes here '''
# if 'LOL' in user_tweet:
#     print('LOL means laughing out loud.')
# else:
#     print('No abbreviation.')

""" 9.4.2: Replace abbreviation.
Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL' with 'talk to you later'.

Sample output with input: 'Gotta go. I will TTYL.'
Gotta go. I will talk to you later. """

# user_tweet = input()

# decoded_tweet =   user_tweet.replace('TTYL', 'talk to you later') 
# print(decoded_tweet)


# item_info = 'Mug 14 20'

# item_tokens = item_info.split()
# item = item_tokens[0]
# quantity = item_tokens[1]
# price = item_tokens[2]

# print(item, 'stock:', quantity)
# print('Price:', price)


# address = 'www.google.com'

# separator = ':'
# address_tokens = address.split('.')
# print(separator.join(address_tokens))

""" 9.5.2: Extract area code.
Assign number_segments with phone_number split by the hyphens.

Sample output with input: '977-555-3221'
Area code: 977 """

phone_number = input()
number_segments = ''' Your solution goes here '''
area_code = number_segments[0]
print('Area code:', area_code)


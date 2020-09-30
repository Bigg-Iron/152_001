""" 11.1.1: Delete from dictionary.
Delete Prussia from country_capital.

Sample output with input: 'Spain:Madrid,Togo:Lome,Prussia: Konigsberg'
Prussia deleted? Yes.
Spain deleted? No.
Togo deleted? No. """

# user_input = input()
# entries = user_input.split(',')
# country_capital = dict(pair.split(':') for pair in entries)
# # country_capital is now a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris' }
# ''' Your solution goes here '''
# del country_capital['Prussia']

# print('Prussia deleted?', end=' ')
# if 'Prussia' in country_capital:
#     print('No.')
# else:
#     print('Yes.')

# print ('Spain deleted?', end=' ')
# if 'Spain' in country_capital:
#     print('No.')
# else:
#     print('Yes.')


""" 11.1.2: Enter the output of dictionaries. """

# airport_codes = {}
# airport_codes['Osaka'] = 'KIX'
# airport_codes['Houston'] = 'IAH'
# airport_codes['Los Angeles'] = 'LAX'

# print(airport_codes['Osaka'])
# print(airport_codes['Los Angeles'])	

# airport_codes = {
#     'Osaka': 'KIX',
#     'Paris': 'CDG',
#     'Tokyo': 'NRT'
# }

# print(airport_codes['Osaka'])
# airport_codes['Osaka'] = 'ITM'
# print(airport_codes['Paris'])
# print(airport_codes['Osaka'])	


# provincial_capitals = {
#     'Yukon': 'Whitehorse',
#     'Manitoba': 'Winnipeg',
#     'Ontario': 'Toronto',
#     'Alberta': 'Edmonton'
# }

# province_name = input()
# while province_name != 'exit':
#     if province_name in provincial_capitals:
#         print(provincial_capitals[province_name])
#     else:
#         print('x')
#     province_name = input()


# "New" means new compared to previous level
provincial_capitals = {
    'Nunavut': 'Iqaluit',
    'Alberta': 'Edmonton',
    'Yukon': 'Whitehorse',
    'Ontario': 'Toronto'
}

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
        del provincial_capitals[province_name] # New line
    else:
        print('x')
    province_name = input()
    
    
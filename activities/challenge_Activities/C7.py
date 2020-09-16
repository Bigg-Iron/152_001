# For loops
# channels = {
#     'MTV': 35,
#     'CNN': 28,
#     'FOX': 11,
#     'NBC': 4,
#     'CBS': 12
# }

# for c in channels:
#     print('{} is on channel {}'.format(c, channels[c]))

''' 7.2.2: For loop: Printing a list
Write an expression to print each price in stock_prices.

Sample output with inputs: 34.62 76.30 85.05
$ 34.62
$ 76.30
$ 85.05 '''

# NOTE: The following statement converts the input into a list container
# stock_prices = input().split()

# for price in stock_prices:
#     print('$', price)


''' 7.2.3: For loop: Printing a dictionary
Write a for loop to print each contact in contact_emails.

Sample output with inputs: 'Alf' 'alf1@hmail.com'
mike.filt@bmail.com is Mike Filt
s.reyn@email.com is Sue Reyn
narty042@nmail.com is Nate Arty
alf1@hmail.com is Alf '''

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

''' Your solution goes here '''
for contact in contact_emails:
    print('{} is {}'.format(contact_emails[contact], contact))

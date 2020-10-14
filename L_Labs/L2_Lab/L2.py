fruit2Id = {
    'Apple':0,
    'Pear':1,
    'Blueberry':2,
    'Orange':3,
    'Strawberry':4,
    'Lime':5,
    'Lemon':6
}

price = [0.59,0.92,0.12,1.07,0.49,8.23,5.42]
inStock = [True,False,True,True,False,False,True]
color = ['Red','Green','Blue','Orange','Red','Green','Yellow']
amount = [281,0,3499,9,0,0,324]

fruit = input('Enter a fruit? ')

print(fruit, fruit2Id[fruit], price[fruit2Id[fruit]], inStock[fruit2Id[fruit]], color[fruit2Id[fruit]], amount[fruit2Id[fruit]],sep=' ,')

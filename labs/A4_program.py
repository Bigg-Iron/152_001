""" 4.13 A4 Program
Recipe conversions are a common practice, whether making dinner or performing a chemistry experiment. The initial recipe calls for a certain amount of each ingredient to make a certain number of servings. The new recipe is adjusted for a different number of servings.

The main function is provided for you. You need to write the body of the other three functions, convertIngredients, getIngredients, and printIngredients.

The program is designed to give you some experience returning multiple values and working with global values.

Sample input
Here is a simple recipe with equal parts of each ingredient for 12 ounce servings that we need to scale up for a party:

cup(s)
1
1
1
2
16

Sample Output
Here is the expected output for the sample input. You program should produce this output exactly:

What is the unit of measure?
Enter amount of lemon juice in cup(s)?
Enter amount of water in cup(s)?
Enter amount of agave nectar in cup(s)?
How many servings of Lemonade does this make?
Lemonade ingredients for 2.0 servings
1.0 cup(s) lemon juice
1.0 cup(s) water
1.0 cup(s) agave nectar
How many servings would you like to make?
Lemonade ingredients for 16.0 servings
8.0 cup(s) lemon juice
8.0 cup(s) water
8.0 cup(s) agave nectar 

"""

# ---------------------------------------------------------------

# Unit conversions

recipe = 'Lemonade'


def convertIngredients(lemon, water, sugar, servings, newServings):
	# obtain the number of servings required
    lemon = float(lemon) / float(servings) * float(newServings)
    water = float(water) / float(servings) * float(newServings)
    sugar = float(sugar) / float(servings) * float(newServings)
    servings = float(newServings)
	# return the amount of each ingredient required for the new serving size
    return lemon, water, sugar, servings


def getIngredients():
	# obtain input for each of the ingredients
    lemon = input('Enter amount of lemon juice in cup(s)?\n')
    water = input('Enter amount of water in cup(s)?\n')
    sugar = input('Enter amount of agave nectar in cup(s)?\n')
	# obtain input for how many servings these ingredients would make
    servings = input('How many servings of Lemonade does this make?\n')
    return lemon, water, sugar, servings


def printIngredients(lemon, water, sugar, servings):
	# print the ingredients required for an amount of servings
    print('Lemonade ingredients for', float(servings), 'servings')
    print(float(lemon), units, 'lemon juice')
    print(float(water), units, 'water')
    print(float(sugar), units, 'agave nectar')
    


def main():
	# convert a recipe to a different number of servings
	global units
	units = input('What is the unit of measure?\n')
	lemon, water, sugar, servings = getIngredients()
	printIngredients(lemon, water, sugar, servings)
	newServings = float(input('How many servings would you like to make?\n'))
	lemon, water, sugar, servings = convertIngredients(lemon, water, sugar, servings, newServings)
	printIngredients(lemon, water, sugar, servings)


if __name__ == '__main__':
	main()

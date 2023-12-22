'''
Week 2
Complete Camel Case, Coke Machine, Just setting up my twitter, Vanity Plates, and Nutrition Facts.
'''

# switches from camelCase to snake_case
def camel():
	string = input('camelCase: ')
	newString = ''

	for char in string:
		if (char.upper() == char):
			newString = f'{newString}_{char.lower()}'
		else:
			newString = f'{newString}{char}'

	print ( f'snake_case: {newString}' )

# vending machine payment system
def coke():
	value = 50

	while (value > 0):
		print( f'Amount Due: {value}' )

		coin = int(input('Insert Coin: '))
		if (coin in [25, 10, 5]):
			value = value - coin

	print ( f'Change Owed: {0 - value}' )

# removes vowels from a string
def twitter():
	string = input('Enter a tweet: ')
	newString = ''

	for char in string:
		if (char.lower() not in 'aeiou'):
			newString = f'{newString}{char}'

	print( newString )

# determines if a string is a valid code
def plates():

	def is_valid(s):
		if len(s) < 2 or len(s) > 6:
			return False
		if not s[0].isalpha() or not s[1].isalpha():
			return False
		if not all(ch.isalnum() for ch in s):
			return False

		flag = False
		for ch in s:
			if ch.isdigit():
				flag = True
			if ch.isalpha() and flag:
				return False

		for ch in s:
			if ch.isdigit():
				return ch != '0'
		return True
	
	string = input('Plate: ')
	if is_valid(string):
		print('Valid')
	else:
		print('Invalid')

# displays the calories in a fruit
def nutrition():
	fruits = {
		'apple': 130,
		'avocado': 50,
		'banana': 110,
		'cantaloupe': 50,
		'grapefruit': 60,
		'grapes': 90,
		'honeydew melon': 50,
		'kiwifruit': 90,
		'lemon': 15,
		'lime': 20,
		'nectarine': 60,
		'orange': 80,
		'peach': 60,
		'pear': 100,
		'pineapple': 50,
		'plums': 70,
		'strawberries': 50,
		'sweet cherries': 100,
		'tangerine': 50,
		'watermelon': 80,
	}

	string = input('Item: ').lower()
	if string in fruits:
		print( F'Calories: {fruits[string]}' )


# execute every task
def main():
	camel()
	coke()
	twitter()
	plates()
	nutrition()

main()

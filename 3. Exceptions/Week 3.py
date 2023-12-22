'''
Week 3
Complete Fuel Gauge, Felipe's Taqueria, Grocery List, and Outdated.
'''

# determines the percentage of fuel left
def fuel():
	while True:
		string = input('Enter the fuel: ')
		if ('/' not in string):
			continue

		num1, num2 = string.split('/')
		try:
			num1 = int(num1)
			num2 = int(num2)
		except ValueError:
			continue

		if (num2 != 0) and (num1 <= num2):
			break

	percent = (num1 / num2) * 100

	if (percent <= 1):
		result = 'E'
	elif(percent >= 99):
		result = 'F'
	else:
		result = f'{percent:.0f}%'

	print( result )

# displays the cost for several items
def taqueria():
	menu = {
		'Baja Taco': 4.25,
		'Burrito': 7.50,
		'Bowl': 8.50,
		'Nachos': 11.00,
		'Quesadilla': 8.50,
		'Super Burrito': 8.50,
		'Super Quesadilla': 9.50,
		'Taco': 3.00,
		'Tortilla Salad': 8.00
	}

	total = 0
	while True:
		try:
			string = input('Item: ').title()
			if string in menu:
				total += menu[string]
				print( f'Total: ${total:.2f}' )

		except EOFError:
			break

# generates a shopping list
def grocery():
	dictionary = {}

	while True:
		try:
			value = input('').upper()
		except EOFError:
			break

		if value in dictionary:
			dictionary[value] += 1
		else:
			dictionary[value] = 1

	for value, key in sorted(dictionary.items()):
		print( f'{key} {value}' )

#
def outdated():
	months = [
		'January', 'February', 'March',
		'April', 'May', 'June',
		'July', 'August', 'September',
		'October', 'November', 'December',
	]

	while True:
		string = input('Date: ')

		if len(string.split('/')) == 3:
			string = string.split('/')
			try:
				month, day, year = map(int, string)
				if 1 <= month <= 12 and 1 <= day <= 31:
					print( f'{year:04d}-{month:02d}-{day:02d}' )
					break
			except ValueError:
				pass
		else:
			string = string.split(',')
			if len(string) == 2:
				try:
					month, day = string[0].split()
					month = months.index(month) + 1
					day, year = int(day), int(string[1])
					if 1 <= month <= 12 and 1 <= day <= 31:
						print( f'{year:04d}-{month:02d}-{day:02d}' )
						break
				except ValueError:
					pass


# execute every task
def main():
	fuel()
	taqueria()
	grocery()
	outdated()

main()

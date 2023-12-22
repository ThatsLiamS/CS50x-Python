'''
Week 1
Complete Deep Thought, Home Federal Savings Bank, File Extensions, Math Interpreter, and Meal Time.
'''

# determines the meaning of life...
def deep():
	string = input('What\'s the meaning of life: ').lower().strip(' ')
	if (string == '42') or (string == 'forty two') or (string == 'forty-two'):
		print( 'Yes' )
	else:
		print( 'No' )

# Seinfeld Season 7 Episode 24's Joke
def bank():
	string = input('Greeting: ').lower().strip(' ')
	money = 100
	
	if (string.startswith('hello')):
		money = 0
	elif (string.startswith('h')):
		money = 20
	
	print( f'${money}' )

# determines the file type based on extension
def extensions():
	string = input('Enter file name: ').split('.')[-1]
	type = 'application/octet-stream'

	match string.lower().strip():
		case 'gif':
			type = 'image/gif'
		case 'jpg':
			type = 'image/jpeg'
		case 'jpeg':
			type = 'image/jpeg'
		case 'png':
			type = 'image/png'
		case 'pdf':
			type = 'application/pdf'
		case 'txt':
			type = 'text/plain'
		case 'zip':
			type = 'application/zip'

	print( type )

# basic math calculator
def interpreter():
	num1, operation, num2 = input('Enter calculation: ').split(' ')
	result = 0

	match operation:
		case '+':
			result = float(num1) + float(num2)
		case '-':
			result = float(num1) - float(num2)
		case '*':
			result = float(num1) * float(num2)
		case '/':
			result = float(num1) / float(num2)
	
	print( f'{result:.1f}' )

# determines which meal to eat
def meal():
	string = input('Enter the time: ')

	hours, minutes = string.split(':')
	time = float(hours) + (int(minutes) / 60)

	if (time >= 7.0 and time <= 8.0):
		print ( 'breakfast time' )
	elif (time >= 12 and time <= 13):
		print ( 'lunch time' )
	elif (time >= 18 and time <= 19):
		print ( 'dinner time' )

# execute every task
def main():
	deep()
	bank()
	extensions()
	interpreter()
	meal()

main()

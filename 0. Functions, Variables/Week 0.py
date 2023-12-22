'''
Week 0
Complete Indoor Voice, Playback Speed, Making Faces, Einstein, and Tip Calculator.
'''

# converts a string to lowercase
def indoor():
	string = input('')
	print( string.lower() )

# replaces spaces with an ellipsis
def playback():
	string = input('')
	print( string.replace(' ', '...') )

# converts emoticons to emojis
def faces():
	string = input('')
	print( string.replace(':)', '🙂').replace(':(', '🙁') )

# calculate energy = mass * (speedOfLight) * (speedOfLight)
def einstein():
	number = int(input(''))
	print ( number * 300_000_000 * 300_000_000 )

# calculate how much to tip from a meal
def tip():
	dollars = input('How much was the meal? ').lstrip('$')
	percent = input('What percentage would you like to tip? ').rstrip('%')

	tip = float(dollars) * float(percent) / 100
	print( f'Leave ${tip:.2f}' )


# execute every task
def main():
	indoor()
	playback()
	faces()
	einstein()
	tip()

main()

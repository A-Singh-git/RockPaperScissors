
import random

while True:
	print("Select: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	num=int(input("Enter a number :"))
	
	# Loop until valid input
	while num <1 or num >3:
		num=int(input('Enter a valid choice please '))
		
	if num == 1:
		name= 'Rock'
	elif num == 2:
		name= 'Paper'
	elif num == 3:
		name= 'Scissors'

	print('User has selected: ',name, "\n The Computer is deciding... \n")
	
	# Computer selectes a random number from 1-3
	com_select = random.randint(1,3)
	
	# Initialise computer's choice
	while com_select == num:
		com_select = random.randint(1,3)

	if com_select == 1:
		com_name = 'Rock'
	elif com_select == 2:
		com_name = 'Paper'
	else:
		com_name = 'Scissors'

	print("The Computer's choice is \n", com_name)
	
	# Check for draw
	if num == com_select:
		print('It is a Draw')
		res='Draw'
		
	if (num==1 and com_select==3):
		print('Rock wins')
		res='Rock'
	elif (num==2 and com_select==1):
		print('Paper wins')
		res='Paper'
	elif (num==3 and com_select==2):
		print('Scissors wins')
		res='Scissors'
	else:
		print("User loses")
		res=""
		print("--Computer wins--")
						
	# Printing game state
	if res == name:
		print("--User wins--")
	if res == 'Draw':
		print("--Its a tie--")
	elif res== com_select:
		print("--Computer wins--")
		
	print("Do you want to play again? (y/n)")
	new_game = input().lower
	if new_game =='n':
		break

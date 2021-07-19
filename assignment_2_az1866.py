#import random and clear os
import random
import os
import csv
import operator

#randomly select board
random_board= '/mnt/c/Users/DELL/Desktop/cs/board_1.csv'

#open board
input_file= open(random_board,'r')

#take first line to get board dimensions and to get ans key
data_line1=input_file.readline().strip().split(',')

NUM_ROWS=int(data_line1[0])
NUM_COLS=int(data_line1[1])
answer_key=data_line1[2:]


#code for dynamically printing board
board=[]


for row in range(NUM_ROWS):
	line=input_file.readline().strip().split(',')
	row_list = []
	for col in range(NUM_COLS):
		row_list.append(line[col])
	board.append(row_list)

def print_board():
	for cols in range(NUM_ROWS):
		print(' ', end='')
	print("\n+" + "---+"*NUM_COLS)

	for row in range(NUM_ROWS): 
		print('|', end=' ')
		for col in range(NUM_COLS):
			print(board[row][col] + ' | ', end='') 
		print("\n+"+"---+"*NUM_COLS)

#print initial board
print_board()


#input number of players
ask_user= input('Please enter the number of players: ')
	#error check for number of players
while not ask_user.isdigit():
	print('Please enter an integer!')
	ask_user= input('Please enter the number of players: ')


random_first_turn= random.randint(0,int(ask_user)-1)

#make a list to store the order of turns
list_players=[]


for num in range(int(ask_user))[random_first_turn:int(ask_user)]:
	list_players.append(num)

for num_initial in range(int(ask_user))[0:random_first_turn]:
	list_players.append(num_initial)


#tell which player is playing first
print('Player '+ str(random_first_turn)+ ' gets to go first.\n')

#make a list to store the guesses the user makes, this will be compared with the ans key to decide when to stop the game 
guess=[]

#make seperate dictionaries to store the guess count i.e. score and the guesses made by the user. 
scores={}
player_guess_list={}


#set iniial score as 0 and initial guess as nil for every player
for Player in list_players:
	scores[Player]=0
	player_guess_list[Player]= ''


#run turns till all words are found
while len(guess)!=len(answer_key):

	#run the following code for every player in the list
	for turn in list_players:

		#ask user for input
		item= input('Player '+str(turn)+ ' enter your guess: ').lower()

		#check if input is an ans in the ans key [and so we can proceed to capitalizing letters], or if it has been guessed already/ is not a possible ans[so it can skip turns]
		if item in answer_key and not item in guess:
			#add right guess in guess list
			guess.append(item)
			#increase score by 1 for respective player and add guess to that players guess list
			scores[turn]+= 1
			append_item='"'+item+'"'+','
			player_guess_list[turn]+=append_item
			
			
			#set found variable as false, and Word_Found as False as well.
			#Found is used to see if the word is found in a certain direcion around a letter, once whole word is found, we exit loop and go on to capitalizing it 
			#word_found is used break whole while loop once the complete word is found and capitalized 	

			Found=False
			Word_Found=False

			while Word_Found==False:

				for row in range(NUM_ROWS):
					for col in range(NUM_COLS):


						#look for first letter as starting point 
						if board[row][col]==item[0].lower() or board[row][col]==item[0].upper():

						#look for second letter of word in 8 directions and if found, look for rest of leters in same direction, if whole word is found, set variale found=True 
						#if, found is true, capitalize letters in direcion and then break from loop.
						#try except added to make sure code works if index goes out of range is >6, it will break loop and go to next loop.

							try:
								if board[row][col+1]==item[1].lower() or board[row][col+1]==item[1].upper():									
									col_change=col	
									for letter in item:
											if board[row][col_change]==letter.lower() or board[row][col_change]==letter.upper():		
												Found=True
												col_change=col_change+1
											else:
												Found=False
												break
									
									if Found==True:
										col_change=col
										for index in range(len(item)):
											board[row][col_change]=board[row][col_change].upper()
											col_change=col_change+1
										Word_Found=True
										break

							except IndexError:
								print()

							try:
								if board[row][col-1]==item[1].lower() or board[row][col-1]==item[1].upper():
									
									if col-1>=0:
										
										col_change=col
										for letter in item:

											if board[row][col_change]==letter.lower() or board[row][col_change]==letter.upper():	
												Found=True
												col_change=col_change-1
											else:
												Found=False
												break	
																

										if Found==True:
											col_change=col
											for index in range(len(item)):
												board[row][col_change]=board[row][col_change].upper()
												col_change=col_change-1
											Word_Found=True
											break

							except IndexError:
								print()

							try:
								if board[row-1][col]==item[1].lower() or board[row-1][col]==item[1].upper():
									
									if row-1>=0:
										row_change=row
										for letter in item:
											if board[row_change][col]==letter.lower() or board[row_change][col]==letter.upper():	
												Found=True
												row_change=row_change-1
											else:
												Found=False
												break
											
										if Found==True:
											row_change=row
											for index in range(len(item)):
												board[row_change][col]=board[row_change][col].upper()
												row_change=row_change-1
											Word_Found=True
											break


							except IndexError:
								print()

							try:
								if board[row+1][col]==item[1].lower() or board[row+1][col]==item[1].upper():
									row_change=row
									
									for letter in item:
										if board[row_change][col]==letter.lower() or board[row_change][col]==letter.upper():	
											Found=True
											row_change=row_change+1

										else:
											Found=False
											break	
										
									if Found==True:
										row_change=row
										for index in range(len(item)):
											board[row_change][col]=board[row_change][col].upper()
											row_change=row_change+1

										Word_Found=True
										break

							except IndexError:
								print()

							try:
								if board[row+1][col+1]==item[1].lower() or board[row+1][col+1]==item[1].upper():
									row_change=row
									col_change=col
									
									for letter in item:
										if board[row_change][col_change]==letter.lower() or board[row_change][col_change]==letter.upper():	
											Found=True
											row_change=row_change+1
											col_change=col_change+1
										else:
											Found=False
											break	
										
									if Found==True:
										row_change=row
										col_change=col
										for index in range(len(item)):
											board[row_change][col_change]=board[row_change][col_change].upper()
											row_change=row_change+1
											col_change=col_change+1
										Word_Found=True
										break
			
							except IndexError:
								print()

							try:
								if board[row-1][col-1]==item[1].lower() or board[row-1][col-1]==item[1].upper():
									if col-1>=0 and row-1>=0:
										row_change=row
										col_change=col
										
										for letter in item:
											if board[row_change][col_change]==letter.lower() or board[row_change][col_change]==letter.upper():	
												Found=True
												row_change=row_change-1
												col_change=col_change-1
											else:
												Found=False
												break	
																		
				
										if Found==True:
											row_change=row
											col_change=col
											for index in range(len(item)):
												board[row_change][col_change]=board[row_change][col_change].upper()
												row_change=row_change-1
												col_change=col_change-1
											Word_Found=True
											break

							except IndexError:	
								print()

							try:
								if board[row-1][col+1]==item[1].lower() or board[row-1][col+1]==item[1].upper():
									if row-1>=0:
										row_change=row
										col_change=col
										
										for letter in item:
											if board[row_change][col_change]==letter.lower() or board[row_change][col_change]==letter.upper():	
												Found=True
												row_change=row_change-1
												col_change=col_change+1

											else:
												Found=False
												break	
																		
				
										if Found==True:
											row_change=row
											col_change=col
											for index in range(len(item)):
												board[row_change][col_change]=board[row_change][col_change].upper()
												row_change=row_change-1
												col_change=col_change+1
											Word_Found=True
											break

							except IndexError:
								print()

							try:
								if board[row+1][col-1]==item[1].lower() or board[row+1][col-1]==item[1].upper():
									if col-1>=0:
										row_change=row
										col_change=col
										
										for letter in item:
											if board[row_change][col_change]==letter.lower() or board[row_change][col_change]==letter.upper():	
												Found=True
												row_change=row_change+1
												col_change=col_change-1
											else:
												Found=False
												break
				
										if Found==True:
											row_change=row
											col_change=col
											for index in range(len(item)):
												board[row_change][col_change]=board[row_change][col_change].upper()
												row_change=row_change+1
												col_change=col_change-1
											Word_Found=True
											break

							except IndexError:
								print()
			

			#clear old board and print new
			os.system("clear")
			print_board()					

		elif item not in answer_key:
			print('Your guess is not a part of the board, wait for your next turn.'+'\n')

		elif item in guess:
			print('Word has already been guessed. Try again later.'+'\n')

		print('')
		for Player1 in list_players:
		
			print('Player '+ str(Player1) + ': '+ str(scores[Player1])+' ['+str(player_guess_list[Player1])+']'+'\n')



#set max  value in scores as winner then print winning statement


Winner = max(scores, key=scores.get)
print('Player '+str(Winner)+' WON!')



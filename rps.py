"""In game user inputs either rock, paper, or scissor, the bots goal is to beat you the majority of the time and  the person goal is to beat you the majority of the time. For
simplicity sake, the game with be the best out of 5 to allow the bot more data to play the player. This file simply will execute rock paper scissor with bot choosing at random
but future files will provide the bot with playing strats.
"""
import random
outcomes=open('outcomes.txt','a')


choicebank=[]
def play_rps(round=0,p1_rounds=0,p2_rounds=0):
	print(choicebank)
	score=[p1_rounds,p2_rounds]
	if p1_rounds==3 or p2_rounds==3:
		if max(p1_rounds,p2_rounds)==p1_rounds:
			print(f'Humans live to fight another day.\n SCORE:{score}')
			return None
		else:
			print(f'GAME OVER!!!\n\n\nTHE ROBOTS ARE COMING!!! \n SCORE:{score}')
			return None
	rps=['ROCK','PAPER','SCISSOR']
	print(f'SCORE: \n PLAYER1: {p1_rounds} vs BOT:{p2_rounds}')
	print('\n')
	player1_choice=input('What is your move human?\n').upper()
	choicebank.append(player1_choice)
	if player1_choice not in rps:
		print(f'{player1_choice} is not a valid move. Please type one of the following options {rps}')
		play_rps(rounds,p1_rounds,p2_rounds)
	player2_choice=random.choice(rps)
	print('\n\n')
	outcomes.write(f'{player1_choice},{player2_choice}\n')
	if player1_choice==player2_choice:
		print(f"Great minds think alike! You both picked {player1_choice}!")
		play_rps(round,p1_rounds,p2_rounds)
	else:
		if player1_choice=='ROCK' and player2_choice=='SCISSOR':
			print("ROCK BEATS SCISSOR!")
			return play_rps(round+1,p1_rounds+1,p2_rounds)
		elif player1_choice=='PAPER' and player2_choice=='ROCK':
			print("PAPER BEATS ROCK!")
			return play_rps(round+1,p1_rounds+1,p2_rounds)
		elif player1_choice=='SCISSOR' and player2_choice=='PAPER':
			print("SCISSORS BEATS PAPER!")
			return play_rps(round+1,p1_rounds+1,p2_rounds)
		if player2_choice=='ROCK' and player1_choice=='SCISSOR':
			print("ROCK BEATS SCISSOR!")
			return play_rps(round+1,p1_rounds,p2_rounds+1)
		elif player2_choice=='PAPER' and player1_choice=='ROCK':
			print("PAPER BEATS ROCK!")
			return play_rps(round+1,p1_rounds,p2_rounds+1)
		elif player2_choice=='SCISSOR' and player1_choice=='PAPER':
			print("SCISSORS BEATS PAPER!")
			return play_rps(round+1,p1_rounds,p2_rounds+1)
play_rps()
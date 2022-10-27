#take in choice bank and predicts move and returns either rock paper or scissor
"""it turns out that the most common throw is rock (35 percent), scissors (35 percent), and then paper (29.6 percent). Not sure what to do next? Picking paper may give you a very slight advantage.Apr 26, 2015"""
import random
with open('outcomes.txt',r) as o:
	o.readlines()

def pick(choicebank,botchoices):
	rps=['ROCK','PAPER','SCISSOR']
	if choicebank==[]:
		return "PAPER"
	else:
		random_option=random.choice(rps)
		uno_reverse=choicebank[-1]
		runitback=botchoices[-1]


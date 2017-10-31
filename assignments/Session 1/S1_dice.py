##
# @author : Francony Steven
# @brief : A simple dice game with one player and a computer
##

import random

playerPts = 0
computerPts = 0

playersTurn = False
wantsToStop = 0

while playerPts < 100 and computerPts < 100 :

	playersTurn = not playersTurn
	wantsToStop = 0
	diceValue = -1
	turnScore = 0

	if playersTurn:

		print "\n*** Player ***"

		while wantsToStop == 0 and diceValue != 1:
			diceValue = random.randint(1, 6)
			print "\nDice value : " + str(diceValue)

			if diceValue != 1:
				turnScore += diceValue
				print "Your score : " + str(playerPts + turnScore)
				wantsToStop = input("\nDo you want stop (0 : no ; 1 : yes) ? ")
				
				if wantsToStop == 1:
					playerPts += turnScore
			
			else:
				print "\nYou lost " + str(turnScore) + " points"
				print "Your current score : " + str(playerPts)

	else:
		
		print "\n*** Computer ***"
		
		while wantsToStop == 0 and diceValue != 1:
			diceValue = random.randint(1, 6)
			print "\nDice value : " + str(diceValue)

			if diceValue != 1:
				turnScore += diceValue
				print "Computer score : " + str(computerPts + turnScore)
				wantsToStop = random.randint(0, 1)

				if wantsToStop == 1:
					print "\nComputer stop...\n"
					computerPts += turnScore
				
				else:
					print "\nComputer continue...\n"
			else:
				print "\nComputer lost " + str(turnScore) + " points"
				print "Computer current score : " + str(computerPts)


print "Final score | YOU : " + str(playerPts) + " COMPUTER : " + str(computerPts)

if playersTurn:
	print "You win"
else :
	print "The computer wins"
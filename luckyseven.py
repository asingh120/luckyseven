'''
Program: luckyseven.py
Author: Amit
Date: 9/13/19

Program asks player to enter how much money they want in a pot and then rolls
dice. If dice total equals 7, player wins and is awarded $4.  If player loses, they 
lose $1.  Player can exit program at any time and is then told how many times they 
played and the maximum amount that was held in the pot.
'''

import random

pot = int(input("How much money do you want in the pot? >>> "))
maxPot = 0

# Accumulator for rolls
count = 0

while True:	
	count += 1

	# Game mechanics for die
	die1 = random.randint(1, 6)
	die2 = random.randint(1, 6)
	dieSum = (die1 + die2)

	if dieSum == 7:
		pot = pot + 4
		print("You rolled a(n) "  + str(dieSum))
		print("You win! Your pot is now " + str(pot))
	else:
		pot = pot - 1
		print("You rolled a(n) " + str(dieSum))
		print("You lose! Your pot is now " + str(pot))

	if pot > maxPot:
		maxPot = pot	

	if pot == 0:
		print()
		print("You played a total of ", count, "times")
		print("The maximum held in the pot was ", str(maxPot))
		print("You lost it all sucka! Thank you for playing!")
		
	cont = input("Would you like to play again? YES to continue >> ")
	cont = cont.upper()	

	if cont != "YES":
		break

# Final output message to player
print()
print("You played a total of ", count, "times")
print("The maximum held in the pot was ", str(maxPot))
print("Thank you for playing!")
print()

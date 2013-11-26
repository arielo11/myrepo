from sys import exit

def start_room():
	print "You find yourself in a small room with three doors."
	print "One to the left, one to the right, and one in the middle."
	print "Which do you go through?"
	
	next = raw_input ("> ")
	if "left" in next:
		dead("The door was rigged with explosives! You explode into a million pieces.")
		
	elif "right" in next:
		hallway()
		
	elif "middle" in next:
		harem()
		
	else:
		dead("You cant make up your mind, and wander around until you die of starvation.")
		

def dead(why):
	print why
	exit(0)
	
def harem():
	print "You enter a room with several gorgeous and seductive women."
	print "They signal for you to come join them, but you also spot a door on the left."
	print "What do you do? Join the women, or go through the door?"
	
	next = raw_input ("> ")
	
	if "door" in next:
		loot_room()
	
	elif "join the women" in next:
		dead("You lie down with the seductive women - who then turn out to be succubus' who proceed to eat you alive.")
		
	else:
		harem()
		
def hallway():
	print "You go through what seems to be an endless hallway."
	print "At the end there is a big iron door."
	print "Do you open it, or go back?"
	
	next = raw_input("> ")
	
	if "open" in next:
		loot_room()
		
	elif "go back" in next:
		start_room()
		
	else:
		dead("You cant make up your mind, and wander around until you die of starvation.")
		
def loot_room():
	print "It seems you hit the jackpot! The room is filled with gold!"
	print "Congratulations! You win the game!."
	exit(0)
	
start_room()
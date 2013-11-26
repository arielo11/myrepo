from sys import exit
from random import randint
from ex45_two import Scene


class GameEngine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
		
        while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			

class Datefail(Scene):

	failreason = [
		"Well that was stupid. You'll never get a girl!",
		"Hahahah... You really thought that would work?",
		"NOPE! She looks at you in disgust and leaves."
		]

	def enter(self):
		print Datefail.failreason[randint(0, len(self.failreason)-1)]
		print "No hot date for you! Try one of the other babes perhaps?"
		

		
class Entrance(Scene):
	def enter(self):
		print "You find yourself in the entrance of a bar. You're feeling lucky"
		print "tonight, and spot three potential hot babes."
		print "First, there is the brunette by the bar."
		print "Second, there is a hot blonde sitting at a table."
		print "Third, there's a woman with a large drink sitting in the far back."
		print "\n"
		print "Which do you choose to go for first? (Or leave?)"
		
		choice = raw_input("> ")
		
		if choice == "first":
			return 'brunette'
			
		elif choice == "second":
			return 'blonde'
			
		elif choice == "third":
			return 'soccermom'
			
		elif choice == "leave":
			exit(1)
			
		else:
			print "Invalid choice!"
			return 'entrance'
			
class Reentry(Scene):
	def enter(self):
		print "You are back at the entrance. Which babe will be your next target?"
		print "First, there is the brunette by the bar."
		print "Second, there is a hot blonde sitting at a table."
		print "Third, there's a woman with a large drink sitting in the far back."
		print "\n"
		print "Which do you choose to go for? (Or leave?)"
		
		choice = raw_input("> ")
		
		if choice == "first":
			return 'brunette'
			
		elif choice == "second":
			return 'blonde'
			
		elif choice == "third":
			return 'soccermom'
			
		elif choice == "leave":
			exit(1)
			
		else:
			print "Invalid choice!"
			return 'reentry'
		

class Brunette(Scene):

    def enter(self):
		print "You approach a gorgeous brunette that's standing alone"
		print "in front of the bar. You concider your options on how"
		print "to approach, and go through your options in your head."
		print "\n"
		print "Option 1: Approach from behind, slap her on the butt,"
		print "and open with 'Damn you're a fine specimen of the human race!'"
		print "\n"
		print "Option 2: Approach her, stop and smile, before saying"
		print "Good evening. May I join the beautiful lady?"
		print "\n"
		print "Which option do you choose?"
		
		choice = raw_input("[Option #]> ")
		
		if choice == "1":
			print "That's no way to treat a lady!"
			return 'datefail'
			print "\n"
			print "\n"
			return 'reentry'
			
		elif choice == "2":
			print "Success!"
			print "After talking a while, the gorgeous brunette decides"
			print "to go home with you - of course only to play boardgames"
			print "and bake cookies! This is a PG13 game after all."
			exit(1)
			
		else:
			print "That's not a valid option!"
			return 'brunette'

class Blonde(Scene):

    def enter(self):
		print "You approach a blonde girl at a lone table."
		print "As you draw nearer to the table, she focuses on you."
		print "As you arrive, she pops a bubble with her chewing-gum, before"
		print "saying 'what's happenin' cutie-pie?'"
		print "\n"
		print "You think about your memorized pickup-lines, and can only think of"
		print "two that would maybe work on this girl."
		print "\n"
		print "Option 1: Go right over to her, lift her up from her chair"
		print "and start wildly making out with her."
		print "\n"
		print "Option 2: Rip your shirt off and flex, before you proceed to ask"
		print "'Do you want some of this baby? DO YOU? I've got a car ready to"
		print "take you to my bedroom RIGHT NOW."
		
		success = randint(1,2)
		option = raw_input("[Option #]> ")
		
		if int(option) != success:
			return 'datefail'
			print "\n"
			print "\n"
			return 'reentry'
			
		else:
			print "Thats my boy! She immediately responds to your amazing pickup-method"
			print "and says 'TAKE ME HOME HONEY!'"
			exit(1)

class Soccermom(Scene):

    def enter(self):
		print "You approach the woman in the back of the bar."
		print "As you get closer, you see clearly that this is a"
		print "real 'MILF'(Dont google that, kids!)."
		print "\n"
		print "Before you even get to her table, she smirks, before she says"
		print "'I know what you're after, son. If you guess what number I'm"
		print "thinking of right now, between 1 and 10, I'll rock your world."
		print "Guess wrong, and you can f*** off."
		
		question = randint(1,10)
		guess = raw_input("[I guess #]> ")
		
		if int(guess) != question:
			print "Sorry son, thats the wrong answer!"
			print "Now f*** off..."
			return 'reentry'
			
		else:
			print "Wow, you actually guessed correct..."
			print "Allright, where's your car? Let's get the fun started!"
			exit(1)

class Map(object):

	scenes = {
		'brunette': Brunette(),
		'blonde': Blonde(),
		'soccermom': Soccermom(),
		'entrance': Entrance(),
		'datefail': Datefail(),
		'reentry': Reentry()
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('entrance')
a_game = GameEngine(a_map)
a_game.play()
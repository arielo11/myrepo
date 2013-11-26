class Friend(object):
	def write(self):
		print "FRIEND is being printed()"
		
	def writeagain(self):
		print "FRIEND is being printed AGAIN!()"
		
		
class Me(object):
	def __init__(self):
		self.friend = Friend()
		
	def test(self):
		self.friend.writeagain()
		
	def me_boss(self):
		print "Now I'M being printed!()"
		
		
Ariel = Me()

Ariel.test()
Ariel.me_boss()
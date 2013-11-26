name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
test = 'Test-text'
test2 = 'Double-test-text'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try ti get it exactly right.
print "If I add %d, %d, and %d I get %d." % (age, height, weight, 
age + height + weight)

print "This is a test - %s." % test
print "This is also a test - %r." % test2
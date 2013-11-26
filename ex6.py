# Below are four lines with variables. The y line uses the binary and do_not
# variables in its result.
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#The two lines below print out the x and y variables above.
print x
print y

# The two lines below print "I said:" and then follows by executing a
# %r and %s , which contain the x and y variables, making them print the
# text in those two variables again.
print "I said: %r." % x
print "I also said: '%s'." % y

# Below are two new variables. The second one contains the "False" of 
# the first one, through %r.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This one prints the two above.
print joke_evaluation % hilarious

# Below are two new variables.
w = "This is the left side of..."
e = "a string with a right side."

# The line below prints the two above variables after one another.
# The plus (+) makes it print both as 1 line.
print w + e
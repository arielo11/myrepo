from sys import argv

script, filename = argv
# The above two lines are used so we can specify the filename running a script.

txt = open(filename)
# The above line specifies to open the given (filename).

print "Here is your file %r:" % filename
print txt.read()
# Above, we command the txt file/variable to perfom the action "read", printing its text.

print "Type the filename again:"
file_again = raw_input("> ")
# Here we input the filename again, as a prompt by raw_input.

txt_again = open(file_again)
# Above, the variable txt_again opens the given filename.

print txt_again.read()
# And again, the txt_again file/variable is asked to perform the "read" action.

txt.close()
txt_again.close()
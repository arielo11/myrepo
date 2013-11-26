from sys import argv

script, filename = argv

file2 = open(filename)

print file2.read()

file2.close()

# And below is the other way.

print "Please enter the name of the file"
file = raw_input("> ")

txt = open(file)

print txt.read()

txt.close()
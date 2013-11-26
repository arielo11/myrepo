from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()

# Opens the file you selected.
current_file = open(input_file)

print "First let's print the whole file:\n"
# Prints all the content.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# rewind is a method to seek. Seek sets the files current position at the offset.
rewind(current_file)

print "Let's print three lines:"

# Below current line is defined as 1, and gets +1 for each line.
# print_a_line uses current_line as line_count, and then prints the given line.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
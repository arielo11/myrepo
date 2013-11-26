i = 0
numbers = []
y = 6

print "Press 1 to start."

start = raw_input ("> ")

if start == "1":
	while i < y:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now ", numbers
		print "At the bottom i is %d" % i
	
	print "The number: "

	for num in numbers:
		print num
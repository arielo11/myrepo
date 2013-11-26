def fans(fanboys, fangirls):
	print "You have %d fanboys!" % fanboys
	print "You have %d fangirls!" % fangirls
	print "Holy bejeezus!"
	
	
print "Giving them numbers directly:"
fans(101, 73)

print "Using variables:"
var_fanboys = 50
var_fangirls = 178

fans(var_fanboys, var_fangirls)

print "Or, with math:"
fans(73 + 7, 80 + 2)

print "Or both!"
fans(var_fanboys + 50, var_fangirls + 100)
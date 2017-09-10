def answer(start, length):
	c=0
	num=start
	add=0
	workers=length
	while workers > 0:
		num = num+add
		for i in range(workers):
			#print "NUM:",num
			c=c^num
			num=num+1
		num = num - 1
		#print "ADD:",add
		add = add +1
		workers = workers-1

	return c

print answer(0,3)
print answer(17, 4)
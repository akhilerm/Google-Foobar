"""If someone reads this, the code works for all test cases except 3&4. Please look into it"""
class Point(object):
	
	def __init__(self, x, y, z, dist):
		self.x=x
		self.y=y
		self.z=z
		self.dist=dist

	def __str__(self):
		return "(%s,%s,%s,%s)"%(self.x,self.y,self.z,self.dist)
		
class Queue(object):
	
	def __init__(self):
		self.queue = []

	def enq(self, e):
		self.queue.append(e)

	def deq(self):
		return self.queue.pop(0)

	def isEmpty(self):
		if len(self.queue) == 0:
			return True
		else:
			return False

def answer(n):
	if len(n) == 1 and len(n[0]) == 1:
		return 2
	processed = [[False for y in range(len(n[0]))] for x in range(len(n))]
	sp = 5000
	q=Queue()
	processed[0][0] = True
	q.enq(Point(0,0,0,1))
	while q.isEmpty() == False:
		node = q.deq()
		x = node.x
		y=node.y
		z=node.z
		dist=node.dist
		if x == len(n)-1 and y == len(n[0])-1:
			sp = dist

		if safe(x,y-1,z,processed,n) == True:
			processed[x][y-1] = True
			if z == 1:
				q.enq(Point(x,y-1,z+1,dist+1))
			else:
				q.enq(Point(x,y-1,z,dist+1))

		if safe(x,y+1,z,processed,n) == True:
			processed[x][y+1] = True
			if z == 1:
				q.enq(Point(x,y+1,z+1,dist+1))
			else:
				q.enq(Point(x,y+1,z,dist+1))

		if safe(x-1,y,z,processed,n) == True:
			processed[x-1][y] = True
			if z == 1:
				q.enq(Point(x-1,y,z+1,dist+1))
			else:
				q.enq(Point(x-1,y,z,dist+1))

		if safe(x+1,y,z,processed,n) == True:
			processed[x+1][y] = True
			if z == 1:
				q.enq(Point(x+1,y,z+1,dist+1))
			else:
				q.enq(Point(x+1,y,z,dist+1))

		

	return sp

def safe(x,y,z,processed,n):
	global size
	if x >= 0 and y >=0 and x<len(n) and y<len(n[0]) and processed[x][y] == False:
		if n[x][y] == 0:
			return True
		elif z < 1:
			return True
	return False

print answer([[0, 0, 0, 0, 0, 0],
			  [1, 1, 1, 1, 1, 0],
			  [0, 0, 0, 0, 0, 0], 
			  [0, 1, 1, 1, 1, 1], 
			  [0, 1, 1, 1, 1, 1], 
			  [0, 0, 0, 0, 0, 0]])

print answer([[0, 1, 1, 0], 
			  [0, 0, 0, 1], 
			  [1, 1, 0, 0], 
			  [1, 1, 1, 0]])

print answer([[0, 0, 1, 1, 0],
			  [0, 1, 1, 1, 0],
			  [0, 1, 0, 0, 0],
			  [0, 0, 0, 1, 0],
              [1, 0, 0, 1, 0]])

print answer([[0,1],
			  [1,0]])

print answer([
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

print answer([[0]])

print answer([
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

print answer([[0,0,0,0,0,0,0,0,1],
			  [1,0,0,0,0,0,0,0,0]])
def answer(n):
	if len(n) == 1 and len(n[0]) == 1 and n[0][0] == 0:
		return [1, 1]
	A = [[Fraction(n[x][y]) for y in range(len(n))] for x in range(len(n))]
	for x in range(len(n)):
		for y in range(len(n)):
			if sum(n[x]) != 0:
				A[x][y] = A[x][y]*Fraction(1, sum(n[x]))

	I = I_matrix(len(n))

	W = [[I[x][y] - A[x][y] for y in range(len(n))] for x in range(len(n))]

	V = invert(W)

	result_t = []
	for x in range(len(n)):
		if all(val == 0 for val in n[x]):
			result_t.append(V[0][x])

	lcm = result_t[0].denominator
	for x in result_t:
		lcm = lcm*x.denominator/gcd(lcm, x.denominator)

	final = []
	for x in result_t:
		final.append(x.numerator*lcm/x.denominator)
	final.append(lcm)

	return final

def invert(X):
    rows = len(X)
    cols = len(X[0])

    identity = I_matrix(rows)
    for i in range(0,rows):
        X[i]+=identity[i]

    i = 0
    for j in range(0,cols):
        
        zero, non_zero = check(X,i,j)
        
        if zero == 0:
            if j == cols:
                return X
        
        if non_zero != i:
            X = swap(X, i, non_zero)
        
        X[i] = [m*Fraction(X[i][j].denominator,X[i][j].numerator) for m in X[i]]

        for q in range(0,rows):
            if q!=i:
                new_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - new_row[m] for m in range(0,len(new_row))]
        if i==rows or j==cols:
            break
        i+=1

    for i in range(0,rows):
        X[i] = X[i][cols:len(X[i])]

    return X

def check(X, i, j):
    non_zeros = []
    first_non_zero = -1
    for m in range(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero

def swap(X, i, p):
    X[p], X[i] = X[i], X[p]
    return X

def I_matrix(size):
    identity = [[Fraction(0) for y in range(size)] for x in range(size)]
    for x in range(size):
    	for y in range(size):
    		if x == y:
    			identity[x][y] = Fraction(1)
    return identity

class Fraction(object):

	def __init__(self, numerator, denominator = 1):
		g = gcd(numerator, denominator)
		self.numerator = numerator / g
		self.denominator = denominator / g

	def __mul__(self, other):
		if isinstance(other, int): 
			other = Fraction(other)
		return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
	
	__rmul__ = __mul__

	def __add__(self, other): 
		if isinstance(other, int): 
			other = Fraction(other) 
		return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator) 

	__radd__ = __add__ 

	def __sub__(self, other):
		return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

def gcd(m, n):
	if m % n == 0: 
		return n 
  	else: 
		return gcd(n, m%n)		

print answer([
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
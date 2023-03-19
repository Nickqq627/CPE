def gcd(x,y):
	while y>0:
		z=x%y
		x=y
		y=z
	return x
table=[[0 for i in range(502)] for i in range(502)]
for i in range(502):
	for j in range(502):
		table[i][j]=gcd(i,j)
while 1:
	try:
		n=int(input())
		g=0
		if n==0:
			break
		for i in range(1,n):
			for j in range(i+1,n+1):
				g+=table[i][j]
		print(g)
	except:
		break

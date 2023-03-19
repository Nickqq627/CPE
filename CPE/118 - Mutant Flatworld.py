x,y=map(int, input().split())
lost=[]
while 1:
	try:
		a,b,p=input().split()
		a=int(a)
		b=int(b)
		arr=list(input())
		c=0
		for i in arr:
			if i=='R':
				if p=='N':
					p='E'
				elif p=='S':
					p='W'
				elif p=='E':
					p='S'
				elif p=='W':
					p='N'
			elif i=='L':
				if p=='N':
					p='W'
				elif p=='S':
					p='E'
				elif p=='E':
					p='N'
				elif p=='W':
					p='S'
			elif i=='F':
				if p=='N':
					if [a,b+1] not in lost:
						b=b+1
						if b>y:
							lost.append([a,b])
							b=b-1
							c=1
							break
				elif p=='S':
					if [a,b-1] not in lost:
						b=b-1
						if b<0:
							lost.append([a,b])
							b=b+1
							c=1
							break
				elif p=='E':
					if [a+1,b] not in lost:
						a=a+1
						if a>x:
							lost.append([a,b])
							a=a-1
							c=1
							break
				elif p=='W':
					if [a-1,b] not in lost:
						a=a-1
						if a<0:
							lost.append([a,b])
							a=a+1
							c=1
							break
		if c==1:
			print(a,b,p,'LOST')
		else:
			print(a,b,p)
	except:
		break			
	
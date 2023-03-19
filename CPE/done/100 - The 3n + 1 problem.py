while 1:
	try:
		x,y=map(int, input().split())
		a=min(x,y)
		b=max(x,y)
		m=0
		for i in range(a,b+1):
			count=0
			while i!=1:
				if i%2==1:
					i=3*i+1
				else:
					i=i/2
				count+=1
				if count>m:
					m=count
		print(x,y,m+1)
	except:
		break
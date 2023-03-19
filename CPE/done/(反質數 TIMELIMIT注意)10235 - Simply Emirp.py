while 1:
	try:
		a=input()
		b=a[::-1]
		a=int(a)
		b=int(b)
		count=0
		for i in range(1,a+1):
			if a%i==0:
				count+=1
			if count>2:
				break
		if count>2:
			print(str(a)+' is not prime.')
		elif a==b:
			print(str(a)+' is prime.')
		else:
			for j in range(1,b+1):
				if b%j==0:
					count+=1
				if count>4:
					break
			if count>4:
				print(str(a)+' is prime.')
			else:
				print(str(a)+' is emirp.')
	except:
		break
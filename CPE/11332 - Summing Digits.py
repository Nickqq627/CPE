while 1:
	try:
		a=str(input())
		if a=='0':
			break
		while int(a)>=10:
			count=0
			for i in range(len(a)):
				count+=int(a[i])
			a=str(count)
		print(a)
			
	except:
		break
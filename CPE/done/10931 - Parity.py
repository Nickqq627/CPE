while 1:
	try:
		a=int(input())
		if a==0:
			break
		b=str(bin(a))
		count=0
		for i in b:
			if i=='1':
				count+=1
		print('The parity of '+str(b[2:])+' is '+str(count)+' (mod 2).')
	except:
		break
while 1:
	try:
		a=input()
		x=a
		if a=='0':
			break
		count=0
		if int(a)%9!=0:
			print(a+' is not a multiple of 9.')
		elif a=='9':
			print('9 is a multiple of 9 and has 9-degree 1.')
		else:
			while int(a)>10:
				sum=0
				for i in str(a):
					sum+=int(i)
				count+=1
				a=sum
			print(str(x)+' is a multiple of 9 and has 9-degree '+str(count)+'.')
				
	except:
		break
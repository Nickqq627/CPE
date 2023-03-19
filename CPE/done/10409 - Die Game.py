while 1:
	try:	
		T=input()
		if T=='0':
			break
		die=[1,6,3,4,2,5]
		for t in range(int(T)):
			a=input()
			if a=='north':
				tmp=die[0]
				die[0]=die[5]
				die[5]=die[1]
				die[1]=die[4]
				die[4]=tmp
			elif a=='south':
				tmp=die[0]
				die[0]=die[4]
				die[4]=die[1]
				die[1]=die[5]
				die[5]=tmp
			elif a=='east':
				tmp=die[0]
				die[0]=die[2]
				die[2]=die[1]
				die[1]=die[3]
				die[3]=tmp
			else:
				tmp=die[0]
				die[0]=die[3]
				die[3]=die[1]
				die[1]=die[2]
				die[2]=tmp
		print(die[0])
	except:
		break
		
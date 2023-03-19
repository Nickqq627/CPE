for i in range(100):
	a=input()
	if int(a)==0:
		break
	if int(a)%11==0:
		print(str(a) + " is a multiple of 11.")
	else:
		print(str(a) + " is not a multiple of 11.")

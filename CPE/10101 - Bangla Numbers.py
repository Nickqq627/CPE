def ban(a):
	if a>=10000000:
		ban(a//10000000)
		print(' kuti',end="")
		a=a%10000000
	if a>=100000:
		print(' '+str(a//100000),end="")
		print(' lakh',end="")
		a=a%100000
	if a>=1000:
		print(' '+str(a//1000),end="")
		print(' hajar',end="")
		a=a%1000
	if a>=100:
		print(' '+str(a//100),end="")
		print(' shata',end="")
		a=a%100
	if a>0:
		print(' '+str(a),end="")
c=1
while 1:
	try:
		a=int(input())
		if c<10:
			print('   '+str(c)+'.',end="")
		else:
			print('  '+str(c)+'.',end="")
		c=c+1
		
		if a==0:
			print(' 0',end="")
		else:
			ban(a)
		print()
	except:
		break
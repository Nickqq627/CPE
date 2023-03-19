T=input()
for t in range(int(T)):
	a=int(input(),2)
	b=int(input(),2)
	while b>0:
		z=a%b
		a=b
		b=z
	if a>1:
		print('Pair #'+str(t+1)+': All you need is love!')
	else:
		print('Pair #'+str(t+1)+': Love is not all you need!')
	
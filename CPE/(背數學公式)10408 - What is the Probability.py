T=input()
for t in range(int(T)):
	m,p,k=map(float, input().split())
	q=1-p
	if 1-(q**m)==0:
		print('0.0000')
	else:
		ans=(q**(k-1))*p/(1-(q**m))
		print('{:.4f}'.format(ans))
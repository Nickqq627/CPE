T=input()
for i in range(int(T)):
	a=int(input())
	b=int(input())
	ans=0
	for j in range(a,b+1):
		if j%2==1:
			ans=ans+j
	print('Case ' + str(i+1) + ': ' + str(ans))
	
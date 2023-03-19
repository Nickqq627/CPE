fib=[2,1]
for i in range(40):
	fib.insert(0,fib[0]+fib[1])
T=input()
for t in range(int(T)):
	a=int(input())
	x=a
	arr=[]
	ans=''
	for i in fib:
		if a>=i:
			a=a-i
			arr.append(1)
		else:
			arr.append(0)
	for i in arr:
		ans+=str(i)
	print(str(x)+' = '+str(int(ans))+' (fib)')
		
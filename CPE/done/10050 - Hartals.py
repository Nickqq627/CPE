T=input()
for t in range(int(T)):
	day=int(input())
	TT=input()
	arr=[]
	ans=[]
	for tt in range(int(TT)):
		arr.append(int(input()))
	for i in range(day):
		ans.append(0)
		for j in arr:
			if (i+1)%j==0 and (i+1)%7!=6 and (i+1)%7!=0:
				ans[i]=1
				break
	count=0
	for i in ans:
		if i==1:
			count+=1
	print(count)
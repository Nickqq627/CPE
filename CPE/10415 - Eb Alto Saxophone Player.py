fin=[[0,1,1,1,0,0,1,1,1,1]
	,[0,1,1,1,0,0,1,1,1,0]
	,[0,1,1,1,0,0,1,1,0,0]
	,[0,1,1,1,0,0,1,0,0,0]
	,[0,1,1,1,0,0,0,0,0,0]
	,[0,1,1,0,0,0,0,0,0,0]
	,[0,1,0,0,0,0,0,0,0,0]
	,[0,0,1,0,0,0,0,0,0,0]
	,[1,1,1,1,0,0,1,1,1,0]
	,[1,1,1,1,0,0,1,1,0,0]
	,[1,1,1,1,0,0,1,0,0,0]
	,[1,1,1,1,0,0,0,0,0,0]
	,[1,1,1,0,0,0,0,0,0,0]
	,[1,1,0,0,0,0,0,0,0,0]]
bu=['c','d','e','f','g','a','b','C','D','E','F','G','A','B']
T=input()
for t in range(int(T)):
	test=[[0,0,0,0,0,0,0,0,0,0]]
	ans=[0,0,0,0,0,0,0,0,0,0]
	a=list(input())
	for i in range(len(a)):
		test.append(fin[bu.index(a[i])])
	for i in range(1,len(test)):
		for j in range(10):
			if test[i][j]==1 and test[i-1][j]==0:	
				ans[j]+=1
	for i in range(len(ans)):
		if i==len(ans)-1:
			print(ans[i])
		else:
			print(ans[i],end=" ")
	
	
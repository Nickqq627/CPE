T=input()
dic={}
for t in range(int(T)):
	arr=input().split()
	a=arr[0]
	if a not in dic:
		dic[a]=1
	else:
		dic[a]+=1
ans=sorted(dic.items(),key=lambda x:x[1])
ans=sorted(ans,key=lambda x:x[0])
for x,y in ans:
	print('{} {}'.format(x,y))
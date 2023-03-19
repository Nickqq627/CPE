T=input()
space=input()
for t in range(int(T)):
	arr=[]
	count=0
	if t>0:
		print()
	while 1:
		try:
			a=input()
			if a=='':
				break
			else:
				arr.append(a)
				count+=1
		except:
			break
	
	dic={}
	for i in arr:
		if i not in dic:
			dic[i]=1
		else:
			dic[i]+=1
	ans=sorted(dic.items(),key=lambda x:x[1],reverse=True)
	ans=sorted(ans,key=lambda x:x[0])
	for x,y in ans:
		print('{} {:.4f}'.format(x,y/count*100))
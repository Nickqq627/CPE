c=0
while 1:
	try:
		arr=list(input())
		if c!=0:
			print()
		c=1
		dic={}
		for i in range(len(arr)):
			if ord(arr[i]) not in dic:
				dic[ord(arr[i])]=1
			else:
				dic[ord(arr[i])]+=1
		ans=sorted(dic.items(),key=lambda x:x[0],reverse=True)
		ans=sorted(ans,key=lambda x:x[1])
		for x,y in ans:
			print('{} {}'.format(x,y))
	except:
		break
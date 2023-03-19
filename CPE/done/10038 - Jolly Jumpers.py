while 1:
	try:
		arr=list(map(int, input().split()))
		a=arr[1:]
		ans=[]
		c=1
		for i in range(len(a)-1):
			ans.append(abs(a[i]-a[i+1]))
		ans=sorted(ans)
		for i in range(len(ans)):
			if (i+1)!=int(ans[i]):
				c=0
				break
		if c==1:
			print('Jolly')
		else:
			print('Not jolly')	
	except:
		break
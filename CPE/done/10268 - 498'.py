while 1:
	try:
		x=int(input())
		arr=list(map(int,input().split()))
		n=len(arr)-1
		ans=0
		for i in range(len(arr)-1):
			ans+=arr[i]*(n-i)*x**(n-1-i)
		print(ans)
	except:
		break
while 1:
	try:
		g,d=map(int, input().split())
		f=d*2+g**2-g
		ans=int(f**(1/2))
		if (ans*(ans+1))<f:
			ans+=1
		print(ans)
	except:
		break
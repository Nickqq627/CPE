while 1:
	try:
		a=list(input())
		b=list(input())
		a=sorted(a)
		ans=[]
		for i in a:
			if i in b and i!=' ':
				ans.append(i)
				b.remove(i)
		for i in range(len(ans)):
			print(ans[i],end="")
		print()
	except:
		break
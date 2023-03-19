while 1:
	try:
		a,b=map(int, input().split())
		if b==1:
			print('Boring!')
		else:
			ans=[]
			while a>1:
				ans.append(a)
				a=a/b
			c=0
			for i in ans:
				if i%b!=0:
					c=1
			if c==1:
				print('Boring!')
			else:
				ans.append(1)
				for i in range(len(ans)):
					if i==len(ans)-1:
						print(int(ans[i]))
					else:
						print(int(ans[i]),end=" ")
	except:
		break
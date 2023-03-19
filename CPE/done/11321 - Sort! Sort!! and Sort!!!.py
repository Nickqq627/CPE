while 1:
	try:
		arr=[]
		even=[]
		odd=[]
		ans=[]
		# 讀資料
		n,m=map(int,input().split())
		if n==m==0:
			print(0,0)
			break
		for i in range(n):
			arr.append(int(input()))
		# 分基偶	
		for i in range(n):
			if abs(arr[i]%2)==0:
				even.append(arr[i])
			else:
				odd.append(arr[i])
		# 排大小
		arr=sorted(odd,reverse=1)+sorted(even)
		# 分負數餘數
		for i in range(m-1,0,-1):
			for j in arr:
				if abs(j)%m==i and j<0:
					ans.append(j)
		# 分餘0
		for j in arr:
			if(j%m==0):
				ans.append(j)
		# 分正數餘數
		for i in range(1,m):
			for j in arr:
				if j%m==i and j>0:
					ans.append(j)
		# 印出答案
		print(n,m)
		for i in range(len(ans)):
			print(ans[i])					
	except:
		break
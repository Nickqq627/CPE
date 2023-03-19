T=input()
bug=0
for t in range(int(T)):
	if t>0:
		print()
	print('Case '+str(t+1)+':')
	arr=[]
	if bug==0:
		for i in range(4):
			arr+=(map(int, input().split()))
		TT=input()
	else:
		arr=bugarr
		TT=bugTT
	for tt in range(int(TT)):
		a=list(map(int, input().split()))
		if len(a)>1:
			bug=1
			bugarr=a[1:36]
			bugTT=a[37]
			tmp=a[0]
			a=[]
			a.append(tmp)
		a=a[0]
		x=a
		m=99999999999999
		ans=[]
		for i in range(2,37):
			a=x
			count=0
			while a>0:
				count+=arr[a%i]
				a=a//i
			if count<m:
				ans=[]
				ans.append(i)
				m=count
			elif count==m:
				ans.append(i)
		print('Cheapest base(s) for number '+str(x)+':',end="")
		for i in ans:
			print(' '+str(i),end="")
		print()

# T=input()
# bugl=[]
# bug=0
# for t in range(int(T)):
# 	if t!=0:
# 		print()
# 	cost=[]
# 	print('Case '+str(t+1)+':')
# 	if len(bugl)>1:
# 		cost=bugl
# 		test=bug
# 		bugl=[]
# 	else:
# 		for c in range(4):
# 			cost=cost+input().split()
# 		test=input()
# 	for test in range(int(test)):
# 		minx=999999999999999
# 		a=input().split('  ')
# 		if len(a)>1:
# 			bugl=a[1].split()
# 			bug=a[2]
# 		for i in range(2,37):
# 			total=0
# 			x=int(a[0])
# 			while x>0:
# 				total+=int(cost[x%i])
# 				x=x//i
# 			if total<minx:
# 				totallist=[]
# 				minx=total
# 				totallist.append(i)
# 			elif total==minx:
# 				totallist.append(i)
# 		print('Cheapest base(s) for number '+str(int(a[0]))+': ',end='')
# 		for p in range(len(totallist)):
# 			if p!=len(totallist)-1:
# 				print(totallist[p],end=' ')
# 			else:
# 				print(totallist[p])
			
# # T=input()
# # for t in range(int(T)):
# # 	if t!=0:
# # 		print()
# # 	cost=[]
# # 	print('Case '+str(t+1)+':')
# # 	for c in range(4):
# # 		cost=cost+input().split()
# # 	test=input()
# # 	for test in range(int(test)):
# # 		minx=999999999999999
# # 		a=input()
# # 		for i in range(2,37):
# # 			total=0
# # 			x=int(a)
# # 			while x>0:
# # 				total+=int(cost[x%i])
# # 				x=x//i
# # 			if total<minx:
# # 				totallist=[]
# # 				minx=total
# # 				totallist.append(i)
# # 			elif total==minx:
# # 				totallist.append(i)
# # 		print('Cheapest base(s) for number '+str(a)+': ',end='')
# # 		for p in range(len(totallist)):
# # 			if p!=len(totallist)-1:
# # 				print(totallist[p],end=' ')
# # 			else:
# # 				print(totallist[p])
			

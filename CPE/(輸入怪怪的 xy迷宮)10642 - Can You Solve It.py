def sol(x1,y1,x2,y2,count):
	while x1!=x2 or y1!=y2:
		if y1==0:
			y1=x1+1
			x1=0
		else:
			y1=y1-1
			x1=x1+1
		count+=1
	return count
T=input().split()
if len(T)>1:
	x1=int(T[1])
	y1=int(T[2])
	x2=int(T[3])
	y2=int(T[4])
	count=0
	if x1==y1==0:
		y1+=1
		count+=1
	ans=sol(x1,y1,x2,y2,count)
	print('Case '+str(1)+': '+str(ans))
else:
	for t in range(int(T[0])):
		x1,y1,x2,y2=map(int, input().split())
		count=0
		if x1==y1==0:
			y1+=1
			count+=1
		ans=sol(x1,y1,x2,y2,count)
	
		print('Case '+str(t+1)+': '+str(ans))
		

# T=input().split()
# bug=0
# if len(T)>1:
# 	bugarr=T[1:]
# 	T=T[0]
# 	bug=1

# for t in range(int(T[0])):
# 	if bug==1:
# 		x1=int(bugarr[0])
# 		y1=int(bugarr[1])
# 		x2=int(bugarr[2])
# 		y2=int(bugarr[3])
# 	else:
# 		x1,y1,x2,y2=map(int, input().split())
		
# 	if x1==y1==0:
# 		y1=1
# 		count=1
# 	else:
# 		count=0
		
# 	while 1:
# 		if x1==x2 and y1==y2:
# 			break
# 		if y1==0:
# 			y1=x1+1
# 			x1=0
# 		else:
# 			x1+=1
# 			y1-=1
# 		count+=1
# 	print('Case '+str(t+1)+': '+str(count))
		
		
			
		
# # tmp=input().split()
# # bug=[]
# # if len(tmp)>1:
# # 	bug=tmp[1:]
# # 	T=tmp[0]
# # else:
# # 	T=int(tmp[0])

# # for t in range(int(T)):
# # 	if len(bug)<1:
# # 		tmp=list(map(int, (input().split())))
# # 		a=[tmp[0],tmp[1]]
# # 		b=[tmp[2],tmp[3]]
# # 	else:
# # 		a=[int(bug[0]),int(bug[1])]
# # 		b=[int(bug[2]),int(bug[3])]

# # 	if a[0]==0 and a[1]==0:
# # 		a[1]+=1
# # 		count=1
# # 	else:
# # 		count=0
		
# # 	while a[0]!=b[0] or a[1]!=b[1]:
# # 		if a[1]==0:
# # 			a[1]=a[0]+1
# # 			a[0]=0
# # 		else:
# # 			a[1]-=1
# # 			a[0]+=1
# # 		count+=1
# # 	print('Case '+str(t+1)+': '+str(count))
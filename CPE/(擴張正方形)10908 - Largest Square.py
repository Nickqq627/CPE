T=input()
for t in range(int(T)):
	x,y,TT=map(int, input().split())
	print(x,y,TT)
	arr=[]
	arr.append(['0' for i in range(y+2)])
	for i in range(x):
		tmp=[]
		tmp+=list(input())
		tmp.append('0')
		tmp.insert(0,'0')
		arr.append(tmp)
	arr.append(['0' for i in range(y+2)])
	for tt in range(TT):
		a,b=map(int, input().split())
		a=a+1
		b=b+1
		count=1
		p=0
		for i in range(1,100):
			for j in range(a-i,a+i+1):
				for k in range(b-i,b+i+1):
				#	print(j,k)
					if arr[a][b]!=arr[j][k]:
						p=1
			if p==1:
				break
			count+=2
		print(count)
# T=input()
# for t in range(int(T)):
# 	arr=list(map(int, input().split()))
# 	print(arr[0],arr[1],arr[2])
# 	squ=[]
# 	for i in range(arr[0]):
# 		squ.append(list(input()))
# 	for i in range(int(arr[2])):
# 		a,b=map(int, input().split())
# 		count=1
# 		p=0
# 		while p==0:
# 			for n in range(1,100):
# 				for j in range(a-n,a+n+1):
# 					for k in range(b-n,b+n+1):
# 						if 0<=j<arr[0] and 0<=k<arr[1]:
# 							if squ[j][k]!=squ[a][b]:
# 								p=1
# 						else:
# 							p=1
# 				if p==0:
# 					count+=2
# 				else:
# 					break
# 		print(count)
		


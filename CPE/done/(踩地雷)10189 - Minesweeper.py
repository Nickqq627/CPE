count=1
while 1:
	try:
		a,b=map(int, input().split())
		if a==b==0:
			break
		if count>1:
			print()
		print('Field #'+str(count)+':')
		count+=1
		arr=[]
		for i in range(a):
			arr.append(list(input()))
		for i in range(a):
			for j in range(b):
				if arr[i][j]=='*':
					print(arr[i][j],end="")	
					continue
				else:
					arr[i][j]=0
					if j-1>=0:
						if arr[i][j-1]=='*':
							arr[i][j]+=1
					if j+1<b:
						if arr[i][j+1]=='*':
							arr[i][j]+=1		
					if i+1<a:
						if arr[i+1][j]=='*':
							arr[i][j]+=1
					if i-1>=0:
						if arr[i-1][j]=='*':
							arr[i][j]+=1
					if i-1>=0 and j-1>=0:
						if arr[i-1][j-1]=='*':
							arr[i][j]+=1
					if i-1>=0 and j+1<b:
						if arr[i-1][j+1]=='*':
							arr[i][j]+=1
					if i+1<a and j-1>=0:
						if arr[i+1][j-1]=='*':
							arr[i][j]+=1
					if i+1<a and j+1<b:	
						if arr[i+1][j+1]=='*':
							arr[i][j]+=1
				print(arr[i][j],end="")	
			print()	
		
	except:
		break
# count=1
# while 1:
# 	try:
# 		mine=[]
# 		x,y=map(int, input().split())
# 		if x==y==0:
# 			break
# 		if count>1:
# 			print('')# 格式
# 		for t in range(x):
# 			mine.append(list(input()))
# 		print('Field #' + str(count) +':')
# 		count+=1
# 		for i in range(x):
# 			for j in range(y):
# 				if mine[i][j]!='*':
# 					mine[i][j]=0
# 					if j-1>=0:
# 						if mine[i][j-1]=='*':
# 							mine[i][j]+=1
# 					if j+1<y:
# 						if mine[i][j+1]=='*':
# 							mine[i][j]+=1
# 					if i+1<x:
# 						if mine[i+1][j]=='*':
# 							mine[i][j]+=1
# 					if i-1>=0:
# 						if mine[i-1][j]=='*':
# 							mine[i][j]+=1
# 					if i-1>=0 and j-1>=0:
# 						if mine[i-1][j-1]=='*':
# 							mine[i][j]+=1
# 					if i+1<x and j+1<y:
# 						if mine[i+1][j+1]=='*':
# 							mine[i][j]+=1
# 					if i-1>=0 and j+1<y:
# 						if mine[i-1][j+1]=='*':
# 							mine[i][j]+=1
# 					if i+1<x and j-1>=0:
# 						if mine[i+1][j-1]=='*':
# 							mine[i][j]+=1
# 				print(mine[i][j],end='')
# 			print()
# 	except:
# 		break
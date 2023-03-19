T=input()
for t in range(int(T)):
	tmp=list(input().split())
	n=int(tmp[2])
	mix=[]
	for nn in range(n):
		mix.append(input().split())
	c=0
	for i in range(n):
		for j in range(n):
			if mix[i][j]!=mix[n-i-1][n-j-1] or int(mix[i][j])<0:
				c=1
				break
		if c==1:
			break
	if c==1:
		print('Test #'+str(t+1)+': Non-symmetric.')
	else:
		print('Test #'+str(t+1)+': Symmetric.')
# def mix(arr):
# 	n=len(arr)
# 	for i in range(n):
# 		for j in range(n):
# 			if arr[i][j]!=arr[n-1-i][n-1-j] or int(arr[i][j])<0:
# 				return 1	
# 	return 0

# T=input()
# for t in range(int(T)):
# 	arrn=list(input().split())
# 	n=int(arrn[2])
# 	arr=[]
# 	count=0
# 	for i in range(n):
# 		arr.append(input().split())
# 	count=mix(arr)
# 	if count==1:
# 		print('Test #' + str(t+1) + ': Non-symmetric.')
# 	else:
# 		print('Test #' + str(t+1) + ': Symmetric.')
# def ff(mtx,n):
# 	for j in range(n):
# 		for k in range(n):
# 			if int(mtx[j][k])<0:
# 				return 'Non-symmetric.'
# 			if mtx[j][k]!=mtx[n-j-1][n-k-1]:
# 				return 'Non-symmetric.'
# 	return 'Symmetric.'
			
# T=int(input())
# for i in range(T):
# 	arr=list(input().split())
# 	n=int(arr[2])
# 	mtx=[]
# 	for j in range(n):
# 		mtx.append(input().split())
# 	print('Test #' + str(i+1) + ': ' + ff(mtx,n))
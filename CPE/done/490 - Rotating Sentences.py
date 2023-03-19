arr=[]
while 1:
	try:
		arr.append(list(input()))
	except:
		break
m=0
for i in range(len(arr)):
	if len(arr[i])>m:
		m=len(arr[i])
for i in range(m):
	for j in range(len(arr)-1,-1,-1):
		if len(arr[j])<=i and j==0:
			print('',end="")
		elif len(arr[j])<=i:
			print(' ',end="")
		else:
			print(arr[j][i],end="")
	print()


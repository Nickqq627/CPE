arr=[]
while 1:
	try:
		arr.append(list(input()))
	except:
		break
count=0
for i in range(len(arr)):
	for j in range(len(arr[i])):
		if arr[i][j]=='"' and count==0:
			arr[i][j]='``'
			count=1
		elif arr[i][j]=='"' and count==1:
			arr[i][j]="''"
			count=0
		print(arr[i][j],end="")
	print()
	
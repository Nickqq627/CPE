arr='qwertyuiop[]'+"asdfghjkl;'"+'zxcvbnm,./'
arr=list(arr)
while 1:
	try:
		a=list(input())
		for i in range(len(a)):
			a[i]=a[i].lower()
			for j in range(len(arr)):
				if a[i]==arr[j]:
					a[i]=arr[j-2]
					break
		for i in a:
			print(i,end="")
		print()		
	except:
		break
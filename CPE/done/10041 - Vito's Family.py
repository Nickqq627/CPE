T=input()
for t in range(int(T)):
	arr=list(map(int, input().split()))
	arr=sorted(arr[1:])
	m=len(arr)//2
	sum=0
	for i in arr:
		sum+=abs(arr[m]-i)
	print(sum)
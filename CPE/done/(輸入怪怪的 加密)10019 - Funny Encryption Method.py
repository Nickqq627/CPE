T=list(map(int, input().split()))
arr=[]
bug=0
if len(T)>1:
	bug=1
	arr=T[1:]
else:
	for t in range(T[0]):
		arr.append(int(input()))	
for i in arr:
	x1=bin(i)
	x2=bin(int('0x'+str(i),16))
	b1=0
	b2=0
	for j in range(len(x1)):
		if x1[j]=='1':
			b1+=1
	for k in range(len(x2)):
		if x2[k]=='1':
			b2+=1	
	print(b1,b2)	
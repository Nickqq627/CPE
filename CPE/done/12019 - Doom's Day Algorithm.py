month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
day=['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
T=input()
for t in range(int(T)):
	a,b=map(int, input().split())
	sum=0
	for i in range(a):
		sum+=month[i]
	sum+=b
	print(day[sum%7])
	
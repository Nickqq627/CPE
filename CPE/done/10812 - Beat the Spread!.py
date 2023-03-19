def ff(a,b):
	ans=''
	for i in range(a+1):
		for j in range(a+1):
			if i+j==a and abs(i-j)==b:
				if i>j:
					ans=str(i)+' '+str(j)
				else:
					ans=str(j)+' '+str(i)
				return ans
	return 'impossible'
T=int(input())
for t in range(T):
	a,b=map(int, input().split())
	ans=ff(a,b)
	print(ans)
	
# T=input()
# for t in range(int(T)):
# 	a,b=map(int, input().split())
# 	x=0
# 	y=0
# 	c=0
# 	for i in range(max(a,b)):
# 		for j in range(max(a,b)):
# 			if i+j==a and abs(i-j)==b:
# 				c=1
# 				if i>j:
# 					x=i
# 					y=j
# 				else:
# 					x=j
# 					y=i
# 				break
# 		if c==1:
# 			break
# 	if c==0:
# 		print('impossible')
# 	else:
# 		print(x,y)
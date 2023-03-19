while 1:
	try:
		a,b=map(int, input().split())
		if a==b==0:
			break
		count=0
		for i in range(a,b+1):
			if (i**(1/2))%1==0:
				count+=1
		print(count)
	except:
		break
# while 1:
# 	try:
# 		a,b=map(int, input().split())
# 		count=0
# 		if(a==b==0):
# 			break
# 		for i in range(a,b+1):
# 			if float(i**(1/2)).is_integer():
# 				count+=1
# 		print(count)
# 	except:
# 		break
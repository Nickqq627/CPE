while 1:
	try:
		a,b=map(int, input().split())
		if a==b==0:
			break
		carry=0
		count=0
		while a!=0 or b!=0:
			if a%10+b%10+carry>9:
				carry=1
				count+=1
			a=a//10
			b=b//10
			
		if count==0:
			print('No carry operation.')
		elif count==1:
			print('1 carry operation.')
		else:
			print(str(count)+' carry operations.')	
	except:
		break

# while 1:
# 	try:
# 		a,b=input().split()
# 		if a==b=='0':
# 			break
# 		a=list(map(int, a))
# 		b=list(map(int, b))
# 		if len(a)>len(b):
# 			while len(a)!=len(b):
# 				b.insert(0,0)
# 		else:
# 			while len(a)!=len(b):
# 				a.insert(0,0)
# 		carry=0
# 		count=0
# 		for i in range(len(a)-1,-1,-1):
# 			if a[i]+b[i]+carry>9:
# 				carry=1
# 				count+=1
# 			else:
# 				carry=0
# 		if count==1:
# 			print('1 carry operation.')
# 		elif count==0:
# 			print('No carry operation.')
# 		else:
# 			print(str(count)+' carry operations.')
			
# 	except:
# 		break
	
	




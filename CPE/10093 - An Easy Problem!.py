arr='0123456789'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'abcdefghijklmnopqrstuvwxyz'
arr=list(arr)
while 1:
	try:
		a=input()
		if a[0]=='-' or a[0]=='+':
			a=a[1:]
		if a=='0':
			print(2)
		else:
			sum=0
			m=0
			for i in a:
				sum+=arr.index(i)
				if arr.index(i)>m:
					m=arr.index(i)
			ans=0		
			for i in range(m,63):
				if sum%i==0:
					ans=i
					break
			if ans==0:
				print('such number is impossible!')
			else:
				print(ans+1)
			
	except:
		break
# arr = '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'+'abcdefghijklmnopqrstuvwxyz'
# arr = list(arr)
# while 1:
# 	try:
# 		a=input()
# 		if a=='0':
# 			print(2)
# 		else:
# 			sum=0
# 			m=0
# 			for i in a:
# 				for j in arr:
# 					if i==j:
# 						sum+=arr.index(i)
# 						if arr.index(i)>m:
# 							m=arr.index(i)
# 			count=0	
# 			ans=0
# 			for i in range(m,63):
# 				if sum%i==0:
# 					count=1
# 					ans=i+1
# 					break
					
# 			if count==1:
# 				print(ans)
# 			else:
# 				print('such number is impossible!')	
# 	except:
# 		break
while 1:
	try:
		T=input()
		arr=[]
		for t in range(int(T)):
			arr.append(int(input()))
		arr=sorted(arr)
		ans2=0
		if len(arr)%2==1:
			ans1=arr[len(arr)//2]
			for i in arr:
				if i==arr[len(arr)//2]:
					ans2+=1
			ans3=1
		else:
			ans1=arr[len(arr)//2-1]
			for i in arr:
				if i==arr[len(arr)//2] or i==arr[len(arr)//2-1]:
					ans2+=1
			ans3=arr[len(arr)//2]-arr[len(arr)//2-1]+1
		print(ans1,ans2,ans3)
	except:
		break
# while 1:
# 	try:
# 		T=input()
# 		arr=[]
# 		for t in range(int(T)):
# 			arr.append(int(input()))
# 		arr=sorted(arr)
# 		ans2=0
# 		if len(arr)%2==0:
# 			ans1=arr[len(arr)//2-1]
# 			ans2+=arr.count(arr[len(arr)//2-1])
# 			if arr[len(arr)//2-1]!=arr[len(arr)//2]:
# 				ans2+=arr.count(arr[len(arr)//2])		
# 			ans3=arr[len(arr)//2]-arr[len(arr)//2-1]+1
# 			if ans3==0:
# 				ans3=1
# 		else:
# 			ans1=arr[len(arr)//2]
# 			ans2+=arr.count(ans1) 
# 			ans3=1
# 		print(ans1,ans2,ans3)
# 	except:
# 		break
# while 1:
# 	try:
# 		arr=[]
# 		a=0
# 		b=0
# 		aa=''
# 		T=input()
# 		for t in range(int(T)):
# 			arr.append(int(input()))
# 		arr=sorted(arr)
# 		if len(arr)%2==0:
# 			a=arr[int(len(arr)/2-1)]
# 			aa=arr[int(len(arr)//2)]
# 			if a!=aa:
# 				b+=arr.count(a)
# 				b+=arr.count(aa)
# 			else:
# 				b+=arr.count(a)
# 			c=(aa-a)+1
# 		else:
# 			a=arr[int(len(arr)//2)]
# 			b+=arr.count(a)
# 			c=1
			
# 		print(a,b,c)
		
# 	except:
# 		break
c=0
while 1:
	try:
		if c>0:
			space=input()
		c+=1
		T=input()
		arr=list(map(int, input().split()))
		count=1
		ans=[]
		for i in range(len(arr)):
			for j in range(i+1,len(arr)):
				if abs(arr[i]-arr[j]) in ans:
					count=0
					break
				else:
					ans.append(abs(arr[i]-arr[j]))
			if count==0:
				break
		if count==1:
			print('Case #'+str(c)+': It is a B2-Sequence.')	
		else:
			print('Case #'+str(c)+': It is not a B2-Sequence.')	
		print()
	except:
			break
# def b2(arr):
# 	for i in range(len(arr)):
# 		for j in range(len(arr)):
# 			if i==j:
# 				break
# 			if arr[i]+arr[j] in test:
# 				return 'It is not a B2-Sequence.'
# 			else:
# 				test.append(arr[i]+arr[j])
# 	return 'It is a B2-Sequence.'
	
# count=0
# while 1:
# 	try:
# 		T=int(input())
# 		test=[]
# 		count+=1
# 		arr=list(map(int, input().split()))
# 		print('Case #' + str(count) + ': ' + b2(arr))
# 		print()
# 		spcace=input() #沒用
# 	except:
# 		break
def b2(arr):
	ans=[]
	for i in range(len(arr)-1):
		if arr[i+1]-arr[i] in ans:
			return 1
		else:
			ans.append(arr[i+1]-arr[i])
	return 0
t=0	
while 1:
	try:
		t+=1
		n=int(input())
		arr=list(map(int, input().split()))
		count=b2(arr)
		if count==1:
			print('Case #'+str(t)+': It is not a B2-Sequence.')
		else:
			print('Case #'+str(t)+': It is a B2-Sequence.')
		print()
		space=input()

	except:
		break
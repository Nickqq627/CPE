T=input()
for t in range(int(T)):
	TT=input()
	arr=list(map(int, input().split()))
	count=0
	while arr!=sorted(arr):
		for j in range(len(arr)-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
				count+=1
	print('Optimal train swapping takes '+str(count)+' swaps.')
# T=input()
# for t in range(int(T)):
# 	tt=input()
# 	count=0
# 	arr=list(map(int, input().split()))
# 	for i in range(len(arr)):
# 		for j in range(len(arr)-1):
# 			if arr[j]>arr[j+1]:
# 				tmp=arr[j]
# 				arr[j]=arr[j+1]
# 				arr[j+1]=tmp
# 				count+=1
# 	print('Optimal train swapping takes '+str(count)+' swaps.')
# # T=input()
# # for t in range(int(T)):
# # 	a=input()
# # 	arr=list(map(int, input().split()))
# # 	ans=arr
# # 	arr=sorted(arr)
# # 	count=0
# # 	while ans!=arr:
# # 		for i in range(int(a)-1):
# # 			if ans[i]>ans[i+1]:
# # 				tmp=ans[i]
# # 				ans[i]=ans[i+1]
# # 				ans[i+1]=tmp
# # 				count+=1
# # 	print('Optimal train swapping takes '+str(count)+' swaps.')
		
T=input()
arr=[]
dic={}
for t in range(int(T)):
	arr+=list(input())
for i in range(len(arr)):
	arr[i]=arr[i].upper()
	if str.isalpha(arr[i]):
		if arr[i] not in dic:
			dic[arr[i]]=1
		else:
			dic[arr[i]]+=1
ans=sorted(dic.items(),key=lambda x:x[0])
ans=sorted(ans,key=lambda x:x[1],reverse=True)
for x,y in ans:
	print('{} {}'.format(x,y))
	
x=[7,6,5,9,8,3,2,1,1,0]
x=[0,1,1,2,3,5,7,8,9,10,12]
# 選擇排序法
def selection(x):
    for i in range(0,len(x)):
        min=999
        for j in range(i,len(x)):
            if x[j]<min:
                min=x[j]
                mins=j
        tmp=x[i]
        x[i]=min
        x[mins]=tmp
    return x
# print(selection(x))

# 插入排序法
# def insertion(x):
#     for i in range(0,len(x)):
#         for j in range(i,len(x)):
#             if 
#                 x[i]

# 氣泡排序法
def bubble(x):
    for i in range(1,len(x)):
        flag=0
        for j in range(0,len(x)-i):
            print(1)
            if x[j]>x[j+1]:
                tmp=x[j]
                x[j]=x[j+1]
                x[j+1]=tmp
                flag=1
        if flag==0:
            return x
    return x
# print(bubble(x))

# 快速排序法
def quick(x):
    if len(x)<=1: return x
    flag=x[0]
    l=[]
    r=[]
    for i in range(1,len(x)):
        if x[i]>flag:
            r.append(x[i])
        else:
            l.append(x[i])
    ll=quick(l)
    rr=quick(r)
    return ll+[x[0]]+rr
# print(quick(x))

# 二元搜尋法
key=9
mid=0
left=0
right=len(x)-1
while left<=right:
    mid=(right+left)//2
    if x[mid]==key:
        print(mid)
        break
    elif key>x[(left-right)//2]:
        left=mid+1
    else:
        right=mid-1
if right<left:
    print("沒找到")

# 河內塔
# count=0
# def hanoi(n,a,b,c):
#     global count
#     if n==1:
#         count+=1
#         print(count,':盤子',n,'從',a,'到',c)
#     else:
#         hanoi(n-1,a,c,b)
#         count+=1
#         print(count,':盤子',n,'從',a,'到',c)
#         hanoi(n-1,b,a,c)
# hanoi(3,'A','B','C')

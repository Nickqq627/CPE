# s="1234"
# ss=''
# for i in range(len(s),0,-1):
#     ss=ss+s[i-1:i]
# print(ss)

# word = 'geeks for geeks'
# print(word.find('fors'))
# a=123
# b=456
# sa=str(a)
# sb=str(b)
# for i in range(3,0,-1):
#     print(int(sa[i-1:i])+int(sb[i-1:i]))
# ss=s[3:4]+s[2:3]+s[1:2]+s[0,1]
# print(sa[-18])
# def cou(x):
#     count=0
#     while(x!=1):
#         if x % 2 == 0:
#             x=x/2
#             count+=1
#         else:
#             x=x*3+1
#             count+=1
#     return count+1
# print(cou(9))
# a=3123456

# print(a-int(a/1000000)*1000000)

# def f(n):
#     if(n>=10000000):
#         f(math.floor(n/10000000))
#         print(' kuti ',end='')
#         n%=10000000
#     if(n>=100000):
#         f(math.floor(n/100000))
#         print(' lakh ',end='')
#         n%=100000
#     if(n>=1000):
#         f(math.floor(n/1000))
#         print(' hajar ',end='')
#         n%=1000
#     if(n>=100):
#         f(math.floor(n/100))
#         print(' shata ',end='')
#         n%=100
#     if(n>=1):
#         print(n,end='')

# import math
# from sys import stdin
# for s in stdin:
#     n=int(s)
#     if(n>0):
#         f(n)
#     print('\n')

# a="hi hihi hihihi"
# dicta={"yes":1,"no":2}
# if 3 in dicta.values():
#     print(4)
# a='"123"'
# a.replace('"',"''")
# print(a)
# def hi(x):
#     for i in range(2,x+1):
#         if x%i==0:
#             x=x/i
#         break
#     return x
# x=12
# while x>1:
#     for i in range(2,int(x+1),1):
#         if x%i==0:
#             print(i)
#             x=x/i
#             break

# a=[1,2,3,4,5,7,1,1,1]
# print(a.count(1))

# for i in reversed(range(10)):
#     print(i)

# a='52334'
# k=0
# k=k+int(a[0])
# print(k)
# for i in range(0,len(a)):
#     print(123)
# n=15
# for i in range(n):# 0~14 arr[i]%m>arr[j]%m
#     for j in range(n):
#         print(i,j)

# f=[10, 16,-4,3,-3,9]
# m=6
# def cmp(x):

#     if x<0:
#         pn=-1
#     else:
#         pn=1

#     k1=abs(x) % m *pn

#     if(x % 2 ==1):
#         k2,k3=-x,0
#     else: 
#         k2,k3=0,x
#     print(x,k1,k2,k3)
#     return k1,k2,k3

# f.sort(key=cmp)
# print(f)



# print(ans)
a='12345'
b=list(a)
print(b)
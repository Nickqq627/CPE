# import random
# countin=0
# countout=0
# for i in range(100000):
#     x = random.randint(1,1000)
#     y = random.randint(1,1000)
#     if (x*x+y*y)<1000000:
#         countin+=1
# print(countin/100000*4)

# for i in range(1000,10000):
#     zz=str(i)
#     ss=""
#     for k in range(len(zz),0,-1):
#         ss=ss+zz[k-1:k]
#     kk=int(ss)    
#     for j in range(2,10):
#         if i*j==kk:
#             print("%d*%d=%s" % (i,j,ss))

# for i in range(61234,79866):
#     for j in range(1234,9877):
#         if i-j==66666:
#             count = 0
#             ans = str(i)+str(j)
#             for k in range(1,10):
#                 count+=ans.find(str(k))
#             if count == 36:
#                 print(i,j,i-j)

# s=[[1,2,3],[1,2,3],[1,2,3]}

# for i in range(123,988):
#     for j in range(123,988):
#         for k in range(123,988):
#             si=str(i)
#             sj=str(j)
#             sk=str(k)
#             if int(si[0:1])+int(sj[0:1])+int(sk[0:1])==int(si[1:2])+int(sj[1:2])+int(sk[1:2])==int(si[2:3])+int(sj[2:3])+int(sk[2:3]):
#                 if int(si[0:1])+int(si[1:2])+int(si[2:3])==int(sj[0:1])+int(sj[1:2])+int(sj[2:3])==int(sk[0:1])+int(sk[1:2])+int(sk[2:3]):
#                     if int(si[0:1])+int(sj[1:2])+int(sk[2:3])==int(si[2:3])+int(sj[1:2])+int(sk[0:1]):
#                         ans = si+sj+sk
#                         count=0
#                         # print(si)
#                         # print(sj)
#                         # print(sk)
#                         for l in range(1,10):
#                             count+=ans.find(str(l))
#                         if count == 36:
#                             print('->'+si)
#                             print('->'+sj)
#                             print('->'+sk)

# def min(x):
#     key=x[0]
#     index=0
#     for i in range(0,len(x)-1):
#         if x[i]<key:
#             key=x[i]
#             index=i
#     return key,index

# print(min([2,5,9,1,6,3,5]))


# x=[1,2,3]
# y=[5,6,7]
# print(x+[4]+y)
a="12345"
b=list(a)
for i in range(0,len(b)):
    b[i]=int(b[i])
print(b)
c="AbC"
print(c.upper())
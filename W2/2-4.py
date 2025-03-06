n=int(input())
freq={}
for i in range(n):
    num=int(input())
    for j in range(num):
        lis=input().split(" ")
        if lis[0] not in freq:
            freq[lis[0]]=int(lis[1])
        else:
            freq[lis[0]]+=int(lis[1])
import collections
dic=collections.OrderedDict(sorted(freq.items(),key=lambda x:x[0],reverse=True))
for i in dic:
    print(i,dic[i])
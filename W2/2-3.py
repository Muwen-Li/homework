n,m=map(int,input().split(' '))
students=input().split(' ')
course=[]
count=0
freq={key:0 for key in students}
for i in range(m):
    members=input().split(' ')
    for member in members:
        member=member.strip()
        freq[member]+=1
for name in students:
    if freq[name]==0:
        count+=1
print(count)
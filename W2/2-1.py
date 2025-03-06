students=eval(input())
sorted_students=sorted(students,key=lambda x:x[2],reverse=True)
for item in sorted_students:
    print(item[0],item[1],item[2])
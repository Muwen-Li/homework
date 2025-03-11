def my_sum(*args,value=1):
    '''
    Add Value To Numbers
    '''
    list0=[]
    for i in args:
        if(value==None):
            list0.append(i+1)
        else:
            list0.append(i+value)
    return list0
print(my_sum(1,2,3,4,5))

def get_my_counter():
    x=0
    def counter():
        nonlocal x
        x+=1
        return x
    return counter
my_counter=get_my_counter()
print(my_counter())
print(my_counter())
print(my_counter())

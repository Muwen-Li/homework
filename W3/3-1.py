import random

def my_random(keys,weights):
    total=[]
    for i in range(len(keys)):
        total.extend([keys[i]]*weights[i])
    return random.sample(total,1)[0]

print(my_random([1,2,3,4],[1,1,1,5]))

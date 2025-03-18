import collections
import json
def get_sorted_keys_values(file_path):
    with open(file_path, 'r', encoding='utf-8') as dic:
        data=json.load(dic)
    sorted_items=sorted(data.items(),key=lambda x:x[0])
    sorted_keys=[item[0] for item in sorted_items]
    sorted_values=[item[1] for item in sorted_items]
    result=[sorted_keys,sorted_values]
    return result

def get_sorted_keys_values0(data):
    sorted_items=sorted(data.items(),key=lambda x:x[0])
    sorted_keys=[item[0] for item in sorted_items]
    sorted_values=[item[1] for item in sorted_items]
    result=[sorted_keys,sorted_values]
    return result

print(get_sorted_keys_values0({'john':1,'peter':2,'adam':3}))
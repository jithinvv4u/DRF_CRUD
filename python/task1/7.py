# Convert Nested Tuple to Custom Key Dictionary

test_tuple = ((1, 'Gfg', 2), (3, 'best', 4))
keys = ['key', 'value', 'id']

new_dict=[{key: val for key,val in zip(keys,data)} for data in test_tuple]
    
print(new_dict)
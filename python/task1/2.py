#Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict={}

for key in keys:
    for value in values:
        new_dict[key]=value
        values.remove(value)
        break
print(new_dict)
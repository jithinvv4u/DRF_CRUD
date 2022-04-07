# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
result=[]
for num in a:
    if num%2==0:
        result.append(num)
    
print(result)
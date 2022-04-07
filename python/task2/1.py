# problem 1:
# -----------
# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000
# return 0000 1111 0000 1111 0000 1111 0000 1111

num='1111,0000,1111,0000,1111,0000,1111,0000'
num2=''
for i in num:
    if i=='0':
        num2+='1'
    if i=='1':
        num2+='0'
data=str(num2)
print(data)
out = [(num2[i:i+4]) for i in range(0, len(data), 4)]
print(out)

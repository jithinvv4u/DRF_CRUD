# problem: 4
# -----------

# Using a method that returns 7 characters from a file, implement readN(n) which reads n characters.

# For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".

string_data="When you reach the end of your rope, tie a knot in it and hang on."

def readN(n):
    f=open('/home/jithin/TASK_FFZ/python/task2/data.txt','r')
    print(f.read(n))

readN(7)
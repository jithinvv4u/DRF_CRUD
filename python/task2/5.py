# problem: 5
# ----------

# Write a function that takes a natural number as input and returns the number of digits the input has.

# Constraint: don't use any loops.


def num_length(n):
    if n>=0:
        num=str(n)
        print(len(num))
    
num_length(7675)
# problem: 2
# ------------
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix
# by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column.
# Similarly, given the target word 'MASS', you should return true, since it's the last row.


def check(matrix,word):
     for spell in matrix:
          spell="".join(spell)
          if word in spell:
               return True

     spell=0
     while spell<len(matrix):
          data="".join([col[spell] for col in matrix])
          spell+=1
          if word in data:
               return True
     return False


matrix= [['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]

word = "FOAM"

print(check(matrix,word))
# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.

import string
import random

characters=list(string.ascii_letters+string.digits+"@#$&*!")

password=[]
for pswd in range(10):
    password.append(random.choice(characters))

random_password="".join(password)

print(random_password)
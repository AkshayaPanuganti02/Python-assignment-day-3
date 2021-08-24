# Assignment day-3
# Write a program everytime to generate a six character otp

import random
import string

id = ''
characters_list = list(string.ascii_letters + string.digits)
for i in range(6):
  id += random.choice(characters_list)

print(id)




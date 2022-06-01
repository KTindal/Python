## Script to generate a random password using special characters, numbers, and ascii letters ##
# Length of password generated will vary depending on value supplied to range() in for loop ##

import random
from string import digits
from string import punctuation
from string import ascii_letters

password = ""
symbol = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
for i in range(30):
    password += "".join(secure_random.choice(symbol))
print(password)

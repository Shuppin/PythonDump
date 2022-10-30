import random

chars = 'ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghigklnmopqrstuvwxxyz1234567890!"£$%^&*()[]{}@~#/\|?<>,.'

length = input('Password Length: ')
length = int(length)

amount = input('Number Of Passwords: ')
amount = int(amount)

for p in range(amount):
  password = ''
  for c in range(length):
      password += random.choice(chars)
   
  print(password)


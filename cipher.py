#Cipher

import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

while True:
  plain_text = input('Enter the message: ')

  if plain_text == 'quit':
    break

  cipher_text = ''

  for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

  print(f'encrypted message: {cipher_text}')

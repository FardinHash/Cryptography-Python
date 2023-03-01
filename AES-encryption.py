#AES encryption

from Crypto.Cipher import AES
import os

key = os.urandom(16)

message = 'Sayy my name SOS'

pasw = AES.new(key)

encrypt = pasw.encrypt(message)

print(encrypt.hex())

decrypt = pasw.decrypt(encrypt)

print(decrypt)

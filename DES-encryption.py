#DES encryption

from Crypto.Cipher import DES
import os

key = os.urandom(8)

message = 'Sayy my name SOS'

pasw = DES.new(key)

encrypt = pasw.encrypt(message)

print(encrypt.hex())

decrypt = pasw.decrypt(encrypt)

print(decrypt)

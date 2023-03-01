#Hashing text MD5

import hashlib

md5 = hashlib.md5()

print(md5)

md5.update(b'Say my name')

print(md5.digest())

print(md5.hexdigest())

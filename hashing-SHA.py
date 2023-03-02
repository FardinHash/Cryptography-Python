#Hashing text SHA

import hashlib

sha = hashlib.sha1(b'Say my name').digest()

sha2 = hashlib.sha1(b'Say my name').hexdigest()

sha256 = hashlib.sha256(b'Say my name').digest()

sha3_256 = hashlib.sha3_256(b'Say my name').digest()

sha512 = hashlib.sha512(b'Say my name').digest()

print(sha)
print(sha2)
print(sha256)
print(sha3_256)
print(sha512)

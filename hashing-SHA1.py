#Hashing text SHA

import hashlib

sha = hashlib.sha1(b'Say my name').digest()

sha2 = hashlib.sha1(b'Say my name').hexdigest()

print(sha)
print(sha2)

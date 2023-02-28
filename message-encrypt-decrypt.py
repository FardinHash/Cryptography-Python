from cryptography.fernet import Fernet

key = Fernet.generate_key()

pasw = Fernet(key)

message = 'Say my name'.encode()

encrypt = pasw.encrypt(message)

print(encrypt)

decrypt = pasw.decrypt(encrypt)

print(decrypt)

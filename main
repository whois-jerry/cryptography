import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt():
    print()
    message = input("Enter message to be encrypted: ")
    message = message.encode()

    iterations = input("Enter a kdf iteration value: ")
    iterations = int(iterations)

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = iterations
    )

    password = input("Enter encryption password: ")
    password = password.encode()

    key = base64.urlsafe_b64encode(kdf.derive(password))
    token = Fernet(key).encrypt(message)
    salt = base64.urlsafe_b64encode(salt)
    
    print()
    print (f"Store these values in a secure place: ")
    print (f"   Your encrypted message ---> {token.decode()}")
    print (f"   Your encryption salt ---> {salt.decode()}")
    print()
    print (f"Commit these values to memory only: ")
    print (f"   Your selected iterations ---> {iterations}")
    print (f"   Your encryption password ---> {password.decode()}")

    print()

def decrypt():
    print()
    token = input("Enter your encrypted message: ")
    token = token.encode()

    salt = input("Enter your salt: ")
    salt = salt.encode()
    salt = base64.urlsafe_b64decode(salt)

    iterations = input("Enter a kdf iteration value: ")
    iterations = int(iterations)

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = iterations
    )

    password = input("Enter your password: ")
    password = password.encode()

    key = base64.urlsafe_b64encode(kdf.derive(password))
    message = Fernet(key).decrypt(token)
    message = message.decode()

    print()
    print (f"Your decrypted message ---> {message}")
    print()

prompt = input("Press 1 to encrypt a message. Press 2 to decrypt a message: ")
if prompt == str(1):
    encrypt()
elif prompt == str(2):
    decrypt()
else:
    print("Please choose an available option.")

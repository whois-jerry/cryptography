# To execute: Open command prompt, navigate to file directory containing script file. Type 'python main.py" to run.
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt():
    print()
    message = input("Enter message to be encrypted: ")
    message = message.encode()
    print()

    salt = input("Enter your salt value: ")
    salt = salt.encode()

    iterations = input("Enter a key derivation iteration value: ")
    iterations = int(iterations)

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = iterations
    )

    print()
    password = input("Enter encryption password: ")
    password = password.encode()

    key = base64.urlsafe_b64encode(kdf.derive(password))
    token = Fernet(key).encrypt(message)
    
    print()
    print (f"Store this value in a secure place: ")
    print (f"   Your encrypted message ---> {token.decode()}")
    print()
    print (f"Commit these values to memory only: ")
    print (f"   Your encryption salt ---> {salt.decode()}")
    print (f"   Your selected key derivation iterations ---> {iterations}")
    print (f"   Your encryption password ---> {password.decode()}")

    print()

def decrypt():
    print()
    token = input("Enter your encrypted message: ")
    token = token.encode()
    print()

    salt = input("Enter your salt: ")
    salt = salt.encode()

    iterations = input("Enter a key derivation iteration value: ")
    iterations = int(iterations)

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = iterations
    )
    
    print()
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

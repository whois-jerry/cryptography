from cryptography.fernet import Fernet

def encrypt():
    print()
    message = input("Enter message to be encrypted: ")
    message = message.encode()

    key = Fernet.generate_key()
    token = Fernet(key).encrypt(message)

    print()
    print (f"Your key ---> {key.decode()}")
    print (f"Your encrypted message ---> {token.decode()}")
    print()

def decrypt():
    print()
    token = input("Enter your encrypted message: ")
    token = token.encode()

    key = input("Enter your key: ")
    key = key.encode()

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
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pyDes import des, ECB, PAD_PKCS5
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt_aes(message):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    

    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    

    return base64.b64encode(ciphertext).decode()

def encrypt_des(message):
    key = b"8bytekey"
    cipher = des(key, ECB, padmode=PAD_PKCS5)
   

    ciphertext = cipher.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()


def encrypt_rsa(message):
    key = RSA.generate(2048)
    public_key = key.publickey()
    
    encryptor = PKCS1_OAEP.new(public_key)
    ciphertext = encryptor.encrypt(message.encode())
    return base64.b64encode(ciphertext).decode()




'''
Encryptor decryptor which uses AES-256-CBC with a random IV and SHA-256 hash
'''
import base64
import sys

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def encrypt(key, source, encode=True):
    '''
    Encrypts the message using AES (CBC mode) with the
    given key.
    Parameters:
        key (bytes):
            The key to use for encryption.
        source (bytes):
            The message to encrypt.
        encode:
        Whether to base64 encode the encrypted message.
    Returns:
        The encrypted message.
    '''
    key = SHA256.new(key).digest()
    i_v = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, i_v)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = i_v + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True):
    '''
    Decrypts the message using AES (CBC mode) with the
    given key.
    Parameters:
        key (bytes):
            The key to use for decryption.
        source (bytes):
            The message to decrypt.
        decode:
        Whether to base64 decode the encrypted message.
    Returns:
        The decrypted message.
    '''
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    i_v = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, i_v)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        print("Reporting to the owner")
        sys.exit("Incorrect password")
    return data[:-padding]

'''
Test file for EncryptorDecryptor
'''
from random import randint

import pytest

from helpers.encryptor_decryptor import decrypt, encrypt
from util.test_modules import generate_random_code, generate_random_string


# Random tests for messages
messages = [generate_random_string(randint(100,10000)) for _ in range(100)]

@pytest.mark.parametrize("test_input, _", zip(messages, messages))
def test_encrypt_decrypt_random(test_input, _):
    '''
    Test encrypt and decrypt for random messages using the same key
    Asserts that the encrypted message is equal to the original message
    Parameters:
        message (bytes): The message to be encrypted
    '''
    key = generate_random_code()
    encrypted = encrypt(key, test_input)
    decrypted = decrypt(key, encrypted)
    assert test_input == decrypted

# Random tests for keys
keys = [generate_random_code(randint(0,100000)) for _ in range(100)]

@pytest.mark.parametrize("test_input, _", zip(keys, keys))
def test_encrypt_decrypt_random_key(test_input, _):
    '''
    Test encrypt and decrypt for random keys using the same message
    Asserts that the encrypted message is equal to the original message
    Parameters:
        key (bytes): The key to be used for encryption
    '''
    source = generate_random_string(100)
    encrypted = encrypt(test_input, source)
    decrypted = decrypt(test_input, encrypted)
    assert source == decrypted

#  Random tests for messages and keys
messages = [generate_random_string(randint(100,10000)) for _ in range(100)]
keys = [generate_random_code(randint(0,100000)) for _ in range(100)]

@pytest.mark.parametrize("test_input,_", zip(messages, keys))
def test_encrypt_decrypt_random_message(test_input, _):
    '''
    Test encrypt and decrypt for random keys and messages
    Asserts that the encrypted message is equal to the original message
    Parameters:
        message (bytes): The message to be encrypted
        key (bytes): The key to be used for encryption
    '''
    encrypted = encrypt(test_input, test_input)
    decrypted = decrypt(test_input, encrypted)
    assert test_input == decrypted
    
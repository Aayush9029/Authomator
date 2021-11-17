from Helper.EncryptorDecryptor import *
from Utils.TestModules import *
import pytest

# Manual random tests
def test_encrypt_decrypt1():
    key = generate_random_code()
    source = generate_random_string(100)
    encrypted = encrypt(key, source)
    decrypted = decrypt(key, encrypted)
    assert source == decrypted
        
def test_encrypt_decrypt2():
    key =  generate_random_code()
    source = generate_random_string(0)
    encrypted = encrypt(key, source)
    decrypted = decrypt(key, encrypted)
    assert source == decrypted
    

# Manual tests
def test_encrypt_decrypt3():
    key = b"0000"
    source = b"Hello World!"
    encrypted = encrypt(key, source)
    decrypted = decrypt(key, encrypted)
    assert source == decrypted


def test_encrypt_decrypt4():
    key = b"4914239klada/23'aasd/asdasd//asdasdasd"
    source = b"Sint velit do in eiusmod eiusmod consectetur est do excepteur mollit culpa esse ullamco cupidatat."
    encrypted = encrypt(key, source)
    decrypted = decrypt(key, encrypted)
    assert source == decrypted

def test_encrypt_decrypt5(message: bytes = b'lorem ipsum', key: bytes = b'lorem ipsum'):
    encrypted = encrypt(key, message)
    decrypted = decrypt(key, encrypted)
    assert message == decrypted

# Random tests for messages
messages = [generate_random_string(randint(100,10000)) for _ in range(100)]

@pytest.mark.parametrize("test_input,expected", zip(messages, messages))
def test_encrypt_decryptRandom(test_input, expected):
    key = generate_random_code()
    encrypted = encrypt(key, test_input)
    decrypted = decrypt(key, encrypted)
    assert test_input == decrypted

# Random tests for keys
keys = [generate_random_code(randint(0,100000)) for _ in range(100)]

@pytest.mark.parametrize("test_input,expected", zip(keys, keys))
def test_encrypt_decryptRandomKey(test_input, expected):
    source = generate_random_string(100)
    encrypted = encrypt(test_input, source)
    decrypted = decrypt(test_input, encrypted)
    assert source == decrypted

#  Random tests for messages and keys
messages = [generate_random_string(randint(100,10000)) for _ in range(100)]
keys = [generate_random_code(randint(0,100000)) for _ in range(100)]

@pytest.mark.parametrize("test_input,expected", zip(messages, keys))
def test_encrypt_decryptRandomKeyAndMessage(test_input, expected):
    encrypted = encrypt(test_input, test_input)
    decrypted = decrypt(test_input, encrypted)
    assert test_input == decrypted
    
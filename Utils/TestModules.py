from random import randint

from Helper.EncryptorDecryptor import encrypt, decrypt


def string_to_bytes(string) -> bytes:
    return bytes(string, 'latin-1')


# Helpers
def generate_random_string(length) -> str:
    random_string = ''.join(
        [chr(randint(0, 255)) for _ in range(length)]
    )
    return string_to_bytes(random_string)

def generate_random_code(start=100, end=100000) -> bytes:
    code =  str(randint(start, end))
    return string_to_bytes(code)


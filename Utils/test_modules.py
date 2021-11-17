'''
Helper modules for testing
'''
from random import randint

def string_to_bytes(string) -> bytes:
    '''
    Returns a bytes object from a string
    Parameters:
        string (str): String to convert to bytes
    Returns:
        bytes: Bytes object
    '''
    return bytes(string, 'latin-1')

# Helpers
def generate_random_string(length) -> bytes:
    '''
    Generates a random string of a given length
    Parameters:
        length (int): Length of the string to be generated
    Returns:
        bytes: Bytes object generated from the string

    '''
    random_string = ''.join(
        [chr(randint(0, 255)) for _ in range(length)]
    )
    return string_to_bytes(random_string)

def generate_random_code(start=100, end=100000) -> bytes:
    '''
    Generates a random code of a given length
    Parameters:
        start (int): Minimum length of the code
        end (int): Maximum length of the code
    Returns:
        bytes: Bytes object generated from the code
    '''
    code =  str(randint(start, end))
    return string_to_bytes(code)
    
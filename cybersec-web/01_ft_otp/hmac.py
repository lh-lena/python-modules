import hashlib

def HMAC(key: str, m: str, hash, l:int=20, block_size=64):
    """
    :param str Key: Authentication key
    :param str m: Is the message to be authenticated
    :param func hash: The hash function to use (e.g. SHA-1)
    :param int l: output size of hash function (e.g. 20 bytes for SHA-1)
    :param int block_size: The block size of the hash function (e.g. 64 bytes for SHA-1)
    """
    block_sized_key = computeBlockSizedKey(key, hash, block_size)

    # ipad = 

    return True

def computeBlockSizedKey(key: str, hash, block_size: int):
    """
    Computes the block sized key

    :param str Key: Authentication key
    :param func hash: The hash function to use (e.g. SHA-1)
    :param int block_size: The block size of the hash function (e.g. 64 bytes for SHA-1)
    """
    # Keys longer than block_size are shortened by hashing them
    if len(key) > block_size:
        key = hash(key)

    # Keys shorter than block_size are padded to block_size by padding with zeros on the right
    if len(key) < block_size:
        ss = block_size - len(key)
        key = key + '0' * ss

    print(key)
    return key
    
computeBlockSizedKey("hello", hashlib.sha1, 64)

#HMAC_SHA1("key", "The quick brown fox jumps over the lazy dog")   = de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9

"""
https://datatracker.ietf.org/doc/html/rfc6238
https://datatracker.ietf.org/doc/html/rfc4226#page-3
https://datatracker.ietf.org/doc/html/rfc2104

https://en.wikipedia.org/wiki/HMAC
https://en.wikipedia.org/wiki/HMAC-based_one-time_password
https://www.geeksforgeeks.org/python-add-trailing-zeros-to-string/
https://www.geeksforgeeks.org/hashlib-module-in-python/
https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/
"""

#!/usr/bin/env python3
import hashlib

def ft_hmac(key: str, msg: str, hash=hashlib.sha1):
    """
    Implements the HMAC algorithm.
    :param hexadecimal str Key: Authentication key
    :param str msg: Is the message to be authenticated
    :param func hash: The hash function to use (e.g. SHA-1)
    Returns: The HMAC digest as a bytes object
    """

    block_size = hash().block_size
    key = key

    # Keys longer than block_size are shortened by hashing them
    if len(key) > block_size:
        key = hash(key).digest()
    elif len(key) < block_size:
        key += b'\x00' * (block_size - len(key))

    ipad = b'\x36' * block_size
    opad = b'\x5C' * block_size
    k_ipad = bytes(a ^ b for a, b in zip(ipad, key))
    k_opad = bytes(a ^ b for a, b in zip(opad, key))
    
    h = hash()
    h.update(k_ipad + msg)
    inner_hash = h.digest()
    h = hash()
    h.update(k_opad + inner_hash)
    return h.digest()

'''
msg_padded = k_ipad + msg.encode()
hashed_msg = hash(msg_padded).digest()
conct_res = k_opad + hashed_msg
return hash(conct_res).digest()
'''


#HMAC_SHA1("key", "The quick brown fox jumps over the lazy dog")   = de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9

'''
import hashlib

m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
m.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
'''
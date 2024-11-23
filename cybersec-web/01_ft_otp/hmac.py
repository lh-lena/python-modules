#!/usr/bin/env python3
import hashlib

KEY = "x347137324A48675838397A33426B464D7436637751784C31724432386A704E3555665668495A59506243536575476F765261576D413073443945437458374A66"
MSG = "x48656C6C6F"

def HMAC(key: str, msg: str, hash, l=20, block_size=64):
    """
    to hash msg
    :param str Key: Authentication key
    :param str msg: Is the message to be authenticated
    :param func hash: The hash function to use (e.g. SHA-1)
    :param int l: output size of hash function (e.g. 20 bytes for SHA-1)
    :param int block_size: The block size of the hash function (e.g. 64 bytes for SHA-1)
    """

    if len(key) < block_size:
        key = key.encode() + b'\x00' * (block_size - len(key))

    # Keys longer than block_size are shortened by hashing them
    if len(key) > block_size:
        key = hash(key.encode()).digest()

    # Keys shorter than block_size are padded to block_size by padding with zeros on the right
    ipad = b'\x36' * block_size
    opad = b'\x5C' * block_size
    k_ipad = key.digest() ^ ipad
    k_opad = key.digest() ^ opad
    msg_padded = k_ipad + msg
    hashed_msg = hash(msg_padded.encode())
    conct_res = k_opad + hashed_msg

    return hash(conct_res.encode())

print(HMAC(KEY, MSG, hashlib.sha1, 20, 64))

#HMAC_SHA1("key", "The quick brown fox jumps over the lazy dog")   = de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9


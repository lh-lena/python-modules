#!/usr/bin/env python3
import sys
import argparse
import string
import time
import hashlib
import hmac
from ft_hmac import ft_hmac
from cryptography.fernet import Fernet

KEY = "68656c6c6f68656c6c6f68656c6c6f68656c6c6f"
MSG = "68656c6c6f68656c6c6f68656c6c6f68656c6c6f"

def ft_opt():
    try:
        ac = len(sys.argv)
        parser = argparse.ArgumentParser()
        parser.add_argument('key', help='A source file containes a hexadecimal key')
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-g', '--encrypt', action='store_true', help='Encrypt a hexadecimal key')
        group.add_argument('-k', '--generate', action='store_true', help='Generate a new temporary password based on ft_otp.key')
        args = parser.parse_args()
        assert ac == 3, f"Invalid input\nUsage: {sys.argv[0]} [OPTION] [KEY_FILE]\n-g:  to save encrypted key given as argument to file.\n-k:  to generate a new temporary password based on the key given as argument"

        if args.encrypt:
            encrypt(args.key)
        elif args.generate:
            print(ft_hmac(KEY.encode(), MSG.encode()))
            h = hmac.new(KEY.encode(), MSG.encode(), hashlib.sha1)
            print("Org HMAC:\n",h.digest())
    except AssertionError as e:
        print(f"{sys.argv[0]}: error: {e}.")
        return 0
    except Exception as e:
        print(f"{sys.argv[0]}: error: {e}.")
        return 1

def is_hex_str(byte_string: str) -> bool:
    return all(c in string.hexdigits for c in byte_string.decode('ascii').strip())

def encrypt(msg_file):
    with open(msg_file, "rb") as f:
        msg = f.read()
        print("Org msg", msg)
        if not msg:
            raise Exception("empty key file")
        if not is_hex_str(msg) or len(msg) < 64:
            raise Exception("key must be 64 hexadecimal characters")

def ft_hopt(HS: bytes):
    """ Implements HOPT algorithm
    HOTP(K,C) = Truncate(HMAC-SHA-1(K,C))

    Args:
        HS (bytes): Generated an HMAC-SHA-1 value, a 20-byte string 
    """
    # Generate a 4-byte string (Dynamic Truncation)
    Sbits = DT(HS)
    # Compute an HOTP value
    Snum = strToNum(Sbits)
    D = Snum % 10**6
    
    def DT(string: bytes):
        offsetBits = string[19]
        offset = strToNum(offsetBits) # 0 <= offset <= 15
        '''
        Let P = String[OffSet]...String[OffSet+3]
        Return the Last 31 bits of P
        '''
        
        
    def strToNum(string):
        return int(string, 2)
    
    return D
if __name__ == "__main__":
    ft_opt()
#!/usr/bin/env python3
import sys
import argparse
import string
import time
import datetime
import hashlib
import hmac
from ft_hmac import ft_hmac
from cryptography.fernet import Fernet

KEY = "68656c6c6f68656c6c6f68656c6c6f68656c6c6f"
MSG = "68656c6c6f68656c6c6f68656c6c6f68656c6c6f"
TIME_DURATION = 30

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

        cur_time = int(time.time())
        T = (cur_time - 1732289019) // TIME_DURATION
        if args.encrypt:
            encrypt(args.key)
        elif args.generate:
            HS = ft_hmac(KEY.encode(), str(T).encode())
            print(HS)
            h = hmac.new(KEY.encode(), str(T).encode(), hashlib.sha1)
            print("Org HMAC:\n",h.digest())
            print(ft_hopt(HS))
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
    Returns:
        int: A 6-digit calculated HOTP value from the HMAC value
    """
    
    def strToNum(string: bytes) -> int:
        return int.from_bytes(string, byteorder='big')

    def DT(string: bytes) -> str:
        """Perfoms the dynamic truncation and then the reduction modulo 10^6
        The purpose of the dynamic offset truncation technique is 
        to extract a 4-byte dynamic binary code from a 160-bit (20-byte) 
        HMAC-SHA-1 result.

        Returns:
            int: Return the Last 31 bits of p
        """
        print("strToNum(string[19]", strToNum(string[19]))
        offset = strToNum(string[19]) & 0xf # 0 <= offset <= 15
        print("offset  ", offset)
        
        # p_str = string[offset:offset+4]
        # p = strToNum(p_str) & 0x7fffffff
        p = ((string[offset] & 0x7f) << 24 | 
            (string[offset+1] & 0xff) << 16 | 
            (string[offset+2] & 0xff) << 8 | 
            (string[offset+3] & 0xff))
        return p
        
    # Generate a 4-byte string (Dynamic Truncation)
    Sbits = DT(HS)
    # Compute an HOTP value
    Snum = strToNum(Sbits)
    D = Snum % 10 ** 6
    return D

if __name__ == "__main__":
    ft_opt()
#!/usr/bin/env python3
import os
import secrets
import sys
import argparse
import string
import time
import hashlib
from dotenv import load_dotenv
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def is_valid_hex_key(byte_string: bytes) -> bool:
    return all(c in string.hexdigits for c in byte_string.decode('ascii').strip())

class KeyStorage:
    """Handles secure key storage with encryption"""

    SALT_FILE = 'ft_otp.salt'
    IV_SIZE = 12

    def __init__(self):
        """Initialize key storage"""
        self.salt = self._get_or_create_salt()

    def _get_or_create_salt(self) -> bytes:
        """Get existing salt or create new one"""
        if os.path.exists(self.SALT_FILE):
            with open(self.SALT_FILE, 'rb') as f:
                return f.read()
        else:
            salt = os.urandom(16)
            with open(self.SALT_FILE, 'wb') as f:
                f.write(salt)
            os.chmod(self.SALT_FILE, 0o600)
            return salt

    def _derive_key(self) -> bytes:
        """Derive a 256-bit AES key from OTP_SECRET_PASSWORD using PBKDF2.
            Output: 32-byte symmetric key."""
        pwd = os.getenv("OTP_SECRET_PASSWORD")
        if not pwd:
            raise ValueError("OTP_SECRET_PASSWORD is missing from the environment (.env).")
        pwd_bytes = pwd.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        return kdf.derive(pwd_bytes)

    def _aes_encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt plaintext using AES-256-GCM.
        Output format: nonce || tag || ciphertext
        """
        key = self._derive_key()
        aes = AESGCM(key)

        nonce = secrets.token_bytes(self.IV_SIZE)
        ciphertext = aes.encrypt(nonce, plaintext, None)

        tag = ciphertext[-16:]
        ct = ciphertext[:-16]

        return nonce + tag + ct

    def _aes_decrypt(self, blob: bytes) -> bytes:
        """
        Decrypt a blob produced by _aes_encrypt().
        Expects: nonce (12) || tag (16) || ciphertext
        """
        key = self._derive_key()
        aes = AESGCM(key)

        nonce = blob[:12]
        tag = blob[12:28]
        ct = blob[28:]

        ciphertext_with_tag = ct + tag
        return aes.decrypt(nonce, ciphertext_with_tag, None)

    def encrypt_and_save_key(self, hex_key: bytes, output_file: str = "ft_otp.key") -> bytes:
        """Encrypt the hexadecimal key using AES-GCM and save key to file"""
        encrypted_key = self._aes_encrypt(hex_key)
        with open(output_file, "wb") as f:
            f.write(encrypted_key)
        print("Key was successfully saved in ft_otp.key.")
    
    def load_encrypted_key(self, input_file: str = "ft_otp.key") -> bytes:
        """Reads and decrypts the AES-encrypted ft_otp.key."""

        try:
            with open(input_file, "rb") as f:
                blob = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Encrypted key file '{input_file}' not found")
        try:
            decrypted = self._aes_decrypt(blob)
        except Exception:
            raise ValueError("Failed to decrypt key: wrong password or corrupted file")
        if not is_valid_hex_key(decrypted):
            raise ValueError("Decrypted key is invalid (should be ≥ 64 hex characters)")
        return decrypted.strip()

def process_encryption(key_file: str) -> None:
    """Read key from file, validate, and store encryptedly"""
    try:
        with open(key_file, 'r') as f:
            key_data = f.read().strip()
    except FileNotFoundError:
        print(f"./ft_otp: error: file '{key_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"./ft_otp: error: unable to read file: {e}", file=sys.stderr)
        sys.exit(1)

    key_bytes = key_data.encode()
    if not is_valid_hex_key(key_bytes):
        print("./ft_otp: error: key must be 64 hexadecimal characters.", file=sys.stderr)
        sys.exit(1)
    storage = KeyStorage()
    storage.encrypt_and_save_key(key_bytes)

def process_totp_generation(key_file: str) -> None:
    if not os.path.exists(key_file):
        print(f"./ft_otp: error: key file '{key_file}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        storage = KeyStorage()
        key_bytes = storage.load_encrypted_key(key_file)
    except Exception as e:
        print(f"./ft_otp: error: unable to generate OTP: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        prog='./ft_otp',
        description='Generate time-based one-time passwords (TOTP)'
    )
    parser.add_argument('key', help='A source file containes a hexadecimal key')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--encrypt', action='store_true', help='Encrypt a hexadecimal key')
    group.add_argument('-k', '--generate', action='store_true', help='Generate a new temporary password based on ft_otp.key')
    try:
        args = parser.parse_args()
    except:
        sys.exit(1)

    if args.encrypt:
        process_encryption(args.key)
    elif args.generate:
        process_totp_generation(args.key)

if __name__ == "__main__":
    main()

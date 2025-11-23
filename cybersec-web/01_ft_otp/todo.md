### argument handling:
- [x] use argparse + assert
- [x] only -k or -g | else -> print error
- [x] + only one key file argument | else -> print error

### key validation. key must be:
- [x] read from file in binary mode | catch exceptions
- [x] contain only hex digits (0–9, A–F, a–f) | else -> print error
- [x] exactly 64 hexadecimal characters | else -> print error

### key encryption -g:
- [x] derive encryption key from .env
- [x] encrypt original 64-hex key using AES-GCM
- [x] save encrypted data to ft_otp.key
- [x] print: “Key was successfully saved in ft_otp.key.”

### key decription -k:
- [x] load encrypted file ft_otp.key
- [x] decript via AES-GCM

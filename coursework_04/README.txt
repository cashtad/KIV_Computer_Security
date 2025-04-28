So the program is relatively simple compared to the previous ones. Program is divided into four modules, each one
does its own function.
Modules:
    ---sign.py -> main module, controls everything and runs other modules
    ---hash.py -> module contains only one function to make hash print of a text. Function is imported from hashlib and returns 32 byte array
    ---coder.py -> module contains all parts of el graham algorithm
            ---encrypt_bytes(plaintext_bytes)
                works with byte array of hashprint of plaintext. amount of bytes should be exactly 32, not less, not more.
                first step is to convert byte array to big int
                second step is to load values from .txt files. if there are none of them, it will generate them randomly
                third step is to encrypt message
            ---generate_keys()
                randomly generates all values for keys and then exports them into files
            ---elgamal_encrypt(m,p,g,y)
                encrypts message
    ---decoder.py -> decodes encrypted message. returns array of bytes

Program is working, tested and verified. After each encoding it automatically decodes the result and compares it with source
hash print. Rapid.

There are some limits:
1) Works only with text which is initialized directly in code
2) If there are already files with key values, they won't be generated again
3) Values in signature.txt are stored in format a\nb format
4) 

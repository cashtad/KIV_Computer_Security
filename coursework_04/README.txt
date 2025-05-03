The program implements a basic digital signature system using the ElGamal signature scheme. It consists of four main modules, each responsible for a specific part of the process.
Modules:
    ---sign.py -> main module, controls everything and runs other modules
            ---Hashes the input string using SHA-256
            ---Signs the hash using ElGamal signature (via coder.py)
            ---Saves the signature to signature.txt
            ---Verifies the signature using public key and ElGamal logic (via decoder.py).
    ---hash.py -> module contains only one function to make hash print of a text. Function is imported from hashlib and returns 32 byte array
    ---coder.py -> implements the signing part of the ElGamal algorithm
            ---sign_hash(hash_bytes)
                 takes a SHA-256 hash in bytes and returns a signature pair (a, b). It converts the hash to an integer and signs it using the private key x
            ---generate_keys()
                generates ElGamal parameters (p, g, x, y) and stores them in files
    ---decoder.py -> Implements verification of the ElGamal digital signature
            ---verify_signature(a, b, hash_bytes) — returns True if the signature is valid for the given hash

Program is working, tested and verified. After each encoding it automatically decodes the result and compares it with source
hash print. Rapid.

Signature Format:
    File signature.txt stores two decimal values:
        -a
        -b
    where (a, b) is the ElGamal signature pair.

There are some limits:
1) Works only with text which is initialized directly in code
2) If there are already files with key values, they won't be generated again
3) Values in signature.txt are stored in format a\nb format

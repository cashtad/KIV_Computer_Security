def load_hex(filename):
    with open(filename, 'r') as f:
        return int(f.read().strip(), 16)


# Inversed element
def modinv(a, p):
    return pow(a, -1, p)


# Decryption
def elgamal_decrypt(a, b, p, x):
    s = pow(a, x, p)
    s_inv = modinv(s, p)
    m = (b * s_inv) % p
    return m


def decrypt_pair(a, b):
    p = load_hex('p.txt')
    x = load_hex('x.txt')

    m = elgamal_decrypt(a, b, p, x)

    plaintext_bytes = m.to_bytes(32, byteorder='big')
    return plaintext_bytes

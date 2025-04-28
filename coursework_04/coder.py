import secrets


def save_hex(filename, value):
    with open(filename, 'w') as f:
        f.write(hex(value)[2:])  # save without '0x'


def load_hex(filename):
    with open(filename, 'r') as f:
        return int(f.read().strip(), 16)


# Quick check for primeness. Doesn't guarantee, but works mostly fine
def is_prime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Generates new keys and saves them into files.
def generate_keys():
    while True:
        p = secrets.randbits(256)
        p |= (1 << 255) | 1  # makes p uneven
        if is_prime(p):
            break

    g = secrets.randbelow(p - 2) + 2
    x = secrets.randbelow(p - 2) + 1
    y = pow(g, x, p)

    save_hex('p.txt', p)
    save_hex('g.txt', g)
    save_hex('x.txt', x)
    save_hex('y.txt', y)

    return p, g, x, y


# Encryption
def elgamal_encrypt(m, p, g, y):
    k = secrets.randbelow(p - 2) + 1
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return a, b


# Main encryption function
def encrypt_bytes(plaintext_bytes):
    if len(plaintext_bytes) != 32:
        raise ValueError("Input must be exactly 32 bytes.")

    m = int.from_bytes(plaintext_bytes, byteorder='big')

    try:
        p = load_hex('p.txt')
        g = load_hex('g.txt')
        y = load_hex('y.txt')
    except FileNotFoundError:
        p, g, x, y = generate_keys()

    while True:
        try:
            if m >= p:
                raise ValueError("Message is too large for the current prime. Regenerate keys.")
            else:
                break
        except ValueError:
            p, g, x, y = generate_keys()

    a, b = elgamal_encrypt(m, p, g, y)
    return a, b

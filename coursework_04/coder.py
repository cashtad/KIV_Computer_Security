import math
import secrets


def save_hex(filename, value):
    with open(filename, 'w') as f:
        f.write(hex(value)[2:])


def load_hex(filename):
    with open(filename, 'r') as f:
        return int(f.read().strip(), 16)


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
        if x in (1, n - 1):
            continue
        for __ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_keys():
    while True:
        p = secrets.randbits(256)
        p |= (1 << 255) | 1  # Установим старший бит и сделаем p нечетным
        if is_prime(p):
            break

    g = secrets.randbelow(p - 2) + 2
    x = secrets.randbelow(p - 2) + 1
    y = pow(g, x, p)

    save_hex("p.txt", p)
    save_hex("g.txt", g)
    save_hex("x.txt", x)
    save_hex("y.txt", y)

    return p, g, x, y


def sign_hash(hash_bytes):
    if len(hash_bytes) != 32:
        raise ValueError("Hash must be 32 bytes (256 bits) long.")

    m = int.from_bytes(hash_bytes, byteorder="big")

    try:
        p = load_hex("p.txt")
        g = load_hex("g.txt")
        x = load_hex("x.txt")
    except FileNotFoundError:
        p, g, x, _ = generate_keys()

    while m >= p:
        p, g, x, _ = generate_keys()

    while True:
        k = secrets.randbelow(p - 2) + 1
        if math.gcd(k, p - 1) == 1:
            break

    a = pow(g, k, p)
    k_inv = pow(k, -1, p - 1)
    b = (k_inv * (m - x * a)) % (p - 1)

    return a, b

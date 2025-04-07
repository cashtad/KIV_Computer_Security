import math
import random
import secrets

from coursework_03 import decoder


def generate_and_save_public_key(filename, e, n):
    return

def generate_and_save_private_key(filename, d, n):
    return

def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def xgcd(a, b, s1=1, s2=0, t1=0, t2=1):

    if (b == 0):
        return abs(a), 1, 0

    q = math.floor(a / b)
    r = a - q * b
    s3 = s1 - q * s2
    t3 = t1 - q * t2

    # if r==0, then b will be the gcd and s2, t2 the Bezout coefficients
    return (abs(b), s2, t2) if (r == 0) else xgcd(b, r, s2, s3, t2, t3)

def multinv(b, n):
    # Get the gcd and the second Bezout coefficient (t)
    # from the Extended Euclidean Algorithm. (We don't need s)
    my_gcd, _, t = xgcd(n, b)

    # It only has a multiplicative inverse if the gcd is 1
    if (my_gcd == 1):
        return t % n
    else:
        raise ValueError('{} has no multiplicative inverse modulo {}'.format(b, n))

def generate_numbers():
    e = 17
    n = 0
    q = 0
    p = 0
    while True:
        while n < 10000000000000000:
            p = secrets.randbelow(1000000000)
            q = secrets.randbelow(1000000000)
            if p * q < 10000000000000000:
                continue
            if miller_rabin(p, 40):
                if miller_rabin(q, 40):
                    n = p * q
        x = (p - 1) * (q - 1)
        try:
            d = multinv(e, x)
            print(f"q = {q}\np = {p}\nn = {n}\nx = {x}\nd = {d}")
            return d,e,n
        except ValueError:
            pass

def code(data_blocks):
    d,e,n = generate_numbers()

    cypher_text = ""

    for block in data_blocks:
        number = int(block)
        result = pow(number, e) % n
        binary_str = bin(result)[2:].zfill(64)
        decoded = decoder.decode_block(binary_str,d, n)
        print(f"{block} -> {binary_str} -> {decoded}")


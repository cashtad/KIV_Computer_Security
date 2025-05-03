def load_hex(filename):
    with open(filename, 'r') as f:
        return int(f.read().strip(), 16)


def verify_signature(hash_bytes, a, b):
    p = load_hex("p.txt")
    g = load_hex("g.txt")
    y = load_hex("y.txt")

    m = int.from_bytes(hash_bytes, byteorder="big")

    left = pow(g, m, p)
    right = (pow(y, a, p) * pow(a, b, p)) % p

    return left == right

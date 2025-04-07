import random
import secrets

from tqdm import tqdm


# Function to check if number is prime (NOT GUARANTEED)
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


# Function is needed to generate random values for keys
def generate_numbers():
    e = 65537
    n = 0
    q = 0
    p = 0
    KEY_SIZE = 2048  # бит
    while True:

        p_is_even = False
        q_is_even = False

        while not p_is_even:
            p = secrets.randbits(KEY_SIZE // 2)
            if miller_rabin(p, 40):
                p_is_even = True

        while not q_is_even:
            q = secrets.randbits(KEY_SIZE // 2)
            if miller_rabin(q, 40):
                q_is_even = True

        n = p * q
        x = (p - 1) * (q - 1)
        try:
            d = pow(e, -1, x)

            break
        except ValueError:
            pass
    return d, e, n


# Saves keys to separate files
def save_keys(d, e, n):
    with open("priv_key.txt", "w") as file:
        text = f"d={hex(d)[2:]}\nn={hex(n)[2:]}"
        file.write(text)
        print("Private key saved to priv_key.txt")
    with open("pub_key.txt", "w") as file:
        text = f"e={hex(e)[2:]}\nn={hex(n)[2:]}"
        file.write(text)
        print("Public key saved to pub_key.txt")


# Main function for coding
# 1) Generates numbers for keys
# 2) Saves keys in separated files
# 3) Block-by-block encrypting then appending to file in binary format
def code(data_blocks, encoded_filename):
    BLOCK_SIZE_OUT = 256
    d, e, n = generate_numbers()

    save_keys(d, e, n)

    with open(encoded_filename, "ab") as file:
        for block in tqdm(data_blocks, desc="Encrypting...", unit="blocks"):
            number = int.from_bytes(block, byteorder='big')
            coded_number = pow(number, e, n)
            coded_bytes = coded_number.to_bytes(BLOCK_SIZE_OUT, byteorder='big')
            file.write(coded_bytes)

import coder
import decoder
import hash


def save_signature(a, b, filename):
    with open(filename, "w") as f:
        f.write(f"{a}\n{b}")


def load_signature(filename):
    with open(filename, "r") as f:
        a = int(f.readline())
        b = int(f.readline())
        return a, b


def dec_to_hex(dec_value):
    hex_value = hex(dec_value)[2:]
    return hex_value.zfill(64)


if __name__ == '__main__':
    student_id = "A22B0387P"
    hashed = hash.hash_text(student_id)

    print(f"{hashed.hex()} <- Hashed text before signing")

    a, b = coder.sign_hash(hashed)

    print(f"a hex: {dec_to_hex(a)}")
    print(f"a dec: {a}")
    print(f"b hex: {dec_to_hex(b)}")
    print(f"b dec: {b}")

    save_signature(a, b, "signature.txt")

    # Verification
    a, b = load_signature("signature.txt")
    is_valid = decoder.verify_signature(hashed, a, b)

    if is_valid:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")

import coder
import decoder
import hash


def save_a_b_to_file(a, b, filename):
    with open(filename, "w") as text_file:
        text_file.write(str(a) + "\n")
        text_file.write(str(b))

def load_a_b_from_file(filename):
    with open(filename, "r") as text_file:
        a = text_file.readline()
        b = text_file.readline()
        return int(a),int(b)


def dec_to_hex(dec_value):
    hex_value = hex(dec_value)[2:]
    if len(hex_value) < 64:
        while len(hex_value) < 64:
            hex_value = "0" + hex_value
    return hex_value


if __name__ == '__main__':
    text = "A22B0387P"
    hashed_text = hash.hash_text(text)

    print(f"{hashed_text.hex()} <- Hashed text before encryption")

    a, b = coder.encrypt_bytes(hashed_text)

    print(f"a hex: {dec_to_hex(a)}")
    print(f"a dec: {a}")
    print(f"b hex: {dec_to_hex(b)}")
    print(f"b dec: {b}")



    save_a_b_to_file(a, b, "signature.txt")


    a,b = load_a_b_from_file("signature.txt")

    plain_bytes = decoder.decrypt_pair(a, b)

    print(f"{plain_bytes.hex()} <- Hashed text after decryption")

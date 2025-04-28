import coder
import decoder
import hash


# Saves encrypted values to file. Values are split by '\n'
def save_a_b_to_file(a, b, filename):
    with open(filename, "w") as text_file:
        text_file.write(str(a) + "\n")
        text_file.write(str(b))


# Loads encrypted values from a file. Values are required to be split by '\n'
def load_a_b_from_file(filename):
    with open(filename, "r") as text_file:
        a = text_file.readline()
        b = text_file.readline()
        return int(a), int(b)


# Converts dec number to hex representation. Fills it with 0's at the start to be 64 chars length
def dec_to_hex(dec_value):
    hex_value = hex(dec_value)[2:]
    if len(hex_value) < 64:
        while len(hex_value) < 64:
            hex_value = "0" + hex_value
    return hex_value


# Main function
if __name__ == '__main__':
    # Student number
    text = "A22B0387P"
    # SHA-256 hash generation in bytes
    hashed_text = hash.hash_text(text)
    print(f"{hashed_text.hex()} <- Hashed text before encryption")

    # Encrypted values
    a, b = coder.encrypt_bytes(hashed_text)

    print(f"a hex: {dec_to_hex(a)}")
    print(f"a dec: {a}")
    print(f"b hex: {dec_to_hex(b)}")
    print(f"b dec: {b}")

    # Exports encrypted values to a file
    save_a_b_to_file(a, b, "signature.txt")

    # ----------------VERIFICATION BLOCK----------------

    # Reads encrypted values from a file
    a, b = load_a_b_from_file("signature.txt")

    # Decrypts values into plain text
    plain_bytes = decoder.decrypt_pair(a, b)

    print(f"{plain_bytes.hex()} <- Hashed text after decryption")

    if plain_bytes.hex() == hashed_text.hex():
        print("Signature is valid, hash is the same as before encryption.")
    else:
        print("Signature is invalid, hash is different than before encryption.")

import os

from tqdm import tqdm


# Decodes one single block of encrypted file
def decode_block(block, d, n):
    BLOCK_SIZE_IN = 32
    number = int(block, 2)
    decoded = pow(number, d, n)

    return decoded.to_bytes(BLOCK_SIZE_IN, byteorder='big')


# Main function for decoding. Creates new decrypted file, then provides block-by-block decryption
def decode(encoded_filename, decoded_filename, d, n):
    BLOCK_SIZE_IN = 256  # 2048 bits = 256 bytes

    file_size = os.path.getsize(encoded_filename)
    total_blocks = file_size // BLOCK_SIZE_IN

    with open(encoded_filename, "rb") as encrypted_file, open(decoded_filename, "wb") as decrypted_file:
        for _ in tqdm(range(total_blocks), desc="Decrypting", unit="blocks"):
            block = encrypted_file.read(BLOCK_SIZE_IN)
            number = int.from_bytes(block, byteorder='big')
            decoded = pow(number, d, n)
            decrypted_file.write(decoded.to_bytes(32, byteorder='big'))

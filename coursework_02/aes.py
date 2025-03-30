import os
import sys

import coder, decoder


def generate_and_save_key(filename):
    key = os.urandom(16)  # Generates 16 pseudo-random bytes

    output = ""  # This text will be written to file
    output_numbers = []  # This array will go to the key expansion function
    for i in range(len(key)):
        text = hex(key[i])[2:]
        if len(text) == 1:
            text = "0" + text
        output += text
        number = int(text, 16)
        output_numbers.append(number)

    with open(filename, 'w') as file:
        file.write(output)
    print(f"AES key generated and saved: {output}")
    return output_numbers


def read_key(filename):
    with open(filename, 'r') as file:
        hex_key = file.read()
        result = []
        for i in range(int(len(hex_key) / 2)):
            text = "0x" + hex_key[2 * i] + hex_key[2 * i + 1]
            number = int(text, 16)
            result.append(number)
    return result


if __name__ == "__main__":
    validation_folder = "validation"
    encoded_folder = ""
    decoded_folder = ""
    key_filename = "aes_key.txt"  # Filename for key read/write

    file_ext = "csv"  # Input file for encoding must be with this extension
    enc_file_ext = "aes"  # Extension for encoded files

    if len(sys.argv) < 3:
        exit(code="Usage: python3 aes.py <mode> <filename>")

    if sys.argv[1] == "-e":  # Encryption mode

        key = generate_and_save_key(key_filename)

        filename = sys.argv[2].split("/")[-1]
        file_input_name = os.path.join(sys.argv[2])
        file_input_name_main = filename.split(".")[0]
        file_input_name_ext = filename.split(".")[1]

        if file_input_name_ext != file_ext:
            exit(code="Usage: python3 aes.py -e <filename.csv>")

        encoded_filename = encoded_folder + file_input_name_main + "." + enc_file_ext

        data = coder.code(file_input_name, key)

        with open(encoded_filename, "wb") as file:
            file.write(data)

        print(f"Successfully encoded: {sys.argv[2]} -> {encoded_filename}")

    elif sys.argv[1] == "-d":  # Dectyption mode
        filename = sys.argv[2].split("/")[-1]
        filename_ext = filename.split(".")[1]

        if filename_ext != enc_file_ext:
            exit(code="Usage: python3 aes.py -d <filename.aes>")

        key = read_key(key_filename)

        data = decoder.decode(sys.argv[2], key)

        decoded_filename = decoded_folder + filename.split(".")[0] + ".csv"

        with open(decoded_filename, "wb") as file:
            file.write(data)

        print(f"Successfully decoded: {sys.argv[2]} -> {decoded_filename}")

    else:
        exit(code="Usage: python3 aes.py <mode (-e/-d)> <filename>")

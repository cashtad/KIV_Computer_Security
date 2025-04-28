import os
import sys

import coder
import decoder


# Function to read plain text from file
def read_plain_text(filename):
    BLOCK_SIZE_IN = 32
    blocks = []
    try:
        with open(filename, 'rb') as f:
            while block := f.read(BLOCK_SIZE_IN):  # Split file to blocks
                blocks.append(block)
        return blocks
    except FileNotFoundError:
        print("File to encrypt found")


# Read values for private key from file
def read_priv_key(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
            parts = text.split('=')
            d = int("0x" + parts[1][:-2], 16)
            n = int("0x" + parts[2], 16)
            return d, n
    except FileNotFoundError:
        exit("File with key was not found")


if __name__ == "__main__":

    private_key_filename = "priv_key.txt"  # Private key filename
    public_key_filename = "pub_key.txt"  # Public key filename

    file_ext = "csv"  # Input file for encoding must be with this extension
    enc_file_ext = "rsa"  # Extension for encoded files

    if len(sys.argv) < 3:
        exit(code="Usage: python3 rsa.py <mode> <filename>")

    if sys.argv[1] == "-e":

        filename = sys.argv[2].split("/")[-1]
        file_input_name = os.path.join(sys.argv[2])
        file_input_name_main = filename.split(".")[0]
        file_input_name_ext = filename.split(".")[1]

        if file_input_name_ext != file_ext:
            exit(code="Usage: python3 rsa.py -e <filename.csv>")

        encoded_filename = file_input_name_main + "_" + file_input_name_ext + "." + enc_file_ext

        data = read_plain_text(file_input_name)  # Read data from plain file

        #   Creation of enc file
        with open(encoded_filename, 'w') as f:
            f.write("")

        coder.code(data, encoded_filename)  # Encrypt then write data to file

        print("Successfully encoded to: " + encoded_filename)

    elif sys.argv[1] == "-d":

        filename = sys.argv[2].split("/")[-1]
        filename_ext = filename.split(".")[1]

        plainfile_ext = filename.split("_")[1].split('.')[0]
        plainfile_name = filename.split("_")[0]

        if filename_ext != enc_file_ext:
            exit(code="Usage: python3 rsa.py -d <filename.rsa>")

        d, n = read_priv_key(private_key_filename)  # Read value for decoding

        decoded_filename = plainfile_name + "." + plainfile_ext

        data = decoder.decode(filename, decoded_filename, d, n)  # Block-by-block decoding then writing to file

        print("Successfully decoded to: " + decoded_filename)

    else:
        exit(code="Usage: python3 rsa.py <mode (-e/-d)> <filename>")

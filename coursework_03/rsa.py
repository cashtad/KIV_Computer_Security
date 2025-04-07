import sys

from coursework_03 import coder

def read_plain_text(filename):
    BLOCK_SIZE = 5
    blocks = []
    with open(filename, 'r') as file:
        input = file.read()
        data = ""
        counter = 0
        for char in input:
            value = ord(char)
            if counter == 0:
                value += 100
            if value < 100:
                value = "0" + str(value)
            else:
                value = str(value)

            data += value
            counter += 1

            if counter == BLOCK_SIZE:
                blocks.append(int(data))
                data = ""
                counter = 0
    return blocks



if __name__ == "__main__":

    private_key_filename = "priv_key.txt"
    public_key_filename = "pub_key.txt"

    enc_file_ext = "rsa"

    if len(sys.argv) < 3:
        exit(code="Usage: python3 rsa.py <mode> <filename>")

    if sys.argv[1] == "-e":
        data = read_plain_text("validation/customers-20.csv")
        coder.code(data)
        print("Encrypting...")

    elif sys.argv[1] == "-d":
        print("Decrypting...")
    else:
        exit(code="Usage: python3 rsa.py <mode (-e/-d)> <filename>")

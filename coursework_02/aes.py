import os
import sys
import binascii


from coursework_02 import coder, decoder


def generate_and_save_key(filename="aes_key.txt"):
    key = os.urandom(16)  # Генерируем 16 случайных байтов (128 бит)
    output = ""
    output_numbers = []
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
    # Чтение содержимого файла
    with open(filename, 'r') as file:
        hex_key = file.read()
        result = bytearray()
        for i in range(int(len(hex_key) / 2)):
            text = "0x" + hex_key[2*i] + hex_key[2*i+1]
            number = int(text, 16)
            result.append(number)
    return result


if __name__ == "__main__":
    validation_folder = "validation"
    encoded_folder = "encoded/"
    decoded_folder = "decoded/"
    key_filename = "aes_key.txt"


    file_ext = "csv"


    name_of_file_encrypted = ""

    if len(sys.argv) < 3:
        exit(code="Usage: python3 aes.py <mode> <filename>")
    if sys.argv[1] == "-e":
        key = generate_and_save_key()

        filename_args = sys.argv[2]
        filename = filename_args.split("/")[-1]
        file_input_name = os.path.join(filename_args)
        file_input_name_main = filename.split(".")[0]
        file_input_name_ext = filename.split(".")[1]

        if file_input_name_ext != file_ext:
            exit(code="Usage: python3 aes.py -e <filename.csv>")

        file_encoded_ext = "aes"

        encoded_filename = os.path.join(encoded_folder,
                                        file_input_name_main + "." + file_encoded_ext)

        data = coder.code(file_input_name, key)

        with open(encoded_filename, "wb") as file:
            file.write(data)

        print(f"Successfully encoded: {filename_args} -> {encoded_filename}")
    if sys.argv[1] == "-d":
        filename_args = sys.argv[2]
        filename = filename_args.split("/")[-1]
        key = read_key(key_filename)

        data = decoder.decode(filename_args,key)

        decoded_filename = filename.split(".")[0] + ".csv"

        with open(decoded_filename, "wb") as file:
            file.write(data)

        print(f"Successfully decoded: {filename_args} -> {decoded_filename}")

    # for filename in os.listdir(validation_folder):
    #
    #     file_input_name = os.path.join(validation_folder, filename)
    #     file_input_name_main = filename.split(".")[0]
    #     file_input_name_ext = filename.split(".")[1]
    #
    #     if file_input_name_ext != file_ext:
    #         print(f"Wrong extension of file: {file_input_name}")
    #         continue
    #
    #     file_encoded_ext = "aes"
    #
    #     encoded_filename = os.path.join(encoded_folder,
    #                                     file_input_name_main + "." + file_encoded_ext)
    #
    #     data = coder.code(file_input_name, key)
    #
    #     with open(encoded_filename, "wb") as file:
    #         file.write(data)
    #
    #     decoded_filename = os.path.join(decoded_folder, file_input_name + "_decoded." + file_ext)
    #
    #
    #
    #     print(f"Processed {filename}\n\n")

    # dec
    # -d
    name_of_file_decrypted = ""

    # comparison

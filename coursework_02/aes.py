import os

from coursework_02 import coder


def generate_and_save_key():
    key = os.urandom(16)  # Генерируем 16 случайных байтов
    hex_key = key.hex()  # Преобразуем в шестнадцатеричный формат
    with open("aes_key.txt", "w") as file:
        file.write(hex_key)  # Сохраняем в текстовом виде
    print("AES ключ сохранён в aes_key.txt:", hex_key)
    return key


validation_folder = "validation"
encoded_folder = "encoded/"
decoded_folder = "decoded/"

# rand key
# 128 bits
# to aes_key.txt file
# in hex format
key = generate_and_save_key()

# search of file
# array of bytes
file_ext = "csv"

# enc
# -e
# Electronic Code Book (ECB)
# length of block is 128 bits
# progressbar
# 10 iterations
# cache
name_of_file_encrypted = ""

# dec
# -d
name_of_file_decrypted = ""

# comparision

for filename in os.listdir(validation_folder):

    file_input_name = os.path.join(validation_folder, filename)
    file_input_name_main = filename.split(".")[0]
    file_input_name_ext = filename.split(".")[1]

    if file_input_name_ext != file_ext:
        print(f"Wrong extension of file: {file_input_name}")

    encoded_filename = os.path.join(encoded_folder,
                                    file_input_name_main + "_encoded" + "." + file_ext)

    data = coder.code(file_input_name, key)

    with open(encoded_filename, "wb") as file:
        file.write(data)

    decoded_filename = os.path.join(decoded_folder, file_input_name + "_decoded." + file_ext)



    print(f"Processed {filename}\n\n")

import os

from coursework_01 import coder, decoder

if __name__ == "__main__":
    file_medium_firstname = "weber"
    file_medium_ext = "bmp"
    file_medium_name = file_medium_firstname + "." + file_medium_ext

    validation_folder = "validation"
    output_folder = "out"
    decoded_folder = "decoded"

    for filename in os.listdir(validation_folder):

        file_input_name = os.path.join(validation_folder, filename)
        file_input_name_main = filename.split(".")[0]
        file_input_name_ext = filename.split(".")[1]

        output_filename = os.path.join(output_folder,
                                       file_input_name_main + "___" + file_medium_firstname + "." + file_medium_ext)
        decoded_filename = os.path.join(decoded_folder, file_input_name_main + "." + file_input_name_ext)

        try:
            data_output = coder.code(file_input_name, file_medium_name)
        except:
            print("File " + decoded_filename + " could not be decoded")
            continue


        with open(output_filename, "wb") as file:
            file.write(data_output)

        data_decoded = decoder.decode(output_filename)
        with open(decoded_filename, "wb") as file:
            file.write(data_decoded)


        print(f"Processed {filename}\n\n")

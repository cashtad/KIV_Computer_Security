def code(file_input_name, file_medium_name):
    with open(file_medium_name, "rb") as file_medium:
        data_medium = file_medium.read()
        print(f"Opened {file_medium_name}")

    with open(file_input_name, "rb") as file_input:
        data_input = bytearray(file_input.read())
        print(f"Opened {file_input_name}")

    if len(data_input) * 8 > len(data_medium) - int.from_bytes(data_medium[10:14], byteorder='little'):
        raise Exception("Data is too long to put it in medium")

    output_data = code_bmp(data_input, data_medium)


    return output_data


def code_bmp(data_input, data_medium):
    print("Hiding data in BMP file...")

    output_data = bytearray()

    offset_medium = int.from_bytes(data_medium[10:14], byteorder='little')  # where to start

    index_input = 0


    data_input.append(0)
    data_input.append(127)
    data_input.append(0)
    data_input.append(127)


    for i in range(len(data_medium)):
        if i <= offset_medium or index_input >= len(data_input) * 8:  # just copying bytes before the offset
            output_data.append(data_medium[i])
            continue

        byte_medium = data_medium[i]  # byte from medium to be changed

        # collecting a bit from input file
        byte_input_temp = data_input[index_input // 8]
        bit_input = (byte_input_temp >> 8 - index_input % 8 - 1) & 1

        # putting the bit from input file to byte from medium
        new_byte = (byte_medium & ~1) | bit_input

        output_data.append(new_byte)

        index_input += 1

    print("Hiding finished")
    return output_data

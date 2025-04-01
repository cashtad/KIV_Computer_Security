def extract_hidden_message(bmp_file):
    with open(bmp_file, "rb") as f:
        bmp_data = bytearray(f.read())

    pixel_data_offset = int.from_bytes(bmp_data[10:14], byteorder='little')  # where to start
    hidden_bits = []
    hidden_message = ""

    # TODO: Какая то иная манипуляция с байтами
    for byte in bmp_data[pixel_data_offset:]:
        hidden_bits.append(str(byte & 1))  # list of end bits
        if len(hidden_bits) == 8:
            char = chr(int("".join(hidden_bits), 2))
            hidden_message += char
            hidden_bits.clear()
            if char == '\n':
                break

    return hidden_message


if __name__ == "__main__":
    bmp_file = "obr2.bmp"
    message = extract_hidden_message(bmp_file)
    print("Hidden message:", message)

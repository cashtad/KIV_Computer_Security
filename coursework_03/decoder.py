def decode(data, d, n):
    decoded_data = ""
    for block in data:
        result = str(decode_block(block, d, n))
        char1 = result[:2]
        char2 = result[3:5]
        char3 = result[6:8]

        dec1 = int(char1) - 100
        decoded_data += chr(dec1) + chr(int(char2)) + chr(int(char3))



def decode_block(block, d, n):
    i = 0
    splitted = ""
    while True:
        if block[i] == "1":
            splitted = "0b" + block[i:]
            break
        else:
            i += 1
    number = int(splitted, 2)

    decoded = pow(number, d, n)
    return decoded



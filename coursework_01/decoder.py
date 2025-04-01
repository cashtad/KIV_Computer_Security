class FixedSizeList:
    def __init__(self, size):
        self.size = size  # Размер списка
        self.data = []  # Список для хранения элементов

    def add(self, element):
        if len(self.data) >= self.size:
            self.data.pop(0)  # Удаляем старейший элемент
        self.data.append(element)  # Добавляем новый элемент

    def __repr__(self):
        return f"FixedSizeList({self.data})"


def decode(filename):
    print("Decoding started...")

    with open(filename, 'rb') as f:
        bmp_data = bytearray(f.read())

    # from which place to start collecting bits
    offset = int.from_bytes(bmp_data[10:14], byteorder='little')  # where to start

    output_data = bytearray()

    byte_temp = 0
    counter = 0

    temp_array = FixedSizeList(4)

    # starting from offset to all over the end of file
    for i in range(offset + 1, len(bmp_data)):

        # byte to be inspected
        byte = bmp_data[i]

        # collecting last bit from the byte
        bit_input = byte & 1

        # constructing new byte from single bits
        byte_temp = (byte_temp << 1) | (bit_input & 1)
        counter += 1

        # if byte is constructed, start all over again and put the byte into output byte array

        if counter == 8:
            temp_array.add(byte_temp)
            if temp_array.data == [0, 127, 0, 127]:
                output_data.pop()
                output_data.pop()
                output_data.pop()
                print("Decoding complete")
                return output_data

            output_data.append(byte_temp)
            counter = 0
            byte_temp = 0

    print("Decoding complete")

    return output_data

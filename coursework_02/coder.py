from tqdm import tqdm

import tables


def key_expansion(key):
    expanded_keys = list()
    expanded_keys.append([key[i:i + 4] for i in range(0, len(key), 4)])

    for round_num in range(0, 10):
        prev_key = expanded_keys[-1]
        new_key = []
        for i in range(len(prev_key)):
            new_key.append([])
            for j in range(len(prev_key)):
                new_key[i].append(prev_key[i][j])

        # First column of new key
        temp = [new_key[0][3], new_key[1][3], new_key[2][3], new_key[3][3]]
        temp = temp[1:] + temp[:1]  # Cykle shift
        temp = [tables.sbox[b >> 4][b & 0x0F] for b in temp]  # Sbox change
        for i in range(len(temp)):
            temp[i] ^= tables.rcon[round_num][i]
        for i in range(4):
            new_key[i][0] = prev_key[i][0] ^ temp[i]

        # Other column generated simply by xor operations with previous key
        for i in range(4):
            for j in range(1, 4):
                new_key[i][j] = new_key[i][j - 1] ^ prev_key[i][j]

        expanded_keys.append(new_key)
    return expanded_keys


# Simple xor operation for each value of state matrix with round key
def add_round_key(matrix, round_key):
    return [[matrix[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]


# Main function of coder
def code(filename, key):
    data = read_file(filename)  # Read data from file
    key_schedule = key_expansion(key)  # Expand key into 11 keys
    encrypted_data = bytearray()  # Encrypted data array initialization

    num_blocks = len(
        data) // 16  # Amount of blocks to be processed. Plain file should be ended with full block of information

    with tqdm(total=num_blocks, desc="Encrypting", unit="block") as pbar:
        for i in range(0, len(data), 16):
            block = data[i:i + 16]  # Retrieving a single block

            # Restructuring block into state matrix
            state = []
            for row in range(4):
                state.append([])
                for col in range(4):
                    state[row].append(block[(4 * row + col)])

            # Applying first round key
            state = add_round_key(state, key_schedule[0])

            # 10 main rounds
            for round_num in range(1, 11):
                state = subbytes(state)
                state = shiftrows(state)
                if round_num != 10:
                    state = mixcolumns(state)  # Will not be applied in the last round
                state = add_round_key(state, key_schedule[round_num])

            # Append information into encrypted array
            for row in range(4):
                for col in range(4):
                    encrypted_data.append(state[row][col])

            pbar.update(1)  # Progress bar update

    return encrypted_data


def subbytes(matrix):
    for i in range(4):
        for j in range(4):
            row_idx = matrix[i][j] >> 4  # Row index
            col_idx = matrix[i][j] & 0x0F  # Column index
            matrix[i][j] = tables.sbox[row_idx][col_idx]  # Changing value of byte to sbox value
    return matrix


def mixcolumns(matrix):
    # Function for multiplying
    def gmul(a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11B
            b >>= 1
        return result

    new_state = [[0] * 4 for _ in range(4)]

    #  Mixcolumns
    for i in range(4):
        for j in range(4):
            value = 0
            for k in range(4):
                value ^= gmul(tables.mix_matrix[j][k], matrix[k][i])
            new_state[j][i] = value

    return new_state


def shiftrows(matrix):
    shift = 0
    for row in matrix:
        for count in range(shift):
            temp = row[len(row) - 1]
            for i in range(len(row)):
                row[len(row) - 1 - i] = row[len(row) - 1 - i - 1]
            row[0] = temp
        shift += 1
    return matrix


def read_file(filename):
    with open(filename, "rb") as file_input:
        data_input = bytearray(file_input.read())
        print(f"Opened {filename}")
    return data_input

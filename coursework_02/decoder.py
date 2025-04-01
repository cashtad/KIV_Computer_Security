from tqdm import tqdm

from coursework_02 import tables


def key_expansion(key):

    expanded_keys = []
    expanded_keys.append([key[i:i + 4] for i in range(0, len(key), 4)])

    for round_num in range(0, 10):
        prev_key = expanded_keys[-1]
        new_key = prev_key.copy()

        temp = new_key[-1]
        temp = temp[1:] + temp[:1]  # Циклический сдвиг
        temp = [tables.sbox[temp[i] >> 4][temp[i] & 0x0F] for i in range(4)]  # S-box замена
        for i in range(len(temp)):
            temp[i] ^= tables.rcon[round_num][i]

        new_key[0] = [prev_key[0][i] ^ temp[i] for i in range(4)]
        for i in range(1, 4):
            new_key[i] = [new_key[i - 1][j] ^ prev_key[i][j] for j in range(4)]

        expanded_keys.append(new_key)

    return expanded_keys[::-1]  # Инвертируем порядок ключей


def add_round_key(matrix, round_key):
    return [[matrix[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]


def decode(filename, key):
    data = read_file(filename)
    key_schedule = key_expansion(key)
    decrypted_data = bytearray()

    num_blocks = len(data) // 16
    with tqdm(total=num_blocks, desc="Decrypting", unit="block") as pbar:
        for i in range(0, len(data), 16):
            block = data[i:i + 16]
            state = [[block[row + col * 4] for col in range(4)] for row in range(4)]

            state = add_round_key(state, key_schedule[0])
            for round_num in range(1, 10):
                state = inv_shiftrows(state)
                state = inv_subbytes(state)
                state = add_round_key(state, key_schedule[round_num])
                if round_num != 9:
                    state = inv_mixcolumns(state)

            decrypted_data.extend([state[row][col] for col in range(4) for row in range(4)])
            pbar.update(1)

    return decrypted_data


def inv_subbytes(matrix):
    for i in range(4):
        for j in range(4):
            row_idx = matrix[i][j] >> 4
            col_idx = matrix[i][j] & 0x0F
            matrix[i][j] = tables.sbox_inv[row_idx][col_idx]
    return matrix


def inv_shiftrows(matrix):
    shift = 0
    for row in matrix:
        for count in range(shift):
            temp = row[0]
            for i in range(len(row) - 1):
                row[i] = row[i + 1]
            row[-1] = temp
        shift += 1
    return matrix


def inv_mixcolumns(matrix):


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
    for i in range(4):
        for j in range(4):
            value = 0
            for k in range(4):
                value ^= gmul(tables.inv_mix_matrix[j][k], matrix[k][i])
            new_state[j][i] = value

    return new_state


def read_file(filename):
    with open(filename, "rb") as file_input:
        data_input = bytearray(file_input.read())
        print(f"Opened {filename}")
    return data_input

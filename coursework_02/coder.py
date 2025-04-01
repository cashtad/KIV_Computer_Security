from tqdm import tqdm

from coursework_02 import tables




def key_expansion(key):

    expanded_keys = []
    expanded_keys.append([key[i:i + 4] for i in range(0, len(key), 4)])

    for round_num in range(0, 10):
        prev_key = expanded_keys[-1]
        new_key = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(len(prev_key)):
            for j in range(len(prev_key)):
                new_key[i][j] = prev_key[i][j]

        # Генерация первой колонки нового ключа
        temp = [new_key[0][3],new_key[1][3],new_key[2][3],new_key[3][3]]
        temp = temp[1:] + temp[:1]  # Циклический сдвиг
        temp = [tables.sbox[b >> 4][b & 0x0F] for b in temp]  # S-box замена
        for i in range(len(temp)):
            temp[i] ^= tables.rcon[round_num][i]
        for i in range(4):
            new_key[i][0] = prev_key[i][0] ^ temp[i]

        # Генерация остальных колонок
        for i in range(4):
            for j in range(1, 4):
                new_key[i][j] = new_key[i][j-1] ^ prev_key[i][j]

        expanded_keys.append(new_key)

    return expanded_keys


def add_round_key(matrix, round_key):
    return [[matrix[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]


def code(filename, key):
    data = read_file(filename)
    key_schedule = key_expansion(key)
    encrypted_data = bytearray()

    num_blocks = len(data) // 16 + (1 if len(data) % 16 != 0 else 0)  # Количество блоков

    with tqdm(total=num_blocks, desc="Encrypting", unit="block") as pbar:
        for i in range(0, len(data), 16):
            state = []
            for row in range(4):
                state.append([])
                for col in range(4):
                    state[row].append(data[4 * row + col])

            # Начальный раундовый ключ
            state = add_round_key(state, key_schedule[0])

            # Основные 9 раундов
            for round_num in range(1, 10):
                state = subbytes(state)
                state = shiftrows(state)
                if round_num != 9:
                    state = mixcolumns(state)
                state = add_round_key(state, key_schedule[round_num])

            # Преобразуем обратно в байтовый массив
            encrypted_data.extend([state[row][col] for col in range(4) for row in range(4)])

            pbar.update(1)  # Обновляем прогресс-бар

    return encrypted_data


#
def subbytes(matrix):
    for i in range(4):
        for j in range(4):
            row_idx = matrix[i][j] >> 4  # Вычисляем номер строки в S-Box
            col_idx = matrix[i][j] & 0x0F  # Вычисляем номер столбца в S-Box
            matrix[i][j] = tables.sbox[row_idx][col_idx]  # Заменяем байт через S-Box
    return matrix



#
def mixcolumns(matrix):
    # Матрица для умножения


    # Функция для умножения с использованием поля Галуа
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

    # Новый список для хранения результата
    new_state = [[0] * 4 for _ in range(4)]

    # Применение операции mixcolumns
    for i in range(4):  # Для каждой колонки
        for j in range(4):  # Для каждого элемента в колонке
            value = 0
            for k in range(4):  # Суммируем элементы
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
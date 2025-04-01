import struct


def left_rotate(x, amount):
    return ((x << amount) | (x >> (8 - amount))) & 0xFF


def F1(x, y, z):
    return (x & y) | ((x ^ 255) & z)


def F2(x, y, z):
    return (x & z) | (y & (z ^ 255))


def F3(x, y, z):
    return x ^ y ^ z



def F4(x, y, z):
    return y ^ (x | (z ^ 255))


def custom_md5(message):
    # Константы
    A, B, C, D = 54, 88, 72, 123
    K = [131, 12, 26, 92]
    rotate_vals = [3, 1, 5, 2]
    funcs = [F2, F1, F4, F3]

    # Преобразование в байты
    message_bytes = message.encode('utf-8')

    count = 0

    # Запуск хэширования
    for byte in message_bytes:
        if count > 0 and count % 4 == 0:
            count = 0
        func = funcs[count]
        K_i = K[count] & 0xFF
        rot = rotate_vals[count]
        temp = (A + func(B, C, D) + byte + K_i) & 0xFF
        temp = left_rotate(temp, rot) & 0xFF
        A, B, C, D = D, temp, B, C  # Правильное обновление
        count += 1


    return f"{A:02x}{B:02x}{C:02x}{D:02x}"


# Пример использования
P = "Kdo implementuje tuto hash funkci, dostane 2 bodiky."
hash_value = custom_md5(P)
print("Hash:", hash_value)

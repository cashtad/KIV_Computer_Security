import random

def load_hex(filename):
    with open(filename, 'r') as f:
        return int(f.read().strip(), 16)

def modinv(a, p):
    """
    @brief Вычисляет обратный элемент a по модулю p.
    @param a Число, для которого ищется обратный элемент.
    @param p Модуль.
    @return Обратный элемент (x такое, что a * x ≡ 1 mod p).
    """
    return pow(a, -1, p)

def elgamal_decrypt(a, b, p, x):
    """
    @brief Расшифровывает сообщение ElGamal по значениям (a, b).
    @param a Первая часть шифротекста.
    @param b Вторая часть шифротекста.
    @param p Простое число (модуль).
    @param x Секретный ключ.
    @return Расшифрованное сообщение в виде целого числа.
    """
    s = pow(a, x, p)
    s_inv = modinv(s, p)
    m = (b * s_inv) % p
    return m

def decrypt_pair(a, b):
    """
    @brief Декодирует зашифрованную пару чисел обратно в 32 байта исходного сообщения.
    @param a Первая часть шифротекста (целое число).
    @param b Вторая часть шифротекста (целое число).
    @return Байтовая строка длиной 32 байта (оригинальный plaintext).
    """
    p = load_hex('p.txt')
    x = load_hex('x.txt')

    m = elgamal_decrypt(a, b, p, x)

    plaintext_bytes = m.to_bytes(32, byteorder='big')
    return plaintext_bytes
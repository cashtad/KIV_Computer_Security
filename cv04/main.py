from itertools import permutations


def read_file(filename):
    """Čte zašifrovaný text ze souboru."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def decrypt_monoalphabetic(ciphertext, key):
    """
    Расшифровывает текст, зашифрованный моноалфавитным шифром.

    :param ciphertext: Зашифрованный текст
    :param key: Словарь, соответствующий заменённым символам
    :return: Расшифрованный текст
    """
    return "".join(key.get(char, char) for char in ciphertext)


def brute_force_decryption(ciphertext, known_plaintext, fixed_mapping):
    """
    Выполняет брутфорс-расшифровку, учитывая известное соответствие символов.

    :param ciphertext: Зашифрованный текст
    :param known_plaintext: Известный фрагмент оригинального текста
    :param fixed_mapping: Словарь с известными заменами символов
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    remaining_chars = [c for c in alphabet if c not in fixed_mapping]
    for perm in permutations(remaining_chars):
        key = fixed_mapping.copy()
        key.update({c: p for c, p in zip(remaining_chars, perm)})
        decrypted = decrypt_monoalphabetic(ciphertext, key)
        if known_plaintext in decrypted:
            print("Найденный ключ:", key)
            print("Расшифрованный текст:", decrypted)
            break

# Пример использования
if __name__ == "__main__":
    cipher_text =  read_file("sifra_1.txt")
    known_text = "na topole nad jezerem sedel vodnik"  # Известный фрагмент расшифрованного текста
    fixed_mapping = {'z': 'a', #
                     'm': 'n', #
                     'w': 'd', #
                     'v': 'e', #
                     'o': 'l', #
                     'l': 'o', #
                     'k': 'p', #
                     'i': 'r', #
                     'g': 't', #
                     'n': 'm', #
                     'a': 'z', #
                     'q': 'j'

                     }  # Известное соответствие букв

    brute_force_decryption(cipher_text, known_text, fixed_mapping)

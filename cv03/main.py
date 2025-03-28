import random


def caesar(input_text, shift):
    min_dec = 97
    max_dec = 122

    result = ""
    result_dec = ""

    for letter in input_text:
        letter_dec = ord(letter)
        letter_new_dec = letter_dec + shift
        if letter_new_dec > max_dec:
            letter_new_dec = letter_new_dec % max_dec + min_dec - 1
        letter_new = chr(letter_new_dec)
        result += letter_new
        result_dec += str(letter_new_dec)

    return result


def monoalphabet(input_text, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    alph_available = "abcdefghijklmnopqrstuvwxyz"

    help = {}
    index = 0
    b_key = 1

    for letter in alph:
        if b_key == 0:
            help[letter] = alph_available[index]
            index += 1
        else:
            help[letter] = key[index]
            temp = alph_available.split(key[index])
            alph_available = temp[0] + temp[1]
            index += 1
            if index == len(key):
                index = 0
                b_key = 0

    print(help)

    result = ""
    result_dec = ""

    for letter in input_text:
        new_letter = help.get(letter)
        result += new_letter
        result_dec += str(ord(new_letter))

    return result


def homophon(input_text, seed):
    random.seed(seed)

    available_dec = []
    for i in range(0, 100 + 1):
        available_dec.append(i)

    alph = "abcdefghijklmnopqrstuvwxyz"

    help = {}

    help["a"] = [8]
    help["b"] = [2]
    help["c"] = [3]
    help["d"] = [4]
    help["e"] = [12]
    help["f"] = [2]
    help["g"] = [2]
    help["h"] = [6]
    help["i"] = [6]
    help["j"] = [1]
    help["k"] = [1]
    help["l"] = [4]
    help["m"] = [2]
    help["n"] = [6]
    help["o"] = [7]
    help["p"] = [2]
    help["q"] = [1]
    help["r"] = [6]
    help["s"] = [6]
    help["t"] = [9]
    help["u"] = [3]
    help["v"] = [1]
    help["w"] = [2]
    help["x"] = [1]
    help["y"] = [2]
    help["z"] = [1]

    for letter in alph:
        amount = help[letter][0]
        numbers = []
        for i in range(amount):
            index = random.randint(0, len(available_dec) - 1)
            numbers.append(available_dec[index])
            available_dec.remove(available_dec[index])
        help[letter] = numbers

    result = ""

    for letter in input_text:
        possible_numbers = help[letter]
        number = random.choice(possible_numbers)

        result += str(number)

    return result


if __name__ == "__main__":
    input = "zeptaslisebudespetminutvypadatjakoblbecnezeptaslisebudesblbcempocelyzivot"

    result = monoalphabet(input, "o")

    print(result)

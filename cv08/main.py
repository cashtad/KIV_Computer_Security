import hashlib


def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()


def md5_hash(filename):
    data = read_file(filename)
    result = hashlib.md5(data).hexdigest()
    print(f"Mdhash {filename}: {result}")

def sha1_hash(filename, hash):
    data = read_file(filename)

    result = hashlib.sha1(data).hexdigest()
    print(f"Sha1 {filename}: {result}")
    if result != hash:
        print(f"{result} != {hash}")
    else:
        print("Hash was generated with sha1 and is in same condition")


def multi_hash(filename, hash):
    data = read_file(filename)
    result_md5 = hashlib.md5(data).hexdigest()

    print(f"Length of data from file: {len(data)}")
    print(f"Length of hash: {len(hash)}")

    result = hashlib.md5(data).hexdigest()
    print(f"md5 {filename}: {result}")
    if result != hash:
        print(f"{result} != {hash}\n")
    else:
        print("Hash was generated with md5 and is in same condition")

    result = hashlib.sha1(data).hexdigest()
    print(f"Sha1 {filename}: {result}")
    if result != hash:
        print(f"{result} != {hash}\n")
    else:
        print("Hash was generated with sha1 and is in same condition")

    result = hashlib.sha512(data).hexdigest()
    print(f"Sha512 {filename}: {result}")
    if result != hash:
        print(f"{result} != {hash}\n")
    else:
        print("Hash was generated with sha512 and is in same condition")



if __name__ == '__main__':
    data_folder = "zadani/"
    filename = data_folder + "zprava.txt"
    md5_hash(filename)

    print()

    filename = data_folder + "zprava2.txt"
    hash = "22544abc54c14ca60316ef6c00a3f10e0fc3cb90"
    sha1_hash(filename, hash)

    print()

    filename = data_folder + "zprava3.txt"
    hash = "07b3c9f88cf16f76479399898cafbe81470961fdf57f336717776bb2c6987388d1a15fb4c9f2f823ae2d282466255fb4b5a07dc24ab48316ec400835b0b347b0"
    multi_hash(filename, hash)

#modul 258
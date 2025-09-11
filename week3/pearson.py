import random
PERMUTATION_TABLE = list(range(256))

random.seed(6)
random.shuffle(PERMUTATION_TABLE)

def pearson_hash(input_string: str) -> int:
    # store the result
    # take the string
    # use the ascii and use a modulus (256) will be the index or the permutation
    hash_value = 0

    for char in input_string:
        xor_value = hash_value ^ ord(char)
        hash_value = PERMUTATION_TABLE[xor_value]

    return hash_value

def multi_byte_pearson_hash(input_string: str, length: int) -> list:
    hash_values = list(range(length))

    for char in input_string:
        for i in range(length):
            xor_value = hash_values[i] ^ ord(char)
            hash_values[i] = PERMUTATION_TABLE[xor_value]

    return hash_values



print(f"Hash of 'hello': {pearson_hash('hello')}")
print(multi_byte_pearson_hash('hello', 4))
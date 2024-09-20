import numpy as np

def to_lower_case(text):
    return text.lower()

def remove_spaces(text):
    return text.replace(" ", "")

def generate_key_table(key):
    key = remove_spaces(to_lower_case(key))
    key = key.replace('j', 'i')
    key = ''.join(dict.fromkeys(key))

    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key_table = [char for char in key if char in alphabet]

    for char in alphabet:
        if char not in key_table:
            key_table.append(char)

    return np.array(key_table).reshape(5, 5)

def search(key_table, a, b):
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    pos_a = pos_b = None
    for i in range(5):
        for j in range(5):
            if key_table[i, j] == a:
                pos_a = (i, j)
            elif key_table[i, j] == b:
                pos_b = (i, j)
    return pos_a, pos_b

def encrypt_playfair(plain_text, key):
    key_table = generate_key_table(key)
    cipher_text = []

    plain_text = remove_spaces(to_lower_case(plain_text))
    if len(plain_text) % 2 != 0:
        plain_text += 'x'
    
    for i in range(0, len(plain_text), 2):
        p1, p2 = search(key_table, plain_text[i], plain_text[i+1])

        if p1[0] == p2[0]:
            cipher_text.append(key_table[p1[0], (p1[1] + 1) % 5])
            cipher_text.append(key_table[p2[0], (p2[1] + 1) % 5])

        elif p1[1] == p2[1]:
            cipher_text.append(key_table[(p1[0] + 1) % 5, p1[1]])
            cipher_text.append(key_table[(p2[0] + 1) % 5, p2[1]])

        else:
            cipher_text.append(key_table[p1[0], p2[1]])
            cipher_text.append(key_table[p2[0], p1[1]])

    return ''.join(cipher_text)


def decrypt_playfair(cipher_text, key):
    key_table = generate_key_table(key)
    deciphered_text = []

    for i in range(0, len(cipher_text), 2):
        p1, p2 = search(key_table, cipher_text[i], cipher_text[i+1])

        if p1[0] == p2[0]:
            deciphered_text.append(key_table[p1[0], (p1[1] - 1) % 5])
            deciphered_text.append(key_table[p2[0], (p2[1] - 1) % 5])

        elif p1[1] == p2[1]:
            deciphered_text.append(key_table[(p1[0] - 1) % 5, p1[1]])
            deciphered_text.append(key_table[(p2[0] - 1) % 5, p2[1]])

        else:
            deciphered_text.append(key_table[p1[0], p2[1]])
            deciphered_text.append(key_table[p2[0], p1[1]])

    return ''.join(deciphered_text)
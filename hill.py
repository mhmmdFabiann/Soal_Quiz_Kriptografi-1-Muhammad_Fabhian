import numpy as np

def create_key_matrix(key):
    key = key.lower()
    key_matrix = [[ord(key[i]) % 97 for i in range(3)],
                  [ord(key[i + 3]) % 97 for i in range(3)],
                  [ord(key[i + 6]) % 97 for i in range(3)]]

    return np.array(key_matrix)

def text_to_vector(text):
    text = text.lower()
    vector = [ord(char) % 97 for char in text if char.isalpha()]

    while len(vector) % 3 != 0:
        vector.append(0)

    return np.array(vector).reshape(-1, 3)

def vector_to_text(vector):
    text = ''.join(chr(int(num) + 97) for num in vector.flatten())
    return text

def find_mod_inverse(matrix):
    determinant = int(np.round(np.linalg.det(matrix)))
    determinant_mod_inv = mod_inverse(determinant, 26)

    if determinant_mod_inv is None:
        return None

    matrix_mod_inv = (determinant_mod_inv * np.round(determinant * np.linalg.inv(matrix)).astype(int)) % 26
    return matrix_mod_inv

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_hill(message, key):
    if len(key) < 9:
        raise ValueError("Kunci harus memiliki panjang minimal 9 karakter.")

    key_matrix = create_key_matrix(key[:9])
    vector = text_to_vector(message)
    encrypted_vector = np.dot(vector, key_matrix) % 26
    encrypted_text = vector_to_text(encrypted_vector)
    return encrypted_text.upper()

def decrypt_hill(cipher_text, key):
    key_matrix = create_key_matrix(key[:9])
    vector = text_to_vector(cipher_text)

    # Cari invers kunci matriks (mod 26)
    key_matrix_inv = find_mod_inverse(key_matrix)

    if key_matrix_inv is None:
        raise ValueError("Kunci matriks tidak memiliki invers modulo 26, dekripsi tidak dapat dilakukan.")

    decrypted_vector = np.dot(vector, key_matrix_inv) % 26
    decrypted_text = vector_to_text(decrypted_vector)
    return decrypted_text.upper()

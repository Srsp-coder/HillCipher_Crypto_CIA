def mod_inverse(a, m):
    """
    Finds modular inverse of a under modulo m
    (a * x) % m = 1
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def matrix_inverse_2x2(matrix):
    """
    Finds inverse of a 2x2 matrix under mod 26
    """
    a, b = matrix[0]
    c, d = matrix[1]

    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        raise ValueError("Matrix is not invertible!")

    adj = [[d, -b],
           [-c, a]]

    inv_matrix = []
    for row in adj:
        inv_row = []
        for val in row:
            inv_val = (val * det_inv) % 26
            inv_row.append(inv_val)
        inv_matrix.append(inv_row)

    return inv_matrix


def text_to_numbers(text):
    """Convert text to numbers (A=0, B=1, ..., Z=25)"""
    return [ord(c) - ord('A') for c in text]


def numbers_to_text(numbers):
    """Convert numbers back to text"""
    return ''.join(chr(n + ord('A')) for n in numbers)



def hill_encrypt(plaintext, key):
    """
    Encrypt plaintext using Hill Cipher
    key: 2x2 matrix
    """
    plaintext = plaintext.upper().replace(" ", "")

    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    nums = text_to_numbers(plaintext)
    ciphertext = []

    for i in range(0, len(nums), 2):
        pair = nums[i:i+2]

        c1 = (key[0][0]*pair[0] + key[0][1]*pair[1]) % 26
        c2 = (key[1][0]*pair[0] + key[1][1]*pair[1]) % 26

        ciphertext.extend([c1, c2])

    return numbers_to_text(ciphertext)



def hill_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Hill Cipher
    """
    ciphertext = ciphertext.upper().replace(" ", "")

    inv_key = matrix_inverse_2x2(key)
    nums = text_to_numbers(ciphertext)
    plaintext = []

    for i in range(0, len(nums), 2):
        pair = nums[i:i+2]

        p1 = (inv_key[0][0]*pair[0] + inv_key[0][1]*pair[1]) % 26
        p2 = (inv_key[1][0]*pair[0] + inv_key[1][1]*pair[1]) % 26

        plaintext.extend([p1, p2])

    return numbers_to_text(plaintext)


def djb2_hash(message):
    """
    djb2 hashing algorithm
    """
    hash_value = 5381

    for char in message:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)

    return hash_value % (10**9 + 7)



def send_message(plaintext, key):
    """
    Sender:
    Encrypt + Hash
    """
    cipher = hill_encrypt(plaintext, key)
    hash_val = djb2_hash(cipher)

    print("Encrypted Message:", cipher)
    print("Hash Value:", hash_val)

    return cipher, hash_val


def receive_message(cipher, received_hash, key):
    """
    Receiver:
    Verify + Decrypt
    """
    computed_hash = djb2_hash(cipher)

    print("Received Hash:", received_hash)
    print("Computed Hash:", computed_hash)

    if computed_hash != received_hash:
        print("Data Integrity Compromised!")
        return None

    print("Integrity Verified!")

    plaintext = hill_decrypt(cipher, key)
    return plaintext


if __name__ == "__main__":
    key_matrix = [[3, 3],
                  [2, 5]]

    message = "HELP"

    print("Original Message:", message)

    cipher, hash_val = send_message(message, key_matrix)

    print("\n--- Transmission ---\n")

    decrypted = receive_message(cipher, hash_val, key_matrix)

    print("\nDecrypted Message:", decrypted)
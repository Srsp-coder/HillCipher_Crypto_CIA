# Hill Cipher with djb2 Hash Function

## 1. Overview

This project implements a secure message processing system using:

- Hill Cipher for encryption and decryption
- djb2 hashing function for data integrity verification

The system demonstrates how classical encryption techniques can be combined with hashing to ensure both confidentiality and integrity of transmitted data.

---

## 2. Theory

### 2.1 Hill Cipher

The Hill Cipher is a polygraphic substitution cipher based on linear algebra. It encrypts blocks of letters using matrix multiplication.

Each letter is mapped to a number:
A = 0, B = 1, ..., Z = 25

For a 2×2 key matrix:

Encryption:
C = (K × P) mod 26

Decryption:
P = (K⁻¹ × C) mod 26

Where:
- K is the key matrix
- K⁻¹ is the inverse of K modulo 26
- P is the plaintext vector
- C is the ciphertext vector

The key matrix must be invertible modulo 26.

---

### 2.2 djb2 Hash Function

The djb2 algorithm, developed by Daniel J. Bernstein, is a simple and efficient hashing function.

It computes the hash using:

    hash = hash * 33 + ASCII(character)

Efficient implementation:

    hash = ((hash << 5) + hash) + ord(character)

Steps:
1. Initialize hash = 5381
2. For each character:
   hash = ((hash << 5) + hash) + ord(character)
3. Apply modulo to control size

Justification for choosing djb2:
- Simple to implement from scratch (no libraries required)
- Fast and efficient
- Good distribution for small-scale applications
- Suitable for demonstrating data integrity concepts


---

## 3. System Workflow

Sender:
1. Input plaintext
2. Encrypt using Hill Cipher
3. Generate hash of ciphertext using djb2
4. Send ciphertext and hash

Receiver:
1. Receive ciphertext and hash
2. Recompute hash
3. Compare hashes
4. If valid, decrypt ciphertext
5. If not, reject data

---

## 4. Instructions to Run the Code

1. Ensure Python is installed (Python 3.x)

2. Place the source code file (e.g., main.py) in a directory

3. Run the program:

```
python main.py
```

4. Modify the input message and key inside the code if required

---

## 5. Worked Examples

### Example 1

Input:
Plaintext: HELLO  
Key Matrix:
| 3  3 |
| 2  5 |

Output:
[Insert screenshot of encryption, hash, and decryption output here]

---

### Example 2

Input:
Plaintext: TESTING  
Key Matrix:
| 3  3 |
| 2  5 |

Output:
[Insert screenshot of encryption, hash, and decryption output here]

---
## 6. Test Script (Round Trip)

The implemented system performs the following sequence:

1. Encrypt plaintext using Hill Cipher
2. Generate hash of ciphertext
3. Verify hash at receiver
4. Decrypt ciphertext back to plaintext

This demonstrates a complete encrypt → hash → verify → decrypt pipeline.

---

## 7. Constraints Followed

- Language used: Python
- No external cryptography libraries used
- All algorithms implemented from scratch
- Hash function implemented manually (djb2)
- Hash function is distinct and justified

---

## 8. Conclusion

This project successfully demonstrates the integration of Hill Cipher encryption with hashing for data integrity. It provides a clear understanding of classical cryptography and basic hashing techniques in a unified system.

---

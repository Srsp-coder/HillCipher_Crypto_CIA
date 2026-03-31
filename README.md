# 🔐 Hill Cipher with djb2 Hashing  
### A Secure Message Transmission System with Data Integrity Verification

---

## 📌 Overview

This project implements a secure communication system by combining:

- **Hill Cipher** for encryption and decryption (confidentiality)
- **djb2 Hash Function** for data integrity verification

The system ensures that:
- Messages are encrypted before transmission  
- Any tampering during transmission is detected before decryption  

---

## 🎯 Objectives

- To implement Hill Cipher using matrix operations
- To design a hashing mechanism for integrity verification
- To integrate encryption and hashing into a single system
- To demonstrate secure data transmission concepts

---

## 🚀 Features

- 🔒 Hill Cipher Encryption (2×2 matrix)
- 🔓 Hill Cipher Decryption using matrix inverse
- 🧮 Custom implementation of djb2 hashing
- ✅ Integrity verification before decryption
- ⚠️ Detection of tampered messages
- 💡 Simple and modular Python implementation

---

## 🧠 Concepts Used

- Linear Algebra (Matrix multiplication & inverse)
- Modular Arithmetic (mod 26)
- Classical Cryptography (Hill Cipher)
- Hashing and Data Integrity
- Bitwise Operations

---

## ⚙️ System Architecture

### 🔁 Sender Side
1. Input plaintext message  
2. Convert to uppercase and preprocess  
3. Encrypt using Hill Cipher → Ciphertext  
4. Generate hash using djb2 → Hash value  
5. Send: *(Ciphertext, Hash)*  

---

### 📥 Receiver Side
1. Receive ciphertext and hash  
2. Compute hash of received ciphertext  
3. Compare hashes:
   - ✅ Match → Proceed  
   - ❌ Mismatch → Reject (tampered data)  
4. Decrypt ciphertext → Original message  

---

## 🔐 Hill Cipher

### 📌 Description
Hill Cipher is a polygraphic substitution cipher that uses matrix multiplication to encrypt blocks of text.

---

### 🔑 Key Matrix

```
| 3  3 |
| 2  5 |
```

> The key matrix must be invertible modulo 26.

---

### 🔁 Encryption Formula

```
C = (K × P) mod 26
```

Where:
- K → Key matrix  
- P → Plaintext vector  
- C → Ciphertext vector  

---

### 🔓 Decryption Formula

```
P = (K⁻¹ × C) mod 26
```

Where:
- K⁻¹ → Inverse of key matrix modulo 26  

---

### ⚠️ Padding
If plaintext length is odd, an extra character `'X'` is added.

---

## 🔐 djb2 Hashing Algorithm

### 📌 Overview
The djb2 algorithm is a simple and efficient hashing function developed by Daniel J. Bernstein. It is used in this project to verify data integrity.

---

### ⚙️ Working Principle

The hash is computed using:

```
hash = hash * 33 + ASCII(character)
```

Optimized using bitwise operations:

```
hash = ((hash << 5) + hash) + ord(character)
```

---

### 🔁 Algorithm Steps

1. Initialize:
```
hash = 5381
```

2. For each character:
```
hash = ((hash << 5) + hash) + ord(character)
```

3. Apply modulo:
```
hash = hash % (10^9 + 7)
```

4. Return final hash

---

### 🧠 Characteristics

- Deterministic  
- Fast and efficient  
- Good distribution  
- Lightweight implementation  

---

### ⚠️ Limitations

- Not cryptographically secure  
- Vulnerable to collisions  
- Suitable for educational purposes only  

---

## 🔗 Integration of Encryption and Hashing

### 🔁 Sender
- Encrypt message → Ciphertext  
- Hash ciphertext → Hash  
- Send both  

### 📥 Receiver
- Recompute hash  
- Compare with received hash  
- If valid → Decrypt  
- Else → Reject  

---

## 🧪 Example

```
Original Message: HELLO
Encrypted Message: HIOZHN
Hash Value: 296352541

--- Transmission ---

Received Hash: 296352541
Computed Hash: 296352541
Integrity Verified!

Decrypted Message: HELLOX
```

> Note: 'X' is added for padding.

---

## 🛠️ Installation & Usage

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Run Program
```bash
python main.py
```

---

## 📁 Project Structure

```
project/
│── main.py
│── README.md
```

---

## ⚠️ Limitations

- Works only with uppercase letters (A–Z)
- Uses fixed 2×2 matrix
- Does not handle special characters
- djb2 is not secure for real-world cryptography

---

## 🔐 Security Considerations

- Hill Cipher ensures confidentiality  
- djb2 ensures basic data integrity  
- For real-world applications, use:
  - SHA-256 / SHA-3  
  - HMAC or Digital Signatures  

---

## 📚 Viva Explanation (Short)

This project combines Hill Cipher for encryption and djb2 hashing for data integrity. The ciphertext is hashed before transmission, and the receiver verifies the hash before decrypting to ensure that the message has not been altered.

---

## 👨‍💻 Author

**Sai Pranav S R**

---

## ⭐ Future Enhancements

- Support for larger matrices (3×3, 4×4)
- GUI-based interface
- File encryption support
- Replace djb2 with SHA-3 / HMAC
- Add tampering attack simulation

---

## 📄 License

This project is intended for educational purposes only.

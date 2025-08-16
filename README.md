# Caesar Cipher - Python Implementation

## 📌 Project Description
The **Caesar Cipher** is one of the oldest known encryption techniques. It works by shifting each letter of the plaintext by a fixed number of positions in the alphabet.
This tool enhances it by adding auto-decryption and brute-force cracking for educational and security learning purposes.

## ⚡ Features
- Supports **letters (uppercase & lowercase)**
- Supports **numbers and punctuation**
- User can set a **custom shift key**
- Encrypts and decrypts messages

## 🔑 How It Works
1. User enters a message and a shift key.
2. The program shifts each character in the message forward by the key value to encrypt.
3. To decrypt, it shifts the characters back by the same key value.

##🛠 Requirements

-Python 3.x

-No external libraries required

## ▶ How to Run
1. Clone the repository
2. Navigate into the project folder
   ```bash
      cd Caesar-Cipher-Generator
3. Run the program using Python in windows and for using linux/mac use python3 instead of (Python)
   ```bash
      python caesar_cipher.py
      python3 Caesar_cipher.py


## Follow the prompts

i) Enter the message you want to encrypt.

ii) Enter a key (shift value).

iii) The program will display the encrypted message and then decrypt it back.


##🖥 Example
```bash
Encrypt (E) or Decrypt (D): D
Enter encrypted text: Wklv lv d whvw phvvdjh
[+] Best key guess: 3
[+] Decrypted text: This is a test message


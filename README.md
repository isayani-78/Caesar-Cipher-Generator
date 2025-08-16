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

## 🛠 Requirements

-Python 3.x

-No external libraries required

## ▶ How to Run
1. Clone the repository
    ```bash
    git clone https://github.com/isayani-78/caesar-cipher-generator.git
2. Navigate into the project folder
   ```bash
   cd caesar-cipher-generator
3. Run the program using Python in windows 
   ```bash
   python caesar_cipher.py
4. For using linux/mac use python3 instead of (Python)
    ```bash
   python3 caesar_cipher.py
    
## Follow the prompts

i) Enter the message you want to encrypt/decrypt in E OR D.

ii) Enter a key (shift value).

iii) The program will display the encrypted message or decrypt message as per your prompt.


## 🖥 Example
```bash
[+] Encrypt (E) or Decrypt (D): E
Enter message: Hello World
Enter key: 3
Encrypted: Khoor#Zruog

[+] Encrypt (E) or Decrypt (D): D
Enter encrypted text: Khoor#Zruog
Best key guess: 3
Decrypted text: Hello World

[+] Brute-forcing all possible keys...

Key 1: Gdkkn Vnqkc
Key 2: Fcjjm Umpjb
Key 3: Hello World   ✅
...


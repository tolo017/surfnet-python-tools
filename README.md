🔐 Password Hasher (SHA-256)
A simple Python tool to securely hash passwords using SHA-256, with optional salting support.

🚀 Features
SHA-256 Hashing – Converts plaintext passwords into irreversible cryptographic hashes.

Optional Salting – Adds a salt value to prevent rainbow table attacks.

Lightweight & Portable – Single Python script, no dependencies.

⚙️ Installation
Ensure Python 3.x is installed:
bash
python --version  

Clone this repository:
bash
git clone https://github.com/tolo017/surfnet-python-tools.git  

🛠 Usage
Basic Hashing
password_hasher.py  

Input:
Enter password to hash: 'SurfNet2024' 

Output:
Hashed password (SHA-256): a1b2c3... (64-char hex string)  

Advanced: Adding Salt
python
Modify the code to include a salt:
salt = "yoursalt123"  
hashed = hashlib.sha256((password + salt).encode()).hexdigest() 

📜 License
MIT License – Use freely for ethical security testing.

🔗 Connect
LinkedIn: https://linkedin.com/in/tolootieno

SurfNet Website: Coming Soon
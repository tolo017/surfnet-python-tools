import hashlib

def hash_password(password):
    # Encode the password to bytes, hash it, and return hex digest
    return hashlib.sha256(password.encode()).hexdigest()

user_input = input("Enter a password to hash: ")
print("Hashed password (SHA-256):", hash_password(user_input))
# This script hashes a password using SHA-256 and prints the hashed value.
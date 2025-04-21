import os
# Replace with your actual script folder path
script_path = r"C:\Users\YourUsername\Documents\Python Scripts\Password Hasher Cracker" # Windows
# script_path = "/home/yourusername/scripts"  # Linux/Mac

os.chdir(script_path)  # Change to the script folder
print("Current working directory:", os.getcwd()) #Verify

import hashlib
from itertools import product
from tqdm import tqdm  # type: ignore # For progress bars

class HashCracker:
    def __init__(self):
        self.found = False
        
    def crack(self, target_hash, salt=None, max_length=6, charset='abcdef123'):
        """Brute-force with optional salt support"""
        chars = list(charset)
        
        # Progress bar setup
        total_guesses = sum(len(chars)**i for i in range(1, max_length+1))
        progress = tqdm(total=total_guesses, desc="Cracking", unit="guess")
        
        for length in range(1, max_length+1):
            for attempt in product(chars, repeat=length):
                guess = ''.join(attempt)
                
                # Apply salt if provided
                if salt:
                    salted_guess = guess + salt
                    hashed = hashlib.sha256(salted_guess.encode()).hexdigest()
                else:
                    hashed = hashlib.sha256(guess.encode()).hexdigest()
                
                progress.update(1)
                
                if hashed == target_hash:
                    progress.close()
                    return guess
                    
        progress.close()
        return None

# Example Usage
if __name__ == "__main__":
    cracker = HashCracker()
    
    # Cracking without salt
    print("Testing unsalted hash...")
    test_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # "password"
    result = cracker.crack(test_hash, max_length=8, charset='abcdefghijklmnopqrstuvwxyz')
    print(f"\nCracked: {result}" if result else "Failed to crack")
    
    # Cracking with salt
    print("\nTesting salted hash...")
    salted_hash = "d1e42a8a39d25b48f6865b5af1e0b125c4e58a42e4bae1e8e18a59e568240c8a"  # "password" + "SurfNet"
    result = cracker.crack(salted_hash, salt="SurfNet", max_length=8, charset='abcdefghijklmnopqrstuvwxyz')
    print(f"\nCracked: {result}" if result else "Failed to crack")
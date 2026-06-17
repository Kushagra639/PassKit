import secrets
import string
import hashlib
import math

def generate_password(length):
    
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(secrets.choice(characters) for i in range(length))

    return password

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1
    
    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:   
        return "Strong"
    

def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def calculate_entropy(password):
    charset_size = 0

    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)

    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    
    return entropy

def dictionary_attack(target_hash, wordlist):
    for word in wordlist:
        if sha256_hash(word) == target_hash:
            return word
    return None
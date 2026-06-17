import secrets
import string
import hashlib
import math
import random

class LengthError(Exception):
    pass

def generate_password(length):
    
    if length < 6:
        raise LengthError("Password length should be at least 6 characters.")

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    for i in range(length - 4):
        password.append(secrets.choice(characters))

    random.SystemRandom().shuffle(password)

    password = ''.join(password)

    return password

def check_strength(password):

    entropy = calculate_entropy(password)

    if entropy < 30:
        return "Very Weak"
    elif entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 130:
        return "Strong"
    else:
        return "Very Strong"
    

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

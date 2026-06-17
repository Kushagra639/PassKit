import password_tools as pt
from pathlib import Path

wordlist_path = Path(__file__).parent / "rockyou.txt"

print("="*49)
print("            Password Security Toolkit")
print("="*49)

while True:
    print("\nSelect an option:")
    print("1. Generate a secure password")
    print("2. Check password strength")
    print("3. Hash a password (SHA-256)")
    print("4. Calculate password entropy")
    print("5. Dictionary attack demo (for educational purposes only)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        try:
            length = int(input("Enter desired password length: "))
            password = pt.generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '2':
        try:
            password = input("Enter the password to check: ")
            strength = pt.check_strength(password)
            print(f"Password Strength: {strength}")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == '3':
        try:
            password = input("Enter the password to hash: ")
            hashed = pt.sha256_hash(password)
            print(f"SHA-256 Hash: {hashed}")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif choice == '4':
        try:
            password = input("Enter the password to calculate entropy: ")
            entropy = pt.calculate_entropy(password)
            print(f"Password Entropy: {entropy:.2f} bits")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == '5':
        try:
            target_hash = input("Enter the SHA-256 hash to crack: ")
            with open(wordlist_path, "r", encoding="iso-8859-1") as f:
                wordlist = [f.strip() for f in f.readlines()]
            cracked_password = pt.dictionary_attack(target_hash, wordlist)
            if cracked_password:
                print(f"Cracked Password: {cracked_password}")
            else:
                print("Password not found in dictionary.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == '6':
        print("Exiting Password Security Toolkit. Stay safe!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
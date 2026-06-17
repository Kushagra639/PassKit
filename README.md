# 🔑 PassKit - Password Security Toolkit

A Python-based Password Security Toolkit with a modern CustomTkinter GUI that helps users generate, analyze, and understand secure passwords.

This project was built as part of my cybersecurity learning journey and demonstrates concepts such as password generation, password strength analysis, hashing, entropy calculation, and dictionary attacks.

---

## 🚀 Features

### 🔐 Secure Password Generation

Generate cryptographically secure passwords using Python's built-in `secrets` and `random` modules.

Generated passwords are guaranteed to contain:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

This ensures that every generated password satisfies basic complexity requirements.

---

### 📊 Password Strength Analysis

Evaluates password strength based on *Entropy*

Strength ratings:

- Very Weak (Entropy < 30)
- Weak (30 $\leq$ Entropy < 40)
- Moderate (40 $\le$ Entropy < 60)
- Strong (60 $\le$ Entropy < 130)
- Very Strong (Entropy $\geq$ 130)

---

### 🔢 Password Entropy Calculation

Calculates password entropy in bits.

Higher entropy generally indicates stronger passwords and greater resistance to brute-force attacks.

---

### #️⃣ SHA-256 Hashing

Convert passwords into SHA-256 hashes.

Demonstrates the difference between:

- Plaintext passwords
- Cryptographic hashing

---

### 🎯 Dictionary Attack Demonstration

Educational demonstration of a dictionary attack against SHA-256 password hashes.

Uses a wordlist (such as RockYou) to illustrate how weak passwords can be recovered.

---

### 🛡️ Input Validation

Includes error handling and validation for user inputs to improve reliability and user experience.

---

### 🖥️ Graphical User Interface

Includes a modern GUI built with CustomTkinter featuring:

- Dark / Light theme switching
- Interactive menus
- Popup notifications
- Password analysis screens
- Dictionary attack visualization

The GUI makes cybersecurity concepts more accessible and user-friendly.

---

## 📸 Screenshots

### Main Menu

<img width="432" height="238" alt="image" src="https://github.com/user-attachments/assets/ab0a17f3-91b0-4a5b-a385-f0af551b5935" />
<img width="1536" height="813" alt="image" src="https://github.com/user-attachments/assets/8f4a7505-8517-4672-b705-1e836c1c280d" />
<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/9c914d1e-378d-49f5-b0bc-d7b8a3ec16ed" />


### Password Generation

<img width="432" height="187" alt="image" src="https://github.com/user-attachments/assets/0c3dc904-6092-4ee9-9ef0-c7e3f2216e1a" />
<img width="1536" height="813" alt="image" src="https://github.com/user-attachments/assets/e5723aa5-b457-4117-96dc-309af75b4c80" />
<img width="1536" height="817" alt="image" src="https://github.com/user-attachments/assets/97256c41-599f-4550-a3aa-10b1b3d67b2a" />


### Password Strength Analysis

<img width="432" height="182" alt="image" src="https://github.com/user-attachments/assets/cb3d191a-184e-4774-bf77-e38611ca4bae" />
<img width="1535" height="816" alt="image" src="https://github.com/user-attachments/assets/153ef737-d72e-4dc0-92a2-66c667cc89b0" />


### Hashing a Password

<img width="582" height="187" alt="image" src="https://github.com/user-attachments/assets/e57446d5-78c1-4bc5-a759-17dd35760476" />
<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/52ea7956-eea1-4c2a-9a63-313bf3fa31d8" />


### Calculate Entropy

<img width="428" height="186" alt="image" src="https://github.com/user-attachments/assets/ac22bfc0-2b4e-431d-bb8c-2524a1260c98" />
<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/3cbcea64-717f-45cd-b467-ceeb8f2ac70b" />


### Dictionary Attack Demo

<img width="721" height="193" alt="image" src="https://github.com/user-attachments/assets/122b01fc-099c-4784-91be-eb989ade2bed" />
<img width="717" height="195" alt="image" src="https://github.com/user-attachments/assets/4a1a21b7-cd79-4e89-90dc-e1762d8c76a4" />
<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/f9c5c145-7bda-40c2-9255-36713892af80" />
<img width="1536" height="812" alt="image" src="https://github.com/user-attachments/assets/7cb4c689-20f0-4e60-b473-c423c7999ffe" />
<img width="1533" height="817" alt="image" src="https://github.com/user-attachments/assets/eba19453-8f76-4e1b-968a-f10071e57b32" />


#### ⚠️ Educational Security Demonstration

The dictionary attack feature is included strictly for educational purposes and demonstrates how weak passwords can be recovered using common password databases such as RockYou.

This functionality is intended to promote stronger password practices and cybersecurity awareness.

---

## 🛠️ Technologies Used

- Python 3
- CustomTkinter
- Secrets
- Random
- Hashlib
- Math
- String
- Pathlib
- Tkinter

---

## 📦 Installation

Install dependencies:

```bash
pip install customtkinter
```

### Download the Source Code

*GUI version* (**Recommended**):

- [`main_gui.py`](/main_gui.py)
- [`password_tools.py`](/password_tools.py)
- [`rockyou.txt`](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) wordlist
- [`pastel_theme.json`](/pastel_theme.json)

Alternatively, the *console version* can be used:

- [`main.py`](/main.py)
- [`password_tools.py`](/password_tools.py)
- [`rockyou.txt`](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) wordlist


**Store all files in the same project folder; otherwise, you will have to change the path of all files in the code.**

---

## ▶️ Usage

Run:

```bash
python main_gui.py
```

or

```bash
python main.py
```

Select one of the available tools:

```text
1. Generate a secure password
2. Check password strength
3. Hash a password (SHA-256)
4. Calculate password entropy
5. Dictionary attack demo
6. Exit
```

---

## 📋 Example Output

```text
=================================================
       PassKit - Password Security Toolkit
=================================================

Select an option:
1. Generate a secure password
2. Check password strength
3. Hash a password (SHA-256)
4. Calculate password entropy
5. Dictionary attack demo (for educational purposes only)
6. Exit
Enter your choice (1-6): 1
Enter desired password length: 10
Generated Password: 3s2Z=s~cVR
```

```text
Enter your choice (1-6): 2
Enter the password to check: 3s2Z=s~cVR
Password Strength: Strong
```

```text
Enter your choice (1-6): 4
Enter the password to calculate entropy: 3s2Z=s~cVR
Password Entropy: 65.55 bits
```

---

## ⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.

The dictionary attack feature is included solely to demonstrate password security concepts and should only be used on systems and data that you own or are authorized to test.

Users are responsible for complying with all applicable laws and regulations.

---

## 🎯 Learning Objectives

This project helped me practice:

- Python Programming
- Secure Password Generation
- Cryptographic Hashing
- SHA-256
- Password Entropy
- Dictionary Attacks
- Input Validation
- Exception Handling
- Cybersecurity Fundamentals

---

## 🚧 Future Improvements

Planned future enhancements include:

- Multiple hashing algorithms (SHA-1, SHA-512, bcrypt)
- Password policy auditing
- Password history management
- Exportable reports
- Have I Been Pwned integration
- Password manager integration
- Performance optimization for large wordlists

---

## 🙋‍♂️ Author

Kushagra Aggarwal

- Cyber Security Enthusiast
- Computer Science Student
- Alumnus, Dr. B.R. Ambedkar SoSE, Karol Bagh

<p style="margin: 0; padding: 0;">
  <span style="font-weight: bold; font-size: 1.1em;">Follow me on: </span>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/LinkedIn%20Logo.png"
         alt="LinkedIn"
         width="20"
         style="display: block;">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/Instagram_logo.png"
         alt="Instagram"
         width="20"
         style="display: block;">
  </a>
</p>

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

Feel free to ⭐ the repository if you find it useful!

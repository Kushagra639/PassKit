import password_tools as pt
from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk

theme_file = Path(__file__).parent / "pastel_theme.json"
wordlist_path = Path(__file__).parent / "rockyou.txt"

ctk.set_appearance_mode("system")
ctk.set_default_color_theme(str(theme_file)) # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system

app = ctk.CTk()
app.title("🔑 PassKit - Password Security Toolkit") 
app.geometry("900x700") 
app.resizable(width=True, height=True)

def create_bottom_frame():
    bottom_frame = ctk.CTkFrame(master=app)
    bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)
    return bottom_frame

def change_theme(): # Function to toggle between light and dark themes
    try:
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    except Exception as e:
        print(f" ❌ Error changing theme: {e}")
        messagebox.showerror("Theme Error", f"Error changing theme: {e}")

def clear_screen(): # Function to clear the current screen by destroying all widgets in the main application window
    try:
        for widget in app.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f" ❌ Error clearing screen: {e}")
        messagebox.showerror("Screen Error", f"Error clearing screen: {e}")

def main_menu():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Welcome to PassKit 🔑!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        options = [
            "Generate a Secure Password", "Check Password Strength", "Hash a Password", "Calculate Entropy", "Dictionary Attack (For Educational Purposes Only)", "Exit"
        ]
        for idx, opt in enumerate(options, 1):
            ctk.CTkButton(app, text=f"{idx}. {opt}", command=lambda i=idx: option_selected(i)).pack(pady=4) # Creates buttons for each option in the main menu
        
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in main menu: {e}")
        messagebox.showerror("Menu Error", f"Error in main menu: {e}")

def generate_password_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Generate a Secure Password", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter desired password length (minimum 6 characters):").pack(pady=5)
        length_entry = ctk.CTkEntry(app)
        length_entry.pack(pady=5)
        result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
        result_label.pack()

        def generate():
            try:
                length = int(length_entry.get())
                password = pt.generate_password(length)
                result_label.configure(text=f"Generated Password: {password}")
                messagebox.showinfo("Password Generated", f"Your generated password is:\n{password}")
            except ValueError:
                print(" ❌ Error: Invalid input. Please enter a valid number.")
                messagebox.showerror("Input Error", "Invalid input. Please enter a valid number.")
            except pt.LengthError as le:
                print(f" ❌ Error: {le}")
                messagebox.showerror("Length Error", str(le))
            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

        ctk.CTkButton(app, text="Generate Password", command=generate).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)

    except Exception as e:
        print(f" ❌ Error in generate password screen: {e}")
        messagebox.showerror("Screen Error", f"Error in generate password screen: {e}")

def check_password_strength_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Check Password Strength", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the password to check:").pack(pady=5)
        password_entry = ctk.CTkEntry(app, show="*")
        password_entry.pack(pady=5)
        result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
        result_label.pack()

        def check_strength():
            try:
                password = password_entry.get()
                strength = pt.check_strength(password)
                entropy = pt.calculate_entropy(password)
                result_label.configure(text=f"Password Strength: {strength}\n\nEntropy: {entropy:.2f} bits")
                messagebox.showinfo("Password Strength", f"The strength of the entered password is: {strength}")
            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

        ctk.CTkButton(app, text="Check Strength", command=check_strength).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)

    except Exception as e:
        print(f" ❌ Error in check password strength screen: {e}")
        messagebox.showerror("Screen Error", f"Error in check password strength screen: {e}")

def hash_password_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Hash a Password (SHA-256)", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the password to hash:").pack(pady=5)
        password_entry = ctk.CTkEntry(app, show="*")
        password_entry.pack(pady=5)
        result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
        result_label.pack()

        def hash_password():
            try:
                password = password_entry.get()
                hashed = pt.sha256_hash(password)
                result_label.configure(text=f"SHA-256 Hash: {hashed}")
                messagebox.showinfo("SHA-256 Hash", f"The SHA-256 hash of the entered password is:\n{hashed}")
            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

        ctk.CTkButton(app, text="Hash Password", command=hash_password).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)

    except Exception as e:
        print(f" ❌ Error in hash password screen: {e}")
        messagebox.showerror("Screen Error", f"Error in hash password screen: {e}")

def calculate_entropy_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Calculate Password Entropy", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the password to calculate entropy:").pack(pady=5)
        password_entry = ctk.CTkEntry(app, show="*")
        password_entry.pack(pady=5)
        result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
        result_label.pack()

        def calculate_entropy():
            try:
                password = password_entry.get()
                entropy = pt.calculate_entropy(password)
                result_label.configure(text=f"Password Entropy: {entropy:.2f} bits")
                messagebox.showinfo("Password Entropy", f"The entropy of the entered password is: {entropy:.2f} bits")
            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

        ctk.CTkButton(app, text="Calculate Entropy", command=calculate_entropy).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)

    except Exception as e:
        print(f" ❌ Error in calculate entropy screen: {e}")
        messagebox.showerror("Screen Error", f"Error in calculate entropy screen: {e}")

def dictionary_buffer_screen(target_hash):
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Performing Dictionary Attack...", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="This may take a while depending on the size of the wordlist and the complexity of the hash.", wraplength=600).pack(pady=5)

        app.update()

        with open(wordlist_path, "r", encoding="iso-8859-1") as f:
            wordlist = [f.strip() for f in f.readlines()]
            cracked_password = pt.dictionary_attack(target_hash, wordlist)
            if cracked_password:
                clear_screen()
                bottom_frame = create_bottom_frame()

                ctk.CTkLabel(app, text="Password Cracked!\n", font=ctk.CTkFont(size=24, weight="bold"), text_color="green").pack(pady=10)
                ctk.CTkLabel(app, text=f"Hash: {target_hash}\n", font=ctk.CTkFont(size=14)).pack(pady=5)
                ctk.CTkLabel(app, text=f"Cracked Password: {cracked_password}", font=ctk.CTkFont(size=14), text_color="green").pack(pady=10)
                ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
                ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
                messagebox.showinfo("Password Cracked", f"The password corresponding to the entered hash is:\n{cracked_password}")
            
            else:
                clear_screen()
                bottom_frame = create_bottom_frame()

                ctk.CTkLabel(app, text="Password not found in dictionary.\n", font=ctk.CTkFont(size=24), text_color="red").pack(pady=10)
                ctk.CTkLabel(app, text=f"Hash: {target_hash}", font=ctk.CTkFont(size=14)).pack(pady=5)
                ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
                ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
                messagebox.showinfo("Not Found", "The password corresponding to the entered hash was not found in the dictionary.")

    except Exception as e:
        print(f" ❌ Error in dictionary buffer screen: {e}")
        messagebox.showerror("Screen Error", f"Error in dictionary buffer screen: {e}")

def dictionary_attack_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Dictionary Attack Demo", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
        ctk.CTkLabel(app, text="Enter the SHA-256 hash to crack:").pack(pady=5)
        hash_entry = ctk.CTkEntry(app, width=500)
        hash_entry.pack(pady=5)

        def dictionary_attack():
            try:
                target_hash = hash_entry.get()
                if not target_hash:
                    messagebox.showerror("Input Error", "Please enter a SHA-256 hash to crack.")
                    return
                if len(target_hash) != 64 or not all(c in '0123456789abcdef' for c in target_hash.lower()):
                    messagebox.showerror("Input Error", "Please enter a valid SHA-256 hash (64 hexadecimal characters).")
                    return
                dictionary_buffer_screen(target_hash)

            except Exception as e:
                print(f"An error occurred: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")

        ctk.CTkButton(app, text="Start Dictionary Attack", command=dictionary_attack).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=main_menu).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)

    except Exception as e:
        print(f" ❌ Error in dictionary attack screen: {e}")
        messagebox.showerror("Screen Error", f"Error in dictionary attack screen: {e}")


def option_selected(option): # Function to handle the option selected by the user in the main menu
    try:
        if option == 1:
            generate_password_screen()
        elif option == 2:
            check_password_strength_screen()
        elif option == 3:
            hash_password_screen()
        elif option == 4:
            calculate_entropy_screen()
        elif option == 5:
            dictionary_attack_screen()
        elif option == 6:
            app.destroy()
        else:
            messagebox.showerror("Error", "Invalid option selected.")
            main_menu()
    except Exception as e:
        print(f" ❌ Error in option selection: {e}")
        messagebox.showerror("Option Selection Error", f"Error in option selection: {e}")

main_menu() # Start the application by displaying the main menu
app.mainloop()
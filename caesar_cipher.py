import tkinter as tk
from tkinter import ttk, messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                shifted = (ord(char) - base + shift) % 26 + base
            else:
                shifted = (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def process_text():
    try:
        message = message_entry.get("1.0", tk.END).strip()
        shift_str = shift_entry.get()
        if not shift_str:
            messagebox.showerror("Error", "Shift value cannot be empty.")
            return
        shift = int(shift_str)
        mode = mode_var.get()

        if not message:
            messagebox.showerror("Error", "Message cannot be empty.")
            return

        output = caesar_cipher(message, shift, mode)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, output)
        result_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the shift value.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def main():
    global message_entry, shift_entry, mode_var, result_text

    root = tk.Tk()
    root.title("Caesar Cipher GUI")
    root.geometry("500x400")
    root.resizable(False, False)

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Message
    message_label = ttk.Label(main_frame, text="Message:")
    message_label.pack(anchor=tk.W)
    message_entry = tk.Text(main_frame, height=5, width=50)
    message_entry.pack(pady=(0, 10))

    # Shift
    shift_frame = ttk.Frame(main_frame)
    shift_frame.pack(fill=tk.X, pady=(0, 10))
    shift_label = ttk.Label(shift_frame, text="Shift value:")
    shift_label.pack(side=tk.LEFT)
    shift_entry = ttk.Entry(shift_frame, width=10)
    shift_entry.pack(side=tk.LEFT, padx=(5,0))

    # Mode
    mode_var = tk.StringVar(value='encrypt')
    mode_frame = ttk.Frame(main_frame)
    mode_frame.pack(anchor=tk.W, pady=(0, 10))
    encrypt_radio = ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode_var, value='encrypt')
    encrypt_radio.pack(side=tk.LEFT)
    decrypt_radio = ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode_var, value='decrypt')
    decrypt_radio.pack(side=tk.LEFT, padx=(10,0))

    # Buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=(10, 10))
    process_button = ttk.Button(button_frame, text="Process", command=process_text)
    process_button.pack(side=tk.LEFT)

    def clear_fields():
        message_entry.delete("1.0", tk.END)
        shift_entry.delete(0, tk.END)
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.config(state=tk.DISABLED)
        mode_var.set('encrypt')

    clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
    clear_button.pack(side=tk.LEFT, padx=(10,0))


    # Result
    result_label = ttk.Label(main_frame, text="Result:")
    result_label.pack(anchor=tk.W)
    result_text = tk.Text(main_frame, height=5, width=50, state=tk.DISABLED)
    result_text.pack()

    root.mainloop()


if __name__ == '__main__':
    main() 
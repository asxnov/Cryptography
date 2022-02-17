import tkinter as tk

FONT = ("calibre", 20, "bold")


class CipherGUI:
    def __init__(self, master):
        master.title("Cipher GUI")
        self.plaintext = tk.StringVar(master, value="")
        self.ciphertext = tk.StringVar(master, value="")

        self.plain_label = tk.Label(master, text="Text", fg="black", font=FONT).grid(row=0, column=0)
        self.plain_entry = tk.Entry(master,textvariable=self.plaintext, width=30, font=FONT)
        self.plain_entry.grid(row=2, column=0, padx=20)
        self.encrypt_button = tk.Button(master, text="Encrypt",fg="black",command=lambda: self.encrypt_callback(), font=FONT).grid(row=3, column=0)
        self.plain_clear = tk.Button(master, text="Clear",command=lambda: self.clear('plain'), font=FONT).grid(row=4, column=0)

        self.cipher_label = tk.Label(master, text="Ciphertext", fg="black", font=FONT).grid(row=0, column=4)
        self.cipher_entry = tk.Entry(master,textvariable=self.ciphertext, width=30, font=FONT)
        self.cipher_entry.grid(row=2, column=4, padx=20)
        self.decrypt_button = tk.Button(master, text="Decrypt", fg="black",command=lambda: self.decrypt_callback(),font=FONT).grid(row=3, column=4)
        self.cipher_clear = tk.Button(master, text="Clear",command=lambda: self.clear('cipher'), font=FONT).grid(row=4, column=4)

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        elif str_val == 'plain':
            self.plain_entry.delete(0, 'end')


    def encrypt_callback(self):
        ciphertext = encrypt(self.plain_entry.get())
        self.cipher_entry.delete(0, tk.END)
        self.cipher_entry.insert(0, ciphertext)
    def decrypt_callback(self):

        plaintext = decrypt(self.cipher_entry.get())
        self.plain_entry.delete(0, tk.END)
        self.plain_entry.insert(0, plaintext)
        
def encrypt(message):
    k = "LEMON"
    k *= len(message) // len(k) + 1
    c = ""
    for i, j in enumerate(message):
        gg = (ord(j) + ord(k[i]))
        c += chr(gg % 26 + 65)
    return "".join(str(c))

def decrypt(message):
    k = "LEMON"
    d = ""
    for i, j in enumerate(message):
        gg = (ord(j) - ord(k[i]))
        d += chr(gg % 26 + 65)
    return "".join(str(d))

if __name__ == "__main__":
    root = tk.Tk()
    vig = CipherGUI(root)
    root.mainloop()
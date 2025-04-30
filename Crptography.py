from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == current_password:
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    
    elif password == "":
        messagebox.showerror("decryption", "Input Password")
    
    else:
        messagebox.showerror("decryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == current_password:
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    
    else:
        messagebox.showerror("encryption", "Invalid Password")

def change_password():
    global current_password
    new_password = new_password_entry.get()
    confirm_new_password = confirm_new_password_entry.get()

    if new_password == confirm_new_password:
        current_password = new_password
        messagebox.showinfo("Password Changed", "Password has been changed successfully.")
        change_password_screen.destroy()
    else:
        messagebox.showerror("Password Mismatch", "New passwords do not match.")

def change_password_screen():
    global change_password_screen
    change_password_screen = Toplevel(screen)
    change_password_screen.title("Change Password")
    change_password_screen.geometry("300x150")
    change_password_screen.configure(bg="#1089ff")

    Label(change_password_screen, text="New Password:", bg="#1089ff", fg="white").grid(row=0, column=0, padx=10, pady=10)
    Label(change_password_screen, text="Confirm New Password:", bg="#1089ff", fg="white").grid(row=1, column=0, padx=10, pady=10)

    global new_password_entry
    global confirm_new_password_entry

    new_password_entry = Entry(change_password_screen, show="*")
    confirm_new_password_entry = Entry(change_password_screen, show="*")

    new_password_entry.grid(row=0, column=1, padx=10, pady=10)
    confirm_new_password_entry.grid(row=1, column=1, padx=10, pady=10)

    Button(change_password_screen, text="Change Password", bg="#ed3833", fg="white", command=change_password).grid(row=2, column=0, columnspan=2, pady=10)

current_password = "5813"

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robot 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    Button(text="ENCRYPT", height="2", width=23, bg="#ff6347", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#2ecc71", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#3498db", fg="white", bd=0, command=reset).place(x=10, y=300)
    Button(text="Change Password", height="2", width=50, bg="#3498db", fg="white", bd=0, command=change_password_screen).place(x=10, y=350)

    screen.mainloop()

def reset():
    code.set("")
    text1.delete(1.0, END)

main_screen()                             



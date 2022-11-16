import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title("LogIn")
root.resizable(FALSE, FALSE)
root.configure(background="#f7f7f7")
root.iconbitmap(os.getcwd() + "/logo.ico")
root.geometry("500x600"+"+410+40")

def main():
    email_input = email.get()
    used_emails = open(os.getcwd() + "/used_email.txt", "r")
    used_email = used_emails.readlines()
    if len(email_input) == 0:
        used_emails.close()
        nothing_true = messagebox.showwarning("Warning", "please write the email!")
        email.focus_force()
    elif email_input.count(" ") > 0:
        used_emails.close()
        space_true = messagebox.showwarning("Warning", "The email cannot have spaces!")
        email.delete(0, END)
        email.focus_force()
    elif email_input.count("@gmail.com") == 0:
        used_emails.close()
        no_gmail_true = messagebox.showwarning("Warning", "The email must have '@gmail.com' !")
        email.delete(0, END)
        email.focus_force()
    elif email_input.count("@gmail.com") > 1:
        used_emails.close()
        more_gmail_true = messagebox.showwarning("Warning", "The email must have only 1 '@gmail.com' !")
        email.delete(0, END)
        email.focus_force()
    elif email_input.find("@gmail.com") != len(email_input) - 10:
        used_emails.close()
        gmail_not_in_end_true = messagebox.showwarning("Warning", "'@gmail.com' must be at the end of the email!")
        email.delete(0, END)
        email.focus_force()
    elif email_input.find("@gmail.com") < 5:
        used_emails.close()
        no_text_true = messagebox.showwarning("Warning", "there must be atleast 5 letters before '@gmail.com' !")
        email.delete(0, END)
        email.focus_force()
    elif f"{email_input}\n" not in used_email:
        used_emails.close()
        not_available_email_true = messagebox.showwarning("Warning", "The email is invalid!")
        email.delete(0, END)
        email.focus_force()
    elif f"{email_input}\n" in used_email:
        used_emails.close()
        password_input = password.get()
        accounts = open(os.getcwd() + "/data.txt", "r")
        account = accounts.readlines()
        correct_password = account.index(f"    email: {email_input}\n") + 1
        if len(password_input) == 0:
            accounts.close()
            nothing_true = messagebox.showwarning("Warning", "please write the password!")
            password.focus_force()
        elif f"    password: {password_input}\n" != account[correct_password]:
            accounts.close()
            wrong_password_true = messagebox.showwarning("Warning", "Wrong password!")
            password.delete(0, END)
            password.focus_force()
        elif f"    password: {password_input}\n" == account[correct_password]:
            name_position = account.index(f"    email: {email_input}\n") - 1
            name_ = account[name_position]
            account_name = name_[0:len(name_)-2]
            accounts.close()
            logged_In = messagebox.showinfo("LoggedIn Successfully", f"Welcome Back {account_name} !")
            root.destroy()


user_image = ImageTk.PhotoImage(Image.open(os.getcwd() + "/user_image.jpg"))
user_image_label = Label(root, image=user_image)
user_image_label.grid(row=0, column=0, padx=200, pady=20, columnspan=2)

email = Entry(root, width=30, borderwidth=1)
password = Entry(root, width=30, borderwidth=1)

email_label = Label(root, text="email:", bg="#f7f7f7")
password_label = Label(root, text="password:", bg="#f7f7f7")

button_submit = Button(root, text="LOGIN", padx=10, pady=5, command=main)



email.grid(row=1, column=1, padx=(0, 140), pady=(40, 30))
password.grid(row=2, column=1, padx=(0, 140))

email_label.grid(row=1, column=0, padx=(90, 0), pady=(40, 30))
password_label.grid(row=2, column=0, padx=(90, 0))

button_submit.grid(row=5, column=0, pady=(220, 0), columnspan=2)


run = messagebox.askyesno("Welcome User!", "Do you want to login?")

email.focus_force()

if run == 1:
    root.mainloop()
elif run == 0:
    no = messagebox.showinfo("GoodBye", "as you want sir!")
    root.destroy()
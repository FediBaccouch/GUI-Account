import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Create Account")
root.resizable(FALSE, FALSE)
root.configure(background="#f7f7f7")
root.iconbitmap(os.getcwd() + "/logo.ico")
root.geometry("500x600"+"+410+40")

picked = IntVar()
picked.set(2)

def create():
    global password
    global password_label
    password = Entry(root, width=30, borderwidth=1)
    password_label = Label(root, text="password:", bg="#f7f7f7")

    password.grid(row=4, column=1, padx=(0, 140), pady=(20, 0))
    password_label.grid(row=4, column=0, padx=(90, 0), pady=(20, 0))
    create_password.configure(state=DISABLED)
    generate_password.configure(state=NORMAL)

def generate():
    try:
        password.grid_forget()
        password_label.grid_forget()
        create_password.configure(state=NORMAL)
        generate_password.configure(state=DISABLED)
    except NameError:
        create_password.configure(state=NORMAL)
        generate_password.configure(state=DISABLED)

def main():
    name_input = name.get()
    used_names = open(os.getcwd() + "/used_name.txt", "r")
    used_name = used_names.readlines()
    if f"{name_input}\n" in used_name:
        used_names.close()
        used_name_true = messagebox.showwarning("Warning", "The name is already used!")
        name.delete(0, END)
        name.focus_force()
    elif len(name_input) == 0:
        used_names.close()
        nothing_true = messagebox.showwarning("Warning", "please write a name!")
        name.focus_force()
    else:
        used_names.close()
        email_input = email.get()

        used_emails = open(os.getcwd() + "/used_email.txt", "r")
        used_email = used_emails.readlines()
        if f"{email_input}\n" in used_email:
            used_emails.close()
            used_email_true = messagebox.showwarning("Warning", "The email is already used!")
            email.delete(0, END)
            email.focus_force()
        elif len(email_input) == 0:
            used_emails.close()
            nothing_true = messagebox.showwarning("Warning", "please write an email!")
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
        else:
            if picked.get() == 0:
                password_input = password.get()
                if len(password_input) == 0:
                    nothing_true = messagebox.showwarning("Warning", "please write a password!")
                    password.focus_force()
                else:
                    new_name = open(os.getcwd() + "/used_name.txt", "a")
                    new_name.write(f"{name_input}\n")
                    new_name.close()
                    new_email = open(os.getcwd() + "/used_email.txt", "a")
                    new_email.write(f"{email_input}\n")
                    new_email.close()
                    account = open(os.getcwd() + "/data.txt", "a")
                    account.write(f"{name_input}:\n    email: {email_input}\n    password: {password_input}\n")
                    account.close()
                    created = messagebox.showinfo("Congratulation", "Account Created Successfully!")
                    root.destroy()
            elif picked.get() == 1:
                import pass_generator
                password_input = pass_generator.password()
                new_name = open(os.getcwd() + "/used_name.txt", "a")
                new_name.write(f"{name_input}\n")
                new_name.close()
                new_email = open(os.getcwd() + "/used_email.txt", "a")
                new_email.write(f"{email_input}\n")
                new_email.close()
                account = open(os.getcwd() + "/data.txt", "a")
                account.write(f"{name_input}:\n    email: {email_input}\n    password: {password_input}\n")
                account.close()
                created = messagebox.showinfo("Congratulation", f"Account Created Successfully!\n\n      password: {password_input}")
                root.destroy()
            else:
                no_password_true = messagebox.showwarning("Warning", "please select a password option!")
        

user_image = ImageTk.PhotoImage(Image.open(os.getcwd() + "/user_image.jpg"))
user_image_label = Label(root, image=user_image)
user_image_label.grid(row=0, column=0, padx=200, pady=20, columnspan=2)

name = Entry(root, width=30, borderwidth=1)
email = Entry(root, width=30, borderwidth=1)

name_label = Label(root, text="name:", bg="#f7f7f7")
email_label = Label(root, text="email:", bg="#f7f7f7")

create_password = Radiobutton(root, text="Create Password", bg="#f7f7f7", variable=picked, value=0, command=create)
generate_password = Radiobutton(root, text="Generate Password", bg="#f7f7f7", variable=picked, value=1, command=generate)

button_submit = Button(root, text="CREATE", padx=10, pady=5, command=main)



name.grid(row=1, column=1, padx=(0, 140), pady=(40, 30))
email.grid(row=2, column=1, padx=(0, 140))

name_label.grid(row=1, column=0, padx=(90, 0), pady=(40, 30))
email_label.grid(row=2, column=0, padx=(90, 0))

create_password.grid(row=3, column=0, padx=(0, 200), pady=(50, 0), columnspan=2)
generate_password.grid(row=3, column=1, padx=(50, 0), pady=(50,0), columnspan=2)

button_submit.grid(row=5, column=0, pady=(160, 0), columnspan=2)


run = messagebox.askyesno("Welcome User!", "Do you want to create an account?")

name.focus_force()

if run == 1:
    root.mainloop()
elif run == 0:
    no = messagebox.showinfo("GoodBye", "as you want sir!")
    root.destroy()
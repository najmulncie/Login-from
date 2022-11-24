from tkinter import *
from tkinter import messagebox


window = Tk()
window.title('Login')
window.geometry('500x500')
window.resizable(width=False, height=False)
frame = Frame(window, bg='white')
frame.place(x=100, y=100, width= 300, height=300)

login_title = Label(frame, text='Login from', font=("Impact", 35, "bold"), bg='white', fg='#33e0ff')
login_title.place(x=40, y=10)

email_address = Label(frame, text='Email', font=("Goudy old style", 15, "bold"), bg='white', fg='grey')
email_address.place(x=10, y=80)
entry_email = Entry(frame, font=("Goudy old style", 10, "bold"),bg='white', width=39, fg='grey')
entry_email.place(x=10, y=110)

password = Label(frame, text='Password', font=("Goudy old style", 15, "bold"), bg='white', fg='grey')
password.place(x=10, y=140)
entry_pass = Entry(frame, font=("Goudy old style", 10, "bold"),bg='white', width=39, fg='grey')
entry_pass.place(x=10, y=170)



def check_function():
    if entry_email.get() =="" or entry_pass.get() =="":
        messagebox.showerror("Error", "All fields are required!",parent=window)

    elif entry_email.get() != "najmulnice284@gmail.com" or entry_pass.get() != "123456":
        messagebox.showerror("Error", "Invalid email or Password!",parent=window)
    else:
        messagebox.showinfo("welcome", f"welcome here your email: {entry_email.get()}")

login_btn = Button(frame,text='Login',font=("Arial", 15, "bold"), bg='skyblue', fg='white', width=10, command=check_function)
login_btn.place(x=10, y=210)




window.mainloop()
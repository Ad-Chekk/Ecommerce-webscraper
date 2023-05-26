import tkinter

import PIL
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
from trial import outp




def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        message_label.config(text="Login Successful!", foreground="green")
        outp()

    else:
        message_label.config(text="Invalid username or password", foreground="red")


# Create tkinter window
root = tk.Tk()
root.title("Login")
root.configure(bg='light blue')
root.eval('tk::PlaceWindow . center')
root.geometry('350x200')

title_label=ttk.Label(root,width=20, text='Amazon Web scraper \u0024', font='calibri 17 bold', background='black', relief='ridge',anchor='center', foreground='yellow')
title_label.grid(row=0, column=2, pady=10, )

# Create username label and entry widget
username_label = ttk.Label(root,width=10, text="Username: ", font= 'lato 13 bold',background='dark blue', foreground='white', borderwidth=1, relief='ridge')
username_label.grid(row=3, column=1,padx= 2)
username_entry = ttk.Entry(root)
username_entry.grid(row=3, column=2, pady=3, padx=2)

# Create password label and entry widget
password_label = ttk.Label(root,width=10, text="Password:",font='lato 13 bold' ,background='dark blue', foreground='white', relief='ridge')
password_label.grid(row=6, column=1, pady=3,padx= 2)
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=6, column=2, pady=3,padx= 2)

# Create login button
login_button = ttk.Button(root,style='', text="Login",command=login)
style = ttk.Style()
style.configure("Custom.TButton", font=("arial", 14, "bold",) )
login_button.grid(row=7, column=2, columnspan=2,pady=5,padx= 2)

# Create message label for displaying login result
message_label = ttk.Label(root, text="Test")
message_label.grid(row=8, column=2, columnspan=2, pady= 5,padx= 2)

# Run the tkinter event loop
root.mainloop()

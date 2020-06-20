from tkinter import *
from tkinter import filedialog
import cv2
import os
import tkinter as TK
import numpy as np
import pandas as pd
from tkinter.filedialog import askopenfilename
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("450x275")
    register_screen.configure(background="turquoise")
    
    global username
    global Email
    global password
    global username_entry
    global password_entry
    global Email_entry
    username = StringVar()
    Email = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below :",fg="blue",font=("Calibri", 15, "italic"), bg="turquoise").pack()
    Label(register_screen, text="", bg="turquoise").pack()
    username_lable = Label(register_screen, text="Username * " ,fg="red", bg="turquoise", font=(18))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, bd=3, width=40)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",fg="red", bg="turquoise", font=(18))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', bd=3, width=40)
    password_entry.pack()
    Email_lable = Label(register_screen, text="Email ID * ",fg="red", bg="turquoise", font=(18))
    Email_lable.pack()
    Email_entry = Entry(register_screen, textvariable=Email, bd=3, width=40)
    Email_entry.pack()
    Label(register_screen, text="", bg="turquoise").pack()
    Button(register_screen, text="Register", command = register_user, font=('helvetica', 15), width=20).pack()
    # Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("450x275")
    login_screen.configure(background="spring green")
    Label(login_screen, text="Please enter details below to login :",fg="dodger blue", bg="spring green", font=("Calibri", 15, "italic")).pack()
    Label(login_screen, text="", bg="spring green").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",fg="red", bg="spring green", font=(18)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bd=3, width=40)
    username_login_entry.pack()
    Label(login_screen, text="", bg="spring green").pack()
    Label(login_screen, text="Password * ",fg="red", bg="spring green", font=(18)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', bd=3, width=40)
    password_login_entry.pack()
    Label(login_screen, text="", bg="spring green").pack()
    Button(login_screen, text="Login", command = login_verify, font=('helvetica', 15), width=20).pack()

# Implementing event on register button

def register_user():
 
    username_info = username.get()
    password_info = password.get()
    Email_info = Email.get()

    file = open('username_info.txt', "a+")
    file.write('Username '+ username_info + '\n')
    file.write( 'Password '+password_info + '\n')
    file.write('Email ID  ' + Email_info + '\n')
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Email_entry.delete(0,END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 #   register_screen.destroy()
# Implementing event on login button 

def login_verify():
    username1 = 'Username '+username_verify.get()
    password1 = 'Password '+password_verify.get()
    
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    file1 = open('username_info.txt', "r")
    check = file1.read().splitlines()
    print(username1,password1,check)
    if username1 in check:
        print(username1,password1,check)
        if password1 in check:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

# Designing popup for login success
 
def login_success():
    global login_success_screen ,panelA, panelB

    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x100")
    login_success_screen.configure(background="green2")
    Label(login_success_screen, text="Login Success !!", fg="White", bg="green2", font=('calibri', 15, "bold")).pack()
    Label(text="", bg="green2").pack()
    Label(text="", bg="green2").pack()
    Button(login_success_screen, text="OK", command=delete_login_success, font=('helvetica', 12)).pack()

    # Registration success
def register_success():
    global register_success_screen ,panelA, panelB

    register_success_screen = Toplevel(register_screen)
    register_success_screen.title("Success")
    register_success_screen.geometry("250x100")
    register_success_screen.configure(background="green2")
    Label(register_success_screen, text="Register Success !!", fg="White", bg="green2", font=('calibri', 15, "bold")).pack()
    Label(text="", bg="green2").pack()
    Label(text="", bg="green2").pack()
    Button(Register_success_screen, text="OK", command=delete_register_success, font=('helvetica', 12)).pack()

# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Retry")
    password_not_recog_screen.geometry("250x100")
    password_not_recog_screen.configure(background="red2")
    Label(password_not_recog_screen, text="Invalid Password !!", fg="White", bg="red2", font=('calibri', 15, "bold")).pack()
    Label(text="", bg="red2").pack()
    Label(text="", bg="red2").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised, font=('helvetica', 12)).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Retry")
    user_not_found_screen.geometry("250x100")
    user_not_found_screen.configure(background="violet red")
    Label(user_not_found_screen, text="User Not Found !!", fg="white", bg="violet red", font=("calibri", 15, "bold")).pack()
    Label(text="", bg="violet red").pack()
    Label(text="", bg="violet red").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen, font=('helvetica', 12)).pack()




       
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()     
    main_screen.destroy()
def delete_register_success():
    register_success_screen.destroy()
    register_screen.destroy()     
    
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
        
# ensure a file path was selected

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x300")
    main_screen.title("Account Login")
    main_screen.configure(background="Orange")
    Label(text="IMAGE RECOGNITION", width="300", height="2", font=("Calibri", 18, "bold"), fg="dark orange").pack()
    Label(text="LOGIN", bg="orange").pack()
    Button(text="Login", command = login, bg="dark orange1", fg="yellow", activebackground="white", font=('helvetica', 17), width=20).pack()
    Label(text="Register", bg="orange").pack()
    Button(text="Register", command=register, bg="Yellow", fg="dark orange1", activebackground="white", font=('helvetica', 17), width=20).pack()

    main_screen.mainloop()
 
 
main_account_screen()    
    


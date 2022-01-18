
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#login function

import csv 

#login UI
#window_login_register

import tkinter as tk
import tkinter.ttk as ttk

def buttonLoginPushed():
	
	userInfo='login_register for python practice_01152022.csv'	

	txtboxEntryEmail_value=txtboxEntryEmail.get()
	txtboxEntryPass_value=txtboxEntryPass.get()

	with open(userInfo) as f:
		infoList=csv.reader(f)

		emailInfo = txtboxEntryEmail_value
		passInfo = txtboxEntryPass_value

		for user in infoList:
			if user[0] == emailInfo:
				if user[1] == passInfo:
					frame_logined.tkraise()
					lblDisplayName['text']=user[2]
					lblDisplayAge['text']=user[3]
					lblDisplayHeight['text']=user[4]
					
			else:
				lblDisplayError['text']='error'

def buttonSignupPushed():
	
	frame_signup.tkraise()
	lblDisplayError.config(text='')

def buttonRegisterPushed():

	userInfo='login_register for python practice_01152022.csv'	

	newUserEmail=txtboxRegisterEmail.get()
	newUserPass=txtboxRegisterPass.get()
	newUserName=txtboxRegisterName.get()
	newUserAge=txtboxRegisterAge.get()
	newUserHeight=txtboxRegisterHeight.get()

	newUser=[newUserEmail,newUserPass,newUserName,newUserAge,newUserHeight]

	with open(userInfo,'a') as f:
		writer=csv.writer(f)
		writer.writerow(newUser)
		f.close()

	frame_login.tkraise()

	txtboxRegisterEmail.delete(0,tk. END)
	txtboxRegisterPass.delete(0,tk. END)
	txtboxRegisterName.delete(0,tk. END)
	txtboxRegisterAge.delete(0,tk. END)
	txtboxRegisterHeight.delete(0,tk. END)

def buttonBackPushed():

    frame_login.tkraise()
    lblDisplayError.config(text='')

    txtboxRegisterEmail.delete(0,tk. END)
    txtboxRegisterPass.delete(0,tk. END)
    txtboxRegisterName.delete(0,tk. END)
    txtboxRegisterAge.delete(0,tk. END)
    txtboxRegisterHeight.delete(0,tk. END)

def buttonLogoutPushed():
    
    frame_login.tkraise()
    
    txtboxEntryEmail.delete(0,tk. END)
    txtboxEntryPass.delete(0,tk. END)

    lblDisplayError.config(text='')


root=tk.Tk()
root.geometry('800x800')
root.title('Login_register')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#frame_login

frame_login = ttk.Frame(root)
frame_login.grid(row=0, column=0, sticky="nsew", pady=20)

#widget_login

buttonLogin=tk.Button(frame_login,text='Login',command=buttonLoginPushed)
buttonLogin.place(x=250,y=350)

buttonSignup=tk.Button(frame_login,text='Signup',command=buttonSignupPushed)
buttonSignup.place(x=250,y=400)

lblEntryEmail=tk.Label(frame_login,text='email')
lblEntryEmail.place(x=100,y=150)

txtboxEntryEmail=tk.Entry(frame_login,width=25)
txtboxEntryEmail.place(x=200,y=150)

lblEntryPass=tk.Label(frame_login,text='password')
lblEntryPass.place(x=100,y=250)

txtboxEntryPass=tk.Entry(frame_login,width=25)
txtboxEntryPass.place(x=200,y=250)

lblDisplayError=tk.Label(frame_login,text='')
lblDisplayError.place(x=250,y=450)

#frame_logined

frame_logined = ttk.Frame(root)
frame_logined.grid(row=0, column=0, sticky="nsew", pady=20)

#widget_logined

buttonLogout=tk.Button(frame_logined,text='Log out',command=buttonLogoutPushed)
buttonLogout.place(x=250,y=350)

lblDisplayName=tk.Label(frame_logined,text='Name')
lblDisplayName.place(x=200, y=200)

lblDisplayAge=tk.Label(frame_logined,text='Age')
lblDisplayAge.place(x=200, y=250)

lblDisplayHeight=tk.Label(frame_logined,text='Height')
lblDisplayHeight.place(x=200, y=300)

#frame_signup

frame_signup = ttk.Frame(root)
frame_signup.grid(row=0, column=0, sticky="nsew", pady=20)

#widget_signup

lblRegisterEmail=tk.Label(frame_signup,text='email')
lblRegisterEmail.place(x=100,y=150)

txtboxRegisterEmail=tk.Entry(frame_signup,width=25)
txtboxRegisterEmail.place(x=200,y=150)

lblRegisterPass=tk.Label(frame_signup,text='password')
lblRegisterPass.place(x=100,y=200)

txtboxRegisterPass=tk.Entry(frame_signup,width=25)
txtboxRegisterPass.place(x=200,y=200)

lblRegisterName=tk.Label(frame_signup,text='Name')
lblRegisterName.place(x=100,y=250)

txtboxRegisterName=tk.Entry(frame_signup,width=25)
txtboxRegisterName.place(x=200,y=250)

lblRegisterAge=tk.Label(frame_signup,text='Age')
lblRegisterAge.place(x=100,y=300)

txtboxRegisterAge=tk.Entry(frame_signup,width=25)
txtboxRegisterAge.place(x=200,y=300)

lblRegisterHeight=tk.Label(frame_signup,text='Height')
lblRegisterHeight.place(x=100,y=350)

txtboxRegisterHeight=tk.Entry(frame_signup,width=25)
txtboxRegisterHeight.place(x=200,y=350)

buttonRegister=tk.Button(frame_signup,text='Register',command=buttonRegisterPushed)
buttonRegister.place(x=250,y=400)

buttonBack=tk.Button(frame_signup,text='Back',command=buttonBackPushed)
buttonBack.place(x=250,y=450)

frame_login.tkraise()

root.mainloop()


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
			if user[1] == emailInfo:
				if user[2] == passInfo:
					frame_logined.tkraise()
					lblDisplayName['text']=user[3]
					lblDisplayAge['text']=user[4]
					lblDisplayHeight['text']=user[5]
					
				else:
					lblDisplayError['text']='error'


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

buttonLogin=tk.Button(frame_login,text='login',command=buttonLoginPushed)
buttonLogin.place(x=250,y=350)

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

buttonLogout=tk.Button(frame_logined,text='log out',command=buttonLogoutPushed)
buttonLogout.place(x=250,y=350)

lblDisplayName=tk.Label(frame_logined,text='name')
lblDisplayName.place(x=200, y=200)

lblDisplayAge=tk.Label(frame_logined,text='age')
lblDisplayAge.place(x=200, y=250)

lblDisplayHeight=tk.Label(frame_logined,text='height')
lblDisplayHeight.place(x=200, y=300)

frame_login.tkraise()

root.mainloop()















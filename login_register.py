
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#login function

import csv 

def buttonTestPushed():

	userInfo='login_register for python practice_01152022.csv'
	
	with open(userInfo) as f:
		reader=csv.reader(f)
		infoList = [row for row in reader]

	for x in range(len(infoList)):
		if x >0:
			lblDisplayName['text']=infoList[x][3]
			lblDisplayAge['text']=infoList[x][4]
			lblDisplayHeight['text']=infoList[x][5]

#login UI

#window_login_register

import tkinter as tk
import tkinter.ttk as ttk

def buttonLoginPushed():
    frame_logined.tkraise()

def buttonLogoutPushed():
    frame_login.tkraise()

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

lblEntryUserID=tk.Label(frame_login,text='userID')
lblEntryUserID.place(x=100,y=150)

txtboxEntryUserID=tk.Entry(frame_login,width=25)
txtboxEntryUserID.place(x=200,y=150)

lblEntryPass=tk.Label(frame_login,text='password')
lblEntryPass.place(x=100,y=250)

txtboxEntryPass=tk.Entry(frame_login,width=25)
txtboxEntryPass.place(x=200,y=250)

#frame_logined

frame_logined = ttk.Frame(root)
frame_logined.grid(row=0, column=0, sticky="nsew", pady=20)

#widget_logined

buttonDisplayTest=tk.Button(frame_logined,text='test',command=buttonTestPushed)
buttonDisplayTest.place(x=100,y=100)

buttonLogin=tk.Button(frame_logined,text='log out',command=buttonLogoutPushed)
buttonLogin.place(x=250,y=350)

lblDisplayName=tk.Label(frame_logined,text='name')
lblDisplayName.place(x=200, y=200)

lblDisplayAge=tk.Label(frame_logined,text='age')
lblDisplayAge.place(x=200, y=250)

lblDisplayHeight=tk.Label(frame_logined,text='height')
lblDisplayHeight.place(x=200, y=300)

frame_login.tkraise()

#labelDisplayError

root.mainloop()















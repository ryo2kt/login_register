#!/usr/bin/env python
# -*- coding: utf-8 -*-

#CSV 

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

import tkinter as tk

#login function

#login UI

root=tk.Tk()
root.geometry('800x800')
root.title('Login_register')

buttonLogin=tk.Button(root,text='login')
buttonLogin.place(x=250,y=350)

buttonDisplayTest=tk.Button(root,text='test',command=buttonTestPushed)
buttonDisplayTest.place(x=250,y=450)

lblEntryUserID=tk.Label(root,text='userID')
lblEntryUserID.place(x=100,y=150)

txtboxEntryUserID=tk.Entry(root,width=25)
txtboxEntryUserID.place(x=200,y=150)

lblEntryPass=tk.Label(root,text='password')
lblEntryPass.place(x=100,y=250)

txtboxEntryPass=tk.Entry(root,width=25)
txtboxEntryPass.place(x=200,y=250)

#labelDisplayInfo

lblDisplayName=tk.Label(root,text='name')
lblDisplayName.place(x=100, y=400)

lblDisplayAge=tk.Label(root,text='age')
lblDisplayAge.place(x=100, y=450)

lblDisplayHeight=tk.Label(root,text='height')
lblDisplayHeight.place(x=100, y=500)

#labelDisplayError

root.mainloop()















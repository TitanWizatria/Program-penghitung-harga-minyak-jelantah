#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *
from tkinter import ttk

def login():
    outfile=open('admin.txt','w')
    outfile.write(str(entri_un.get())+','+str(entri_pass.get()))
    outfile.close()
    root.destroy()

root = Tk()
root.title("Login")
root.eval('tk::PlaceWindow . center')

label_un=ttk.Label(root, text="Masukkan username di sini")
label_un.grid(column=0,row=0)
label_pass=ttk.Label(root, text="Masukkan password di sini")
label_pass.grid(column=0,row=2)
entri_un = StringVar()
entri_un = ttk.Entry(root)
entri_un.grid(column=0,row=1)
entri_pass = StringVar()
entri_pass = ttk.Entry(root, show="*")
entri_pass.grid(column=0,row=3)
button=ttk.Button(root, text="Klik disini!", command=login)
button.grid(column=0, row=4)

root.mainloop()


# In[ ]:





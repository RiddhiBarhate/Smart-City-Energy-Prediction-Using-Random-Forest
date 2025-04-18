import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="azure3")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x650+200+50")
root.title("Login Form")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('log.jpg')
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)






def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','electricity_demand.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')



title=tk.Label(root, text="Login Here",relief="solid", padx=5, pady=10, font=("Algerian", 30, "bold"),bd=5,bg="azure3",fg="black")
title.place(x=200,y=60,width=250)
        
Login_frame=tk.Frame(root,bg="azure3",relief="solid", borderwidth=2)
Login_frame.place(x=100,y=200)


#Login_frame = tk.Frame(root, bg="azure3", relief="solid", borderwidth=2)
#Login_frame.place(x=100, y=200, width=200, height=100)





        
logolbl=tk.Label(Login_frame,bd=0,relief="solid").grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",relief="solid", padx=5, pady=10,compound=LEFT,font=("Times new roman", 20, "bold"),bg="azure3").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username, font=("",15),bg="white")
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",relief="solid", padx=5, pady=10,compound=LEFT,font=("Times new roman", 20, "bold"),bg="azure3").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password, show="*",font=("",15),bg="white")
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",relief="solid", padx=5, pady=10,command=login,width=15,font=("Times new roman", 14, "bold"),bg="azure3",fg="black")
btn_log.grid(row=3,column=1,pady=10)

       

root.mainloop()
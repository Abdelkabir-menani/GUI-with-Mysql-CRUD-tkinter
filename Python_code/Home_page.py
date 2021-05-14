from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#A function that opens the student manager
def get_root1():
    home.destroy()
    import Etudiants_page

#A function that opens the branches manager
def get_root2():
    #Debut gestion des filières
    home.destroy()
    import Filières_page
    

# Creates the window of the Home page

home=Tk()
home.geometry('560x150')
home.title("Home")

#Creates the two buttons on the home page
# Edit the url of the location of the two images  

gest_etud_l=PhotoImage(file=r"C:\Users\lenovo\Desktop\Tkinter app\Images\1.png")
gest_etud=Button(home, image = gest_etud_l,command=get_root1)
gest_etud.place(x=10,y=40)

gest_fil_l=PhotoImage(file=r"C:\Users\lenovo\Desktop\Tkinter app\Images\2.png")
gest_fil=Button(home, image = gest_fil_l,command=get_root2)
gest_fil.place(x=280,y=40)

home.mainloop()

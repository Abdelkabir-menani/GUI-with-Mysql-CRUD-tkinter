from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#Opens the Home page

def get_home2():
    root2.destroy()
    import Home_page

#A function to insert a branch into the table filières 
    
def insert_filière():
    Id_filière=e_Id_filière.get()
    Nom_filière1=e_Nom_filière1.get();

    if (Id_filière=='' or Nom_filière1==''):
        MessageBox.showinfo('Insert status', "Veuillez entrer les information pour chaque case!")
    elif(Id_filière.isdecimal()==False):
        MessageBox.showinfo('Insert status', "Veuillez entrer un id valide pour la filière")    
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        syntax="INSERT INTO filières(Id_filière,Nom_filière) VALUES (%s,%s)"
        value = (Id_filière,Nom_filière1)
        cur.execute(syntax,value)
        cur.execute("commit")
        e_Id_filière.delete(0,'end')
        e_Nom_filière1.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root2.update()
        show_filières()
        MessageBox.showinfo('Insert status', "La filière est insérée avec succès")
        conn.close()

#A function to delete a branch from the table filières

def delete_filière():
    if (e_Id_filière.get()==''):
        MessageBox.showinfo('Delete status',"Entrer l'Id de la filière que vous voulez supprimer svp.")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("delete from filières where ID_Filière= '"+e_Id_filière.get()+"'")
        cur.execute("commit")
        e_Id_filière.delete(0,'end')
        e_Nom_filière1.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root2.update()
        show_filières()
        MessageBox.showinfo('Delete status', "La filière est supprimée avec succès")
        conn.close()

#A function to update the info of a branch

def update_filière():
    Id_filière=e_Id_filière.get()
    Nom_filière1=e_Nom_filière1.get();

    if (Id_filière=='' or Nom_filière1==''):
        MessageBox.showinfo('Update status', "Veuillez entrer les information pour chaque case!")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("update filières set Nom_filière='"+Nom_filière1+"' where Id_filière='"+Id_filière+"'")
        cur.execute("commit")
        e_Id_filière.delete(0,'end')
        e_Nom_filière1.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root2.update()
        show_filières()
        MessageBox.showinfo('Update status', "Les informations de la filière sont modifiées avec succès")
        conn.close()

#A function to get the info of a branch

def get_filière():
    if (e_Id_filière.get()==''):
        MessageBox.showinfo('Fetch status',"Entrer l'Id de la filière que vous voulez trouver svp.")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("select * from filières where Id_filière= '"+e_Id_filière.get()+"'")
        rows=cur.fetchall()

        for row in rows:
            e_Nom_filière1.insert(0,row[1])
                
        conn.close()

#A function to show the list of branches in the table filières
        
def show_filières():
    conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
    cur=conn.cursor()
    cur.execute("select * from filières ")
    rows=cur.fetchall()
    for row in rows:
        tree.insert('', 'end', values=(row[0], row[1]))
    conn.close()

#Creates the window of the branches manager
    
root2=Tk()
root2.geometry('380x405')
root2.title("Gestion des filières")

#Adding different info and entries of a branch
    
Id_filière=Label(root2,text="L'ID de la filière", font=("bold",10))
Id_filière.place(x=30,y=30)

Nom_filière1=Label(root2,text="Le nom de la filière", font=("bold",10))
Nom_filière1.place(x=30,y=50)

e_Id_filière=Entry(root2)
e_Id_filière.place(x=210,y=30)

e_Nom_filière1=Entry(root2)
e_Nom_filière1.place(x=210,y=50)

#Create the buttons of CRUD of a branch

insert5=Button(root2,text='Insérer',font=("italic",10),bg='LightSkyBlue3',command=insert_filière)
insert5.place(x=30,y=80,width = 70)

insert7=Button(root2,text='Modifier',font=("italic",10),bg='LightSkyBlue3',command=update_filière)
insert7.place(x=110,y=80,width = 70)

insert8=Button(root2,text='Trouver',font=("italic",10),bg='LightSkyBlue3',command=get_filière)
insert8.place(x=190,y=80,width = 70)

insert6=Button(root2,text='Supprimer',font=("italic",10),bg='LightSkyBlue3',command=delete_filière)
insert6.place(x=270,y=80,width = 70)

#Create the image that would get us to the home page
##Edit the url of the location of the image

home_logo=PhotoImage(file=r"C:\Users\lenovo\Desktop\Tkinter app\Images\Home_page.png")
home_page=Button(root2, image = home_logo,command=get_home2)
home_page.place(x=160,y=350)

#Adding info of the branches on a tree that will let us show data on a table with columns.

tree = ttk.Treeview(root2, column=("c1", "c2"), show='headings')

tree.column("#1", anchor=CENTER,width=50)
tree.heading("#1", text="ID")
    
tree.column("#2", anchor=CENTER,width=260)
tree.heading("#2", text="Nom de filière")
    
tree.place(x=30,y=120)

#Add a little scrollbar to the right of the table created

vsb = ttk.Scrollbar(root2, orient="vertical", command=tree.yview)
vsb.place(x=353, y=110, height=250)

tree.configure(yscrollcommand=vsb.set)

show_filières()

root2.mainloop()

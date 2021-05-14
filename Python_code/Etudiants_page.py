from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

#Opens the Home page

def get_home1():
    root1.destroy()
    import Home_page

#A function to insert a student into the table Etudiants with his different info(id,fname,lname,age,branch)

def insert_étudiant():
    id_etudiant=e_id_etudiant.get()
    Prénom=e_Prénom.get();
    Nom=e_Nom.get();
    Age=e_Age.get();
    Nom_filière=combo.get()

    if (id_etudiant=='' or Prénom=='' or Nom=='' or Age=='' or Nom_filière==''):
        MessageBox.showinfo('Insert status', "Veuillez entrer les information pour chaque case!")
    elif(Age=='0' or Age.isdecimal()==False):
        MessageBox.showinfo('Insert status', "Veuillez entrer un age valide pour l'étudiant")
    elif(id_etudiant.isdecimal()==False):
        MessageBox.showinfo('Insert status', "Veuillez entrer un id valide pour l'étudiant")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        syntax = """insert into Etudiants(id_etudiant,Prénom,Nom,Age,Nom_filière) values(%s,%s,%s,%s,%s)"""
        value = (id_etudiant,Prénom,Nom,Age,Nom_filière)
        cur.execute(syntax,value)
        cur.execute("commit")
        e_id_etudiant.delete(0,'end')
        e_Prénom.delete(0,'end')
        e_Nom.delete(0,'end')
        e_Age.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root1.update()
        show_étudiants()
        combo.set('')
        MessageBox.showinfo('Insert status', "L'étudiant est inséré avec succès")
        conn.close()
                
#A function to delete a student from the table Etudiants
        
def delete_étudiant():
    if (e_id_etudiant.get()==''):
        MessageBox.showinfo('Delete status',"Entrer l'Id de l'étudiant que vous voulez supprimer svp.")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("delete from Etudiants where id_etudiant= '"+e_id_etudiant.get()+"'")
        cur.execute("commit")
        e_id_etudiant.delete(0,'end')
        e_Prénom.delete(0,'end')
        e_Nom.delete(0,'end')
        e_Age.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root1.update()
        show_étudiants()
        combo.set('')
        MessageBox.showinfo('Delete status', "L'étudiant est supprimé avec succès")
        conn.close()

#A function to update the info of a student
            
def update_étudiant():
    id_etudiant=e_id_etudiant.get()
    Prénom=e_Prénom.get();
    Nom=e_Nom.get();
    Age=e_Age.get();
    Nom_filière=combo.get();

    if (id_etudiant=='' or Prénom=='' or Nom=='' or Age=='' or Nom_filière==''):
        MessageBox.showinfo('Update status', "Veuillez entrer les information pour chaque case!")
    elif(Age==0):
        MessageBox.showinfo('Update status', "Veuillez entrer un age valide pour l'étudiant")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("update Etudiants set Prénom='"+Prénom+"',Nom='"+Nom+"',Age='"+Age+"',Nom_filière='"+Nom_filière+"' where id_etudiant='"+id_etudiant+"'")
        cur.execute("commit")
        e_id_etudiant.delete(0,'end')
        e_Prénom.delete(0,'end')
        e_Nom.delete(0,'end')
        e_Age.delete(0,'end')
        for i in tree.get_children():
            tree.delete(i)
        root1.update()
        show_étudiants()
        combo.set('')
        MessageBox.showinfo('Update status', "Les informations de l'étudiant sont modifiées avec succès")
        conn.close()
        
#A function to get the info of a student            

def get_étudiant():
    if (e_id_etudiant.get()==''):
        MessageBox.showinfo('Fetch status',"Entrer l'Id de l'étudiant que vous voulez trouver svp.")
    else:
        conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
        cur=conn.cursor()
        cur.execute("select * from Etudiants where id_etudiant= '"+e_id_etudiant.get()+"'")
        rows=cur.fetchall()
        for row in rows:
            e_Prénom.insert(0,row[1])
            e_Nom.insert(0,row[2])
            e_Age.insert(0,row[3])
            combo.set(row[4])

#A function to show the list of students in the table Etudiants           
    
def show_étudiants():
    conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
    cur=conn.cursor()
    cur.execute("select * from Etudiants ")
    rows=cur.fetchall()
    for row in rows:
        tree.insert('', 'end', values=(row[0], row[1], row[2],row[3],row[4]))
    conn.close()
    

#Creates the window of the student manager

root1=Tk()
root1.geometry('380x470')
root1.title("Gestion des étudiants")

#Adding different info and entries of a student

id_etudiant=Label(root1,text="L'ID de l'étudiant", font=("bold",10))
id_etudiant.place(x=30,y=30)

Prénom=Label(root1,text="Le prénom de l'étudiant", font=("bold",10))
Prénom.place(x=30,y=50)

Nom=Label(root1,text="Le nom de l'étudiant", font=("bold",10))
Nom.place(x=30,y=70)

Age=Label(root1,text="L'age de l'étudiant", font=("bold",10))
Age.place(x=30,y=90)

Nom_filière=Label(root1,text="Nom de la filière", font=("bold",10))
Nom_filière.place(x=30,y=110)

e_id_etudiant=Entry(root1)
e_id_etudiant.place(x=210,y=30)

e_Prénom=Entry(root1)
e_Prénom.place(x=210,y=50)

e_Nom=Entry(root1)
e_Nom.place(x=210,y=70)

e_Age=Entry(root1)
e_Age.place(x=210,y=90)

#Get the branch from a Combobox that contains the list of branches on the table filières

filière_var = StringVar()
combo=ttk.Combobox(root1,width=17,textvariable=filière_var)
conn=mysql.connect(host='localhost', user='Project',password='.', database='Etudiant')
cur=conn.cursor()
cur.execute("select * from filières ")
rows=cur.fetchall()
m=[]
for row in rows:
    m.append(row[1])
    conn.close()
    
combo['values']=m
combo.place(x=210,y=110)

#Create the buttons of CRUD of a student

insert1=Button(root1,text='Insérer',font=("italic",10),bg='LightSkyBlue3',command=insert_étudiant)
insert1.place(x=30,y=140,width = 70)
    
insert3=Button(root1,text='Modifier',font=("italic",10),bg='LightSkyBlue3',command=update_étudiant)
insert3.place(x=110,y=140,width = 70)

insert4=Button(root1,text='Trouver',font=("italic",10),bg='LightSkyBlue3',command=get_étudiant)
insert4.place(x=190,y=140,width = 70)

insert2=Button(root1,text='Supprimer',font=("italic",10),bg='LightSkyBlue3',command=delete_étudiant)
insert2.place(x=270,y=140,width = 70)

#Create the image that would get us to the home page
##Edit the url of the location of the image

home_logo=PhotoImage(file=r"C:\Users\lenovo\Desktop\Tkinter app\Images\Home_page.png")
home_page=Button(root1, image = home_logo,command=get_home1)
home_page.place(x=160,y=410)

#Adding info of the students on a tree that will let us show data on a table with columns..

tree = ttk.Treeview(root1, column=("c1", "c2", "c3","c4",'c5'), show='headings')

tree.column("#1", anchor=CENTER,width=60)
tree.heading("#1", text="ID")

tree.column("#2", anchor=CENTER,width=60)
tree.heading("#2", text="Prénom")
    
tree.column("#3", anchor=CENTER,width=60)
tree.heading("#3", text="Nom")
    
tree.column("#4", anchor=CENTER,width=60)
tree.heading("#4", text="Age")
    
tree.column("#5", anchor=CENTER,width=90)
tree.heading("#5", text="Nom de filière")
tree.place(x=20,y=180)

#Add a little scrollbar to the right of the table created

vsb = ttk.Scrollbar(root1, orient="vertical", command=tree.yview)
vsb.place(x=353, y=160, height=250)

tree.configure(yscrollcommand=vsb.set)
    
    

show_étudiants()
    
root1.mainloop()

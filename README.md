# GUI with Mysql CRUD tkinter:

## 1-Tools:

### MYSQL:

for the connexion of the database

### Tkinter:

Which is a python library that allow us to create GUI (Graphical User Interface)

## 2-Requirements:

### Creation of a user with all priviliges(optional)

Creating a user with all privileges on Mysql for me i created a user with the username(Project) and password(.) on localhost

![Mysql_user.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/Mysql_user.png)

### Creation of the database

Connect to Mysql with the user you just created and create a database called etudiant for example and the the tables containg it using the code in the Mysql folder

So you are ready to execute the code..

## 3-The application:

### 3-1: The home page:

View of the Home page

![home.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/home.png)

### 3-1: The student manager page:

View of the student manager page

![student_manager_page.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/student_manager_page.png)


### 3-2: The branch manager page:

View of the branch manager page

![branch_manager_page.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/branch_manager_page.png)

### Buttons:

#### The insert button:

We insert a student to the table etudiants by adding his info (id,fname,lname,age,branch). The branch is selected from the list of the branches existed on the table filières of the database we created.

![insert_student.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/insert_student.png)

And on the The branch manager page

![insert_branch.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/insert_branch.png)

#### The delete button:

The delete button works by typing the id of the student or the branch we want to delete.

On the The student manager page

![delete_student.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/delete_student.png)

And on the The branch manager page

![delete_branch.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/delete_branch.png)

#### The update button:

The update button works by adding the info of the id of the student we want to update his info

On the The student manager page, the update looks like this

![update_student.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/update_student.png)

And on the The branch manager page

![update_branch.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/update_branch.png)

#### The get button:

The get button allows us to find all the info of a student or a branch displayed on the screen

On the The student manager page

![get_student.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/get_student.png)

And on the The branch manager page

![get_branch.png](https://github.com/Abdelkabir-menani/GUI-with-Mysql-CRUD-tkinter/blob/main/Images/get_branch.png)







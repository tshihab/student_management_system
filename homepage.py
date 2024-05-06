import tkinter
from tkinter import *
from tkinter import messagebox
from dbms import *
from DataView import *


# Welcome Window
class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("650x400")

        # heading
        Label(self.root, text='Student Management System', fg="Dodgerblue", font=('Arial', 24, 'bold'), border=4, relief=GROOVE).pack(side=TOP, fill=X)

        # login buttons
        student_login = Button(self.root, text="Student Login", command=self.studentLogin, bg="Thistle", height=2, width=15)
        student_login.pack(padx=20, pady=(100, 0))

        teacher_login = Button(self.root, text="Teacher Login", command=self.teacherLogin, bg="Thistle", height=2, width=15)
        teacher_login.pack(padx=20, pady=20)
    

    def studentLogin(self):
        # destroying all pages to show studentInfo
        for widget in self.root.winfo_children():
            widget.destroy()

        # opening student login page
        StudentLoginWindow(self.root)


    def teacherLogin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        TeacherLoginWindow(self.root)


# Student Login Page
class StudentLoginWindow:
    def __init__(self, root):
        # dbms connection
        self.stuDB = StudentDB()

        self.root = root
        self.root.title("Student Login")
        self.root.resizable(False, False)
        
        # heading
        Label(self.root, text='Student Login', fg="Dodgerblue", font=('Arial', 24, 'bold'), border=4, relief=GROOVE).grid(row=0, column=0, columnspan=2, sticky="ew")

        # labels and entry widgets
        Label(self.root, text="Student ID").grid(row=1, column=0, padx=10, pady=(65, 10), sticky="e")
        Label(self.root, text="Registration").grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.getID = Entry(self.root, width=40)
        self.getID.grid(row=1, column=1, padx=(0, 20), pady=(65, 10))

        self.getReg = Entry(self.root, width=40)
        self.getReg.grid(row=2, column=1, padx=(0, 20), pady=10)

        # Setting column weights to make entry widgets and labels centered
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        Button(self.root, text="Back", command=self.back, bg="#76D7C4", height=2, width=12).place(x=230, y=230)
        Button(self.root, text="Submit", command=self.submit, bg="#76D7C4", height=2, width=12).place(x=380, y=230)


    def back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # back to the welcome screen
        HomePage(self.root)


    def submit(self):        
        login_data = {}
        login_data["sid"] = self.getID.get()
        login_data["registration"] = self.getReg.get()

        self.stu_info = self.stuDB.getStudent(login_data)
        
        if self.stu_info != None:
            for widget in self.root.winfo_children():
                widget.destroy()
            
            self.showInformation()
        
        else:
            messagebox.showerror("Error", "No data found!")
            

    def showInformation(self):
        self.root.title("Individual Information")
        self.root.geometry("650x580")
        Label(self.root, text='Student Information', fg="Dodgerblue", font=('Arial', 24, 'bold'), border=4, relief=GROOVE).grid(row=0, column=0, columnspan=2, sticky="ew")
        
        field_label = ["Student ID", "Name", "Roll", "Registration", "Session", "Mobile", "Gender", "Course", "Subject"]
        
        y_axis = 100
        for labels in field_label:
            Label(self.root, text=labels, font=("Arial", 12, "bold")).place(x=100, y=y_axis)
            y_axis += 45
        
        y_axis = 100
        for info in self.stu_info:
            Label(self.root, text=f":\t{info}", font=("Arial", 12, "italic")).place(x=250, y=y_axis)
            y_axis += 45
        

        Button(self.root, text="Back", command=self.back, bg="#76D7C4", height=2, width=12).place(x=100, y=530)
        

# Teacher login page
class TeacherLoginWindow:
    def __init__(self, root):

        self.root = root
        self.root.title("Teacher Login")
        self.root.resizable(False, False)
        
        ## heading
        Label(self.root, text='Teacher Login', fg="Dodgerblue", font=('Arial', 24, 'bold'), border=4, relief=GROOVE).grid(row=0, column=0, columnspan=2, sticky="ew")

        ## labels and entry widgets
        Label(self.root, text="Username").grid(row=1, column=0, padx=10, pady=(65, 10), sticky="e")
        Label(self.root, text="Password").grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.getID = Entry(self.root, width=40)
        self.getID.grid(row=1, column=1, padx=(0, 20), pady=(65, 10))

        self.getReg = Entry(self.root, width=40)
        self.getReg.grid(row=2, column=1, padx=(0, 20), pady=10)

        # Setting column weights to make entry widgets and labels centered
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        Button(self.root, text="Back", command=self.back, bg="#76D7C4", height=2, width=12).place(x=230, y=230)
        Button(self.root, text="Submit", command=self.submit, bg="#76D7C4", height=2, width=12).place(x=380, y=230)


    def back(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        HomePage(self.root)


    def submit(self):        
        login_data = {}
        login_data["username"] = self.getID.get()
        login_data["password"] = self.getReg.get()
        
        if login_data["username"] == "Tshihab07" and login_data["password"] == "2116":
            self.root.destroy()
            TeacherPanel(Tk())
        
        else:
            messagebox.showerror("Error", "No data found!")

            

root = Tk()
w1 = HomePage(root)
root.mainloop()
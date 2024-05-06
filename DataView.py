""" Data Entry Page """
# Importing Modules
# import tkinter
from tkinter import ttk, messagebox
from dbms import *
from tkinter import *

class TeacherPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Page")
        self.root.geometry("1300x1020")

        ############# heading of the program #############
        Label(self.root, text='Student Management System', fg="Dodgerblue", font=('Arial', 24, 'bold'), border=4, relief=GROOVE).pack(side=TOP, fill=X)

        # initializing Frames
        # Entry Frame
        self.dataEntryframe = LabelFrame(self.root, text=" Enter Student Details ".center(50, "-"), font=("Helvetica", 16, "bold"), bg="DarkGray", relief=FLAT)
        self.dataEntryframe.place(x=0, y=45, width=425, height=1050)

        # Data Frame
        self.dataViewframe = LabelFrame(self.root, text=" All Students Data ".center(114, '-'), font=("Arial", 16, 'bold'), bg="LightGray", relief=FLAT)
        self.dataViewframe.place(x=430, y=45, width=1300, height=1050)

        # listbox to show data
        self.listbox = ttk.Treeview(self.dataViewframe)

        # object of database file
        self.mydb = StudentDB()
        self.mydb.dbTable()

        # app interface
        self.entryWidget()
    

    def entryWidget(self):
        #############  attribute labels  #############
        field_label = ["Student ID", "Full Name", "Roll No", "Registration", "Session", "Mobile", "Gender"]
        y_axis = 30
        for txt in field_label:
            Label(self.dataEntryframe, text=txt, bg="DarkGray").place(x=10, y=y_axis)
            y_axis += 30
        
        Label(self.dataEntryframe, text="Select Course", bg="DarkGray").place(x=10, y=300)
        Label(self.dataEntryframe, text="Select Subject", bg="DarkGray").place(x=200, y=300)

        
        #############  read basic input from user  #############
        self.student_id = Entry(self.dataEntryframe, width=40)
        self.student_id.place(x=120, y=30)
        self.student_id.bind('<Button-1>', self.addEvent)

        self.name = Entry(self.dataEntryframe, width=40)
        self.name.place(x=120, y=60)
        # self.name.bind('<Button-1>', self.addEvent)

        self.roll = Entry(self.dataEntryframe, width=40,)
        self.roll.place(x=120, y=90)
        # self.roll.bind('<Button-1>', self.addEvent)

        self.registration = Entry(self.dataEntryframe, width=40,)
        self.registration.place(x=120, y=120)
        # self.registration.bind('<Button-1>', self.addEvent)

        self.session = Entry(self.dataEntryframe, width=40)
        self.session.place(x=120, y=150)
        # self.session.bind('<Button-1>', self.addEvent)

        self.mobile = Entry(self.dataEntryframe, width=40)
        self.mobile.place(x=120, y=180)
        # self.mobile.bind('<Button-1>', self.addEvent)

        self.gender = StringVar(self.dataEntryframe, " ")
        Radiobutton(self.dataEntryframe, text="Male", variable=self.gender, value="Male", font=("", 10), bg="DarkGray").place(x=120, y=210)
        Radiobutton(self.dataEntryframe, text="Female", variable=self.gender, value="Female", font=("", 10), bg="DarkGray").place(x=200, y=210)
        Radiobutton(self.dataEntryframe, text="Others", variable=self.gender, value="Others", font=("", 10), bg="DarkGray").place(x=280, y=210)
    
        ############# department selection #############
        Label(self.dataEntryframe, text=" Choose Department ".center(45, '-'), font=("Helvetica", 16, "bold"), bg='DarkGray').place(x=10, y=260)
        self.ComboBox(self.dataEntryframe, 10, 200, 325, 325)

        #############  setting up buttons  #############
        Button(self.dataEntryframe, text="Add", command=self.AddAction, height=2, width=15).place(x=80, y=420)
        Button(self.dataEntryframe, text="Update", command=self.UpdateAction, height=2, width=15).place(x=220, y=420)
        Button(self.dataEntryframe, text="Delete", command=self.DeleteAction, height=2, width=15).place(x=80, y=480)
        Button(self.dataEntryframe, text="View Data", command=self.viewAllData, height=2, width=15).place(x=220, y=480)
        Button(self.dataEntryframe, text="Refresh", command=self.entryWidget, height=2, width=15).place(x=140, y=540)

    
    ############# combobox setup #############
    def ComboBox(self, frame, x_pos1, x_pos2, y_pos1, y_pos2):
        self.generalSubjects = ["Bangla", "English", "Mathematics", "Phsyics", "History", "Statistics"]
        self.professionalSubjects = ["CSE", "BBA", "Tourism and Hospitality", "Media and Theatre"]

        # combobox for course selection
        self.course = ttk.Combobox(frame, width= 25, values=["General", "Professional"], state='readonly')
        
        self.course.set("Select Course")                                    # combobox title
        self.course.place(x=x_pos1, y=y_pos1)                               # combobox position
        self.course.bind("<<ComboboxSelected>>", self.subject_choice)       # combobox selection event

        # combobox for subject
        self.subject = ttk.Combobox(frame, width= 25, state='readonly')
        self.subject.set("Select Subject")
        self.subject.place(x=x_pos2, y=y_pos2)
    
    
    ############# combobox selection functionality #############
    def subject_choice(self, event):
        if self.course.get() == "General":
            self.subject['values'] = self.generalSubjects
            self.subject.set("Select Subject")
        
        elif self.course.get() == "Professional":
            self.subject['values'] = self.professionalSubjects
            self.subject.set("Select Subject")
    
    
    ############# getter method of the values #############
    def getData(self):
        s_id = self.student_id.get()
        s_name = self.name.get().strip()
        s_roll = self.roll.get()
        s_reg = self.registration.get().strip()
        session = self.session.get()
        mobile = self.mobile.get()
        gender = self.gender.get()
        crs = self.course.get()
        sub = self.subject.get()
        
        return s_id, s_name, s_roll, s_reg, session, mobile, gender, crs, sub
    
    
    ############# clearing input fields #############
    def clearEntries(self):
        self.student_id.delete(0, END)
        self.name.delete(0, END)
        self.roll.delete(0, END)
        self.registration.delete(0, END)
        self.session.delete(0, END)
        self.mobile.delete(0, END)

        self.student_id.focus_set()
        self.gender.set(None)
        self.course.set("Select Course")
        self.subject.set("Select Subject")
    

    ############# add button action #############
    def AddAction(self):
        data = self.getData()
        self.mydb.addData(data)
        self.clearEntries()
        self.viewAllData()


    ############# update button action #############
    def UpdateAction(self):
        data = self.getData()
        self.mydb.updateData(data)
        self.clearEntries()
        self.viewAllData()
    

    ############# delete button action #############
    def DeleteAction(self):
        sid = self.student_id.get()
        self.mydb.deleteData(sid)
        self.clearEntries()
        self.viewAllData()

    
    ############# displaying records #############
    def DisplayRecord(self):
        self.listbox.delete(*self.listbox.get_children())
        try:
            self.listbox.delete(*self.listbox.get_children())
            rows = self.mydb.allData()
            for r in rows:
                self.listbox.insert("", "end", values=r)        
        
        except Exception as expt:
            print(expt)
            messagebox.showerror("Error", expt)

    
    ############# preparing adding items #############
    def addEvent(self, event):
        self.ComboBox(self.dataEntryframe, 10, 200, 325, 325)

    
    ############# get items from row #############
    def getEvent(self, event):
        self.clearEntries()
        self.ComboBox(self.dataEntryframe, 10, 200, 325, 325)  # calling the combobox from entry field
        
        row = self.listbox.selection()[0]                  # get selected item
        select = self.listbox.set(row)                     # get data from selected item
        # print(select)
        
        self.student_id.insert(0, select["Student ID"])
        self.name.insert(0, select["Name"])
        self.roll.insert(0, select["Roll"])
        self.registration.insert(0, select["Registration"])
        self.session.insert(0, select["Session"])
        self.mobile.insert(0, select["Mobile"])
        
        self.gender.set(select["Gender"])                  # set the gender based on the selected data
        self.course.set(select["Course"])                  # Set the course based on the selected data
        self.subject_choice(None)                          # Update the available subjects in the subject combobox based on the selected course
        self.subject.set(select["Subject"])                # Set the subject based on the selected data

    
    def viewAllData(self):
        ############# search data #############
        Label(self.dataViewframe, text="Roll: ", font=("", 10), bg="LightGray").place(x=5, y=20)
        self.searchByroll = Entry(self.dataViewframe, width=20)
        self.searchByroll.place(x=40, y=20)
        self.ComboBox(self.dataViewframe, 200, 410, 20, 20)
        Button(self.dataViewframe, text="Search", command=self.searchAction, height=1, width=10).place(x=630, y=18)
        Button(self.dataViewframe, text="Refresh", command=self.viewAllData, height=1, width=10).place(x=730, y=18)
        

        ############# displaying records #############
        cols = ("Student ID", "Name", "Roll", "Registration", "Session", "Mobile", "Gender", "Course", "Subject")
        cols_width = (90, 130, 50, 90, 70, 100, 80, 80, 150)
        self.listbox = ttk.Treeview(self.dataViewframe, columns=cols, show="headings", height=25)

        for c, w in zip(cols, cols_width):
            self.listbox.heading(c, text=c)
            self.listbox.column(c, width=w)
            self.listbox.grid(row=1, column=0)
            self.listbox.place(x=5, y=80)
        
        
        ############# scrollbar setup #############
        scrollbar = Scrollbar(self.dataViewframe, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.grid(row=1, column=0, sticky=NSEW, padx=(5,0), pady=(80, 0))
        scrollbar.grid(row=1, column=1, sticky=NS, pady=(80, 0))
        
        self.DisplayRecord()
        self.listbox.bind('<Double-Button-1>', self.getEvent)



    def searchAction(self):
        # search items
        roll = self.searchByroll.get()
        course = self.course.get()
        subject = self.subject.get()
        
        # Clear the current contents of the Treeview
        self.listbox.delete(*self.listbox.get_children())
        
        try:
            search_result = self.mydb.DataSearch(roll, course, subject)
            
            if search_result:
                for row in search_result:
                    self.listbox.insert("", "end", values=row)

            else:
                messagebox.showerror("Error", "No data found!")
                self.searchByroll.delete(0, END)
                self.course.set("Select Course")
                self.subject.set("Select Subject")

                self.DisplayRecord()

        
        except Exception as expt:
            print(expt)
            messagebox.showerror("Error", expt)




# root = Tk()
# TeacherPanel(root)
# root.mainloop()
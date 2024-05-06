import mysql.connector
from tkinter import messagebox

class StudentDB:
    def __init__(self):
        # Creating a Database Connection
        self.connection = mysql.connector.connect(host="localhost", user="root", password="", database="studentdb")
        self.db_cursor = self.connection.cursor()
    

    def dbTable(self):
        try:
            self.db_cursor.execute("""CREATE TABLE IF NOT EXISTS student_data (
                                   sid VARCHAR(20) PRIMARY KEY,
                                   name VARCHAR(30),
                                   roll INT,
                                   registration VARCHAR(20) UNIQUE,
                                   session VARCHAR(15),
                                   mobile VARCHAR(15),
                                   gender VARCHAR(10),
                                   course VARCHAR(30),
                                   subject VARCHAR(30)
                                   )""")
            
            self.connection.commit()
        
        except Exception as expt:
            print(expt)
            self.connection.rollback()
    
    
    """ Implement database actions"""
    def addData(self, data):

        try:
            # checking existing StudentID
            self.db_cursor.execute("SELECT sid FROM student_data WHERE sid = %s", (data[0],))
            
            if self.db_cursor.fetchone():
                messagebox.showerror('Error', "Student ID already exists")
            
            else:
                # sql command to add data into database
                self.db_cursor.execute("""INSERT INTO student_data 
                                       (sid, name, roll, registration, session, mobile, gender, course, subject) 
                                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", data)
                
                self.connection.commit()
                messagebox.showinfo('Successful','Record Added Successfully')

        
        except Exception as expt:
            print(expt)
            self.connection.rollback()
        

    def updateData(self, data):

        try:
            # execute command operation with the data on the selected fields
            self.db_cursor.execute("""UPDATE student_data
                               SET name = %s, roll = %s, registration = %s,
                               session = %s, mobile = %s, gender = %s,
                               course = %s, subject = %s
                               WHERE sid = %s""",
                               (data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[0]))
            self.connection.commit()

            # message box that confirm updates
            messagebox.showinfo("Information", "Record updated successfully!")

        
        except Exception as e:
            print(e)
            self.connection.rollback()

    
    def deleteData(self, sid):
        try:
            self.db_cursor.execute("DELETE FROM student_data WHERE sid = %s", (sid,))
            self.connection.commit()
            messagebox.showinfo("Information", "Record deleted successfully!")

        
        except Exception as expt:
            print(expt)
            self.connection.rollback()
    

    def allData(self):
        try:
            self.db_cursor.execute("SELECT * FROM student_data")
            rows = self.db_cursor.fetchall()
            return rows
        
        except Exception as expt:
            print(expt)
            return []
    

    def DataSearch(self, roll, course, subject):
        try:
            # Search query to find rows with the specified roll, course, and subject
            self.db_cursor.execute("SELECT * FROM student_data WHERE roll = %s AND course = %s AND subject = %s", (roll, course, subject))
            rows = self.db_cursor.fetchall()
            return rows
        
        except Exception as expt:
            print(expt)
            return []
    

    """ implemeting login data """
    def getStudent(self, login_info):
        self.db_cursor.execute("SELECT * FROM student_data WHERE sid = %s AND registration = %s", (login_info["sid"], login_info["registration"]))
        return self.db_cursor.fetchone()



# sdb1 = StudentDB()
# print(sdb1.allData())
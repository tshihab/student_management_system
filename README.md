# Student Management System

A simple Student Management System built using Python tkinter and MySQL Connector.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a simple Student Management System developed using Python's tkinter library for the GUI and MySQL Connector for database interaction. It allows users to add, update, delete, and view student records. The system includes both a student login and a teacher login, with different levels of access.

The project consists of three main files:

- `homepage.py`: This file contains the main GUI for the application, including the login screens for students and teachers.
- `dataView.py`: This file contains the interface for teachers to add, update, delete, and view student records. It also includes the functionality to search for students by roll, course, and subject.
- `dbms.py`: This file contains the database management functions, including adding, updating, deleting, and retrieving student records from the MySQL database.

## Features

- **Add New Student Records**: Teachers can add new student records by entering the student's details, including Student ID, Name, Roll No, Registration number, Session, Mobile number, Gender, Course, and Subject.
- **Update Existing Student Records**: Teachers can update existing student records by selecting the record from the list and modifying the details.
- **Delete Student Records**: Teachers can delete student records by selecting the record from the list and deleting it.
- **View All Student Records**: Teachers can view all student records stored in the database.
- **Search for Students**: Teachers can search for students by roll number, course, and subject.
- **Student Login**: Students can log in using their Student ID and Registration number to view their information.

## Screenshots

![Welcome Page](images/welcome_page.png)
![Student Login](images/student_login.png)
![Individual Data](images/individual_information.png)
![Individual Data](images/individual_information.png)
![Teacher's Login](images/teachers_login.png)
![Data Entry Page](images/data_entry_page.png)
![View All Data](images/view_all_data.png)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tshihab/student_management_system.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd student_management_system
    ```

3. **Install the required dependencies:**

    ```bash
    pip install mysql-connector-python
    pip install tkinter
    ```

4. **Set up the database:**
   - Make sure you have MySQL installed and create a database named `studentdb`.
   - Import the `studentdb.sql` file into your database to create the necessary table.

5. **Run the application:**

    ```bash
    python homepage.py
    ```

## Usage

- When you run the `homepage.py` file, you will see the Welcome window.
- You can log in as either a student or a teacher.
- **Student Login**:
  - Students can log in using their Student ID and Registration number to view their information.
- **Teacher Login**:
  - Teachers can add, update, delete, and view student records.
  - Teachers can search for students by roll, course, and subject.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

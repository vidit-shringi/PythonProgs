import mysql.connector
from tkinter import *

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="employees"
)

# Create a cursor object
mycursor = mydb.cursor()

# Define a function to insert employee information into the database
def insert_employee():
    # Get the employee information from the GUI
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    salary = salary_entry.get()

    # Insert the employee information into the database
    sql = "INSERT INTO employee_info (name, age, gender, salary) VALUES (%s, %s, %s, %s)"
    val = (name, age, gender, salary)
    mycursor.execute(sql, val)
    mydb.commit()

# Create the Tkinter GUI
root = Tk()

name_label = Label(root, text="Name")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

age_label = Label(root, text="Age")
age_label.pack()
age_entry = Entry(root)
age_entry.pack()

gender_label = Label(root, text="Gender")
gender_label.pack()
gender_entry = Entry(root)
gender_entry.pack()

salary_label = Label(root, text="Salary")
salary_label.pack()
salary_entry = Entry(root)
salary_entry.pack()

submit_button = Button(root, text="Submit", command=insert_employee)
submit_button.pack()

root.mainloop()



"""(MYSQL Command)
CREATE DATABASE employees;
USE employees;
CREATE TABLE employee_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    salary FLOAT
);
"""

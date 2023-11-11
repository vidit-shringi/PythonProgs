import pandas as pd
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("500x500")
root.title("Student Information")
df = pd.DataFrame(columns=["Name", "Roll No.", "Marks"])
def add_student():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    marks = marks_entry.get()
    df.loc[len(df)] = [name, roll_no, marks]
    name_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
def display_student():
    display_window = tk.Toplevel(root)
    display_window.geometry("500x500")
    display_window.title("Student Information")
    tree = ttk.Treeview(display_window)
    tree.pack(side=tk.LEFT, fill=tk.BOTH)
    tree["columns"] = ["Name", "Roll No.", "Marks"]
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Name", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("Roll No.", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("Marks", width=150, minwidth=150, anchor=tk.CENTER)
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("Name", text="Name", anchor=tk.CENTER)
    tree.heading("Roll No.", text="Roll No.", anchor=tk.CENTER)
    tree.heading("Marks", text="Marks", anchor=tk.CENTER)
    for index, row in df.iterrows():
        tree.insert("", 0, text="", values=list(row))
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

roll_no_label = tk.Label(root, text="Roll No.:")
roll_no_entry = tk.Entry(root)

marks_label = tk.Label(root, text="Marks:")
marks_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add", command=add_student)
display_button = tk.Button(root, text="Display", command=display_student)
name_label.pack()
name_entry.pack()

roll_no_label.pack()
roll_no_entry.pack()

marks_label.pack()
marks_entry.pack()

add_button.pack()
display_button.pack()
root.mainloop()

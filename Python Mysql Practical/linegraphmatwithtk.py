import tkinter as tk
import matplotlib.pyplot as plt
root = tk.Tk()
root.geometry("500x500")
root.title("Student Information")
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

roll_no_label = tk.Label(root, text="Roll No.:")
roll_no_entry = tk.Entry(root)

marks_label = tk.Label(root, text="Marks:")
marks_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add")
display_button = tk.Button(root, text="Display")
def display_student():
    fig, ax = plt.subplots()
    ax.plot(df["Roll No."], df["Marks"])
    ax.set_xlabel("Roll No.")
    ax.set_ylabel("Marks")
    ax.set_title("Student Information")
    plt.show()
import pandas as pd

df = pd.DataFrame(columns=["Name", "Roll No.", "Marks"])

def add_student():
    name = name_entry.get()
    roll_no = roll_no_entry.get()
    marks = marks_entry.get()
    df.loc[len(df)] = [name, roll_no, marks]
    name_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
name_label.pack()
name_entry.pack()

roll_no_label.pack()
roll_no_entry.pack()

marks_label.pack()
marks_entry.pack()

add_button.pack()
add_button.config(command=add_student)

display_button.pack()
display_button.config(command=display_student)
root.mainloop()

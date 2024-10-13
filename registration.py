import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if not name or not email or not age:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return
    
    # Here you can add logic to save the data or further processing
    messagebox.showinfo("Success", "Registration Successful!")

    # Clear the form
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entries for the form
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()


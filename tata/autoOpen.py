import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open URLs from the selected file
def open_urls(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        
        for url in urls:
            webbrowser.open(url.strip())
        messagebox.showinfo("Success", "All URLs opened successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse and select the file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Function to handle button click
def on_open_button_click():
    file_path = file_entry.get()
    if file_path:
        open_urls(file_path)
    else:
        messagebox.showwarning("No file", "Please select a file first.")

# Create the main window
root = tk.Tk()
root.title("Open URLs from File")

# Create the file entry field and browse button
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=0, padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Create the open button
open_button = tk.Button(root, text="Open URLs", command=on_open_button_click)
open_button.grid(row=1, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()


²
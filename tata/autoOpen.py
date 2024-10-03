import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar,PhotoImage
from courses import courses

# Function to handle button click
def on_open_button_click(subject):
    if subject:
        open_urls(subject)
    else:
        messagebox.showwarning("No selection", "Please select a subject first.")

courses_instance = courses()

def open_urls(subject):
    try:
        print(subject)
        urls = getattr(courses_instance, subject, [])  # Use getattr to access the subject dynamically
        for url in urls:
            webbrowser.open(url.strip())
        messagebox.showinfo("Success", "All URLs opened successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Open URLs from File")
root.geometry("300x250")  # Width x Height
root.configure(bg='#242135')  # Light gray background

# Logo
try:
   logo_icon = PhotoImage(file='images.png')  # Use your uploaded image path
   root.iconphoto(False, logo_icon)  
except Exception as e:
    print(f"Error loading logo: {e}")

# Variable to store the selected value
selected_value = StringVar()
selected_value.set("DataAnalysis")  # Set default value

# Create a dropdown menu
options = ["DataAnalysis", "GameTheory", "Econometrics", "DataBaseManagemetnt", "SystemAdministration", "POM"]
dropdown = tk.OptionMenu(root, selected_value, *options)
dropdown.config(font=('Helvetica', 14), bg='#e6e6e6',fg="#383253", width=20,borderwidth=0,highlightthickness=0,relief='flat')
dropdown.pack(pady=20)

# Create the open button

def on_enter(button):
    button.config(bg='#383253', fg='white',borderwidth=5, highlightthickness=0)  # Change to black background and white text

def on_leave(button):
    button.config(bg='white', fg='#383253', borderwidth=5, highlightthickness=0)  # Change back to white background and black text

hover_button = tk.Button(root, text="Open Urls", command=lambda: on_open_button_click(selected_value.get()), font=('Arial', 12, 'bold'), bg='white', fg='#0c0c14',borderwidth=2, highlightthickness=0,relief='flat' )
hover_button.pack(pady=50, padx=50)

# Bind hover events
hover_button.bind("<Enter>", lambda e: on_enter(hover_button))
hover_button.bind("<Leave>", lambda e: on_leave(hover_button))



# open_button = tk.Button(master=root, text="Open URLs", command=lambda: on_open_button_click(selected_value.get()), font=('Helvetica', 14), bg='#4CAF50', fg='white', padx=20, pady=10)
# open_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()

import tkinter as tk
from tkinter import PhotoImage
from threading import Thread
import time
import subprocess
import sys
import os
from PIL import Image, ImageTk

#==========gpt told me to so this ======================
script_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
logo_path = os.path.join(script_dir, 'logo.png')

#==========================
from tkinter import ttk
#---------------------ui-------------------------------------
def run_background_task():
    while True:
        subprocess.run(["python", "check.py"])  
        time.sleep(3600)


# Create the main application window

root = tk.Tk()
root.title("News Update App")

# Email entry field
email_label = tk.Label(root, text="Enter your email:",bg="#343433",fg="#1b94cf")
email_label.pack(pady=10)
email_entry = tk.Entry(root, width=30,bg="#222222",fg="white")
email_entry.pack(padx=10, pady=10)
#email sending function


def send_email_wrapper(eemail):
    save_email(eemail)


def save_email(es):
    global emails
    emails = es
    print(f"Email saved: {emails}")



def handle_send_email():
        email = email_entry.get()
        send_email_wrapper(email)
        print("Submit clicked.")
        with open("email.txt", "w") as file:
            file.write(email)


        
# Send email button
send_button = tk.Button(root, text="Save Email", command=handle_send_email ,padx=10, pady=10, borderwidth=1, relief=tk.FLAT,bg="#1b94cf",fg="white")
send_button.pack(padx=10, pady=30)

# Start background task in a separate thread
background_thread = Thread(target=run_background_task)
background_thread.start()
#style
#iconn >>>>>>>>
#icon_image = PhotoImage(file=logo_path)
img = Image.open(logo_path)
icon_image = ImageTk.PhotoImage(img)
root.iconphoto(False, icon_image)

root.configure(background='#343433')
# Run the main loop for the GUI
root.mainloop()


#=========================================================================================================


# Example usage








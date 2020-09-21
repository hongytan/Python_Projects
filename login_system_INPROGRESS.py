# Login system

import tkinter as tk

WIDTH = 300
HEIGHT = 300

# Functions
def append_storage(email, password):
    storage_email_label['text'] = email
    storage_pass_label['text'] = password

def system_password(user_input):
    """ Checks if inputted password is correct and logins """
    if user_input == '':
        root.destroy()

        top = tk.Tk()
        top.title("Email Storage")

        # Sets up size of GUI
        canvas = tk.Canvas(top,height=HEIGHT, width=WIDTH)
        canvas.pack()

        # GUI for email entries
        email_frame = tk.Frame(top)
        email_frame.place(relwidth=1, relheight=1)

        # Email GUI
        email_label = tk.Label(email_frame, text='Email', font=('Courier', 15))
        email_label.place(rely=0.10, relwidth=0.3, relheight=0.10)

        email_entry = tk.Entry(email_frame, font=('Courier', 15))
        email_entry.place(relx=0.3, rely = 0.1, relwidth=0.6, relheight = 0.1)

        # Password GUI
        pass_label = tk.Label(email_frame, text='Password', font=('Courier', 12))
        pass_label.place(rely=0.20, relwidth=0.3, relheight=0.10)

        pass_entry = tk.Entry(email_frame, font=('Courier', 15))
        pass_entry.place(relx=0.3, rely = 0.2, relwidth=0.6, relheight = 0.1)

        # Button GUI
        storage_button = tk.Button(email_frame, text = 'Register', font=('Courier', 13),
                                   command=lambda: append_storage(email_entry.get(),
                                                                  pass_entry.get()))
        storage_button.place(relx = 0.3, rely = 0.4, relwidth = 0.4, relheight = 0.1)

        # Frame for email storage
        storage_frame = tk.Frame(top, bg='green')
        storage_frame.place(rely=0.5, relwidth=1, relheight=0.5)

        # Label for storage email
        storage_email_label = tk.Label(storage_frame, bg='white', text = 'Email', anchor='nw',
                                       font=('Courier', 12))
        storage_email_label.place(relwidth=0.5, relheight=1)

        # Label for storage password
        storage_pass_label = tk.Label(storage_frame, bg='white', text = 'Password', anchor='ne',
                                      font=('Courier', 12))
        storage_pass_label.place(relx = 0.5, relwidth=0.5, relheight=1)

        


root = tk.Tk()
root.title("Email Storage")

# Sets up size of GUI
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

# GUI for system login
sys_frame = tk.Frame(root)
sys_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.7)

sys_label = tk.Label(sys_frame, text='System Password', font=('Courier', 15))
sys_label.place(rely=0.15, relwidth=1, relheight=0.2)

sys_entry = tk.Entry(sys_frame, font=('Courier', 20))
sys_entry.place(rely = 0.4, relwidth=1, relheight = 0.2)

sys_button = tk.Button(sys_frame, text = 'Enter', font=('Courier', 12), command=lambda:
                           system_password(sys_entry.get()))
sys_button.place(relx = 0.3, rely = 0.7, relwidth = 0.4, relheight = 0.1)






















root.mainloop()



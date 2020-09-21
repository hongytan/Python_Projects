# Login system

import tkinter as tk

WIDTH = 300
HEIGHT = 300

# Functions
def system_password(user_input):
    """ Checks if inputted password is correct and logins """
    if user_input == 'Password':
        root.destroy()

        top = tk.Tk()
        top.title("Email Storage")

        # Sets up size of GUI
        canvas = tk.Canvas(top,height=HEIGHT, width=WIDTH)
        canvas.pack()

        # GUI for email entries
        email_frame = tk.Frame(top)
        email_frame.place(relwidth=1, relheight=1)

        email_label = tk.Label(email_frame, text='Email', font=('Courier', 17))
        email_label.place(rely=0.10, relwidth=0.3, relheight=0.10)

        email_entry = tk.Entry(email_frame)
        email_entry.place(relx=0.3, rely = 0.1, relwidth=0.6, relheight = 0.1)

        pass_label = tk.Label(email_frame, text='Password', font=('Courier', 17))
        pass_label.place(rely=0.20, relwidth=0.3, relheight=0.10)

        pass_entry = tk.Entry(email_frame)
        pass_entry.place(relx=0.3, rely = 0.2, relwidth=0.6, relheight = 0.1)

        email_button = tk.Button(email_frame, text = 'Register', font=('Courier', 12))
        email_button.place(relx = 0.3, rely = 0.4, relwidth = 0.4, relheight = 0.1)

root = tk.Toplevel()
root.title("Email Storage")

# Sets up size of GUI
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

# GUI for system login
sys_frame = tk.Frame(root)
sys_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.7)

sys_label = tk.Label(sys_frame, text='System Password', font=('Courier', 20))
sys_label.place(rely=0.15, relwidth=1, relheight=0.2)

sys_entry = tk.Entry(sys_frame)
sys_entry.place(rely = 0.4, relwidth=1, relheight = 0.2)

sys_button = tk.Button(sys_frame, text = 'Enter', font=('Courier', 12), command=lambda:
                           system_password(sys_entry.get()))
sys_button.place(relx = 0.3, rely = 0.7, relwidth = 0.4, relheight = 0.1)























root.mainloop()



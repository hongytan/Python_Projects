# Weather App GUI Video

import tkinter as tk

HEIGHT = 500
WIDTH = 600

def test(entry):
    print("Hello, {}".format(entry))


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

button = tk.Button(frame, text="Get Weather", command=Lambda: test(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

frame_bottom = tk.Frame(root, bg='#80c1ff', bd=10)
frame_bottom.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

label = tk.Label(frame_bottom, text="This is a label")
label.place(relwidth=1, relheight=1)




root.mainloop()

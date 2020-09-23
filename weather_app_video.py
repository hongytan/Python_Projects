# Weather App GUI Video

import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600


def label_text(weather):
    try:
        city = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature: %sF' %(city, desc, temp)
    except:
        final_str = "Error: Please try again."
    return final_str

def get_weather(city):
    
    weather_key = 'b30a10656b90bcb241341f6099843e01'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = label_text(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

entry = tk.Entry(frame, font = ('Courier', 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier',15), command=lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

frame_bottom = tk.Frame(root, bg='#80c1ff', bd=10)
frame_bottom.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

label = tk.Label(frame_bottom,font = ('Courier', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()

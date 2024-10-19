import tkinter as tk
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz


def get_weather():
    pass


window = tk.Tk()
window.title("Weather App")
window.geometry("900x500")
window.resizable(False, False)

# Search image
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(window, image=search_image)
search_image_label.pack(pady=20, side=tk.TOP)

# Text field for search (جایی که جستجو می‌کنید)
textfield = tk.Entry(window, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white", border=0, highlightthickness=0)
textfield.place(x=280, y=40)

# Search button (دکمه جستجو)
search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(window, image=search_icon, border=0, cursor="hand2", bg="#404040", command=get_weather, bd=0, highlightthickness=0)
search_icon_button.place(x=590, y=34)

# Logo image
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(side=tk.TOP)

# Frame image
frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(window, image=frame_image)
frame_label.pack(pady=10, side=tk.BOTTOM)

# City label
city_label = tk.Label(window, font=("arial", 40, "bold"), fg="#e355cd")
city_label.place(x=120, y=160)

# Time label
time_label = tk.Label(window, font=("arial", 20, "bold"), fg="#4b4bcc")
time_label.place(x=120, y=230)

# Clock label
clock_label = tk.Label(window, font=("Helvetica", 20), fg="#e355cd")
clock_label.place(x=120, y=270)

window.mainloop()

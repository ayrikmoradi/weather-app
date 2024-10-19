import tkinter as tk
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz

# Function to get weather based on city name
def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)

        # Fetch latitude and longitude
        lat = location.latitude
        lng = location.longitude

        # Get timezone using TimezoneFinder
        obj = TimezoneFinder()
        timezone = obj.timezone_at(lng=lng, lat=lat)
        city_label.config(text=timezone.split("/")[1])

        # Fetch current local time
        home = pytz.timezone(timezone)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        time_label.config(text="LOCAL TIME")

        # Fetch weather information
        api_key = "e1ce0948fe43a6f98c4c4378f83cd1a4"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        # Update labels with fetched data
        temp_label.config(text=f"{temp} °C")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp} °C")
        wind_label.config(text=f"{wind} m/s")
        humidity_label.config(text=f"{humidity}%")
        description_label.config(text=description)
        pressure_label.config(text=f"{pressure} hPa")

    except Exception as error:
        print(error)
        messagebox.showerror("Weather App", "Invalid Entry!")


# Initialize main window
window = tk.Tk()
window.title("Weather App")
window.geometry("900x500")
window.resizable(False, False)

# Change background color
window.config(bg="#add8e6")

# Search image (this is the background image for the search area)
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(window, image=search_image, bg="#add8e6")
search_image_label.pack(pady=20, side=tk.TOP)

# Text field for search 
textfield = tk.Entry(window, justify="center", width=17, font=("poppins", 25, "bold"), 
                     bg="#404040", fg="white", border=0, highlightthickness=0)
textfield.place(x=280, y=40)

# Search button (with matching color and no border)
search_icon = tk.PhotoImage(file="search_icon.png")  # Ensure search_icon.png has a transparent background
search_icon_button = tk.Button(window, image=search_icon, border=0, cursor="hand2", 
                               bg="#404040", command=get_weather, bd=0, highlightthickness=0)
search_icon_button.place(x=590, y=34)

# Logo image
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(window, image=logo_image, bg="#add8e6")
logo_label.pack(side=tk.TOP)

# Frame image
frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(window, image=frame_image, bg="#add8e6")
frame_label.pack(pady=10, side=tk.BOTTOM)

# City label
city_label = tk.Label(window, font=("arial", 40, "bold"), fg="#e355cd", bg="#add8e6")
city_label.place(x=120, y=160)

# Time label
time_label = tk.Label(window, font=("arial", 20, "bold"), fg="#4b4bcc", bg="#add8e6")
time_label.place(x=120, y=230)

# Clock label
clock = tk.Label(window, font=("Helvetica", 20), fg="#e355cd", bg="#add8e6")
clock.place(x=120, y=270)

# Weather details labels
label1 = tk.Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=280, y=400)

label3 = tk.Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)

label4 = tk.Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=670, y=400)

# Weather data output labels
temp_label = tk.Label(window, font=("arial", 70, "bold"), fg="#e355cd", bg="#add8e6")
temp_label.place(x=590, y=170)

condition_label = tk.Label(window, font=("arial", 15, "bold"), fg="#4b4bcc", bg="#add8e6")
condition_label.place(x=590, y=270)

wind_label = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#5ebaff", fg="#404040")
wind_label.place(x=120, y=430)

humidity_label = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#5ebaff", fg="#404040")
humidity_label.place(x=280, y=430)

description_label = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#5ebaff", fg="#404040")
description_label.place(x=450, y=430)

pressure_label = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#5ebaff", fg="#404040")
pressure_label.place(x=670, y=430)

# Run the main loop
window.mainloop()

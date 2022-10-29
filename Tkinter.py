from tkinter import *
from tkinter.ttk import Notebook
import requests
import json
from datetime import datetime
from PIL import ImageTk, Image

from TkinterLoadGif import TkinterLoadGif

count = 0
root = Tk()
root.title("Tab Widget")
tabControl = Notebook(root)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
lbl = TkinterLoadGif(tab1)


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def showWeather(tfield,tab2, lat, long):
    global count
    print(count)
    count = count + 1
    # Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "f2b2440583e08bc0b8a8db46eb949c73"  # sample API

    # Get city name from user from the input field (later in the code)

    # API url
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + long + '&appid=f2b2440583e08bc0b8a8db46eb949c73'
    print(weather_url)
    # Get the response from fetched url
    response = requests.get(weather_url)

    # changing response from json to python readable
    weather_info = response.json()

    tfield.delete("1.0", "end")  # to clear the text field for every new output

    # as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    climate_map = {}
    if weather_info['cod'] == 200:
        kelvin = 273  # value of kelvin

        # -----------Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        climate_map["temp"] = temp
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        climate_map["feels_like_temp"] = feels_like_temp
        pressure = weather_info['main']['pressure']
        climate_map["pressure"] = pressure
        humidity = weather_info['main']['humidity']
        climate_map["humidity"] = humidity
        wind_speed = weather_info['wind']['speed'] * 3.6
        climate_map["wind_speed"] = wind_speed
        sunrise = weather_info['sys']['sunrise']
        climate_map["sunrise"] = sunrise
        sunset = weather_info['sys']['sunset']
        climate_map["sunset"] = sunset
        timezone = weather_info['timezone']
        climate_map["timezone"] = timezone
        cloudy = weather_info['clouds']['all']
        climate_map["cloudy"] = cloudy
        description = weather_info['weather'][0]['description']
        climate_map["description"] = description
        sunrise_time = time_format_for_location(sunrise + timezone)
        climate_map["sunrise_time"] = sunrise_time
        sunset_time = time_format_for_location(sunset + timezone)
        climate_map["sunset_time"] = sunset_time
        # assigning Values to our weather varaible, to display as output
        city_name = weather_info['name']
        climate_map["city_name"] = city_name
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}\nWindSpeed: {wind_speed}\nCount: {count}"
    else:
        weather = f"\n\tWeather for API error"

    tfield.insert(INSERT, weather)  # to insert or send value in our Text Field to display output
    return climate_map

# ------------------------------Frontend part of code - Interface

def update_tab(arg):
    lbl.unload()
    lbl.load('Output/alpha.gif')
    print(arg)


def mainPanel(lat, long):
    tabControl.add(tab1, text='Irrigation Pattern')
    tabControl.add(tab2, text='Weather')
    tabControl.add(tab3, text='Control & Calibration')
    tabControl.pack(expand=1, fill="both")

    root.geometry("480x460")  # size of the window by default
    root.resizable(0, 0)  # to make the window size fixed
    # title of our window
    root.title("Patch Detection GUI ")

    # ----------------------Tab 1--------------------------------------------
    lbl = TkinterLoadGif(tab1)
    lbl.pack()
    lbl.load('Output/alpha.gif')
    variable = IntVar(tab1)
    variable.set(1)  # default value
    Label(tab1, text="Alpha").pack(pady=10)
    w = OptionMenu(tab1, variable, 0, 0.5, 1, command=update_tab)
    w.pack()
    w.place(x=260, y=205)
    Label(tab1, text="Sprinkler GPS").pack(pady=10)
    gpsfield = Text(tab1, width=38, height=1)
    gpsfield.pack()
    gpsfield.insert(INSERT, lat + ', ' + long)
    Label(tab1, text="Target Area").pack(pady=10)
    area = Text(tab1, width=14, height=1)
    area.pack()
    area.insert(INSERT, "7.68")
    Label(tab1, text="Deviation Area").pack(pady=10)


    # ----------------------Tab 2--------------------------------------------

    Label(tab2, text="The Weather is:", font='arial 12 bold').grid(row=1, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    tfield = Text(tab2, width=46, height=10)
    tfield.grid(row=2, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    climateMap = showWeather(tfield,tab2, lat, long)
    Button(tab2, command=lambda: showWeather(tfield,tab2, lat, long), text="Update Weather", font="Arial 10",
           bg='lightgreen', fg='black',
           activebackground="teal", padx=5, pady=5).grid(row=3, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    # display = (fImageTk.PhotoImage(Image.open("tkinter_img/sunn.png"))
    # Label(tab2, image=display).pack()
    img = PhotoImage(file="tkinter_img/sunn.png")
    lab = Label(tab2, text=climateMap["temp"])
    lab.grid(row=4, column=2, sticky='E', padx=5, pady=5, ipadx=5, ipady=5)
    lab["compound"] = LEFT
    lab["image"] = img



    # ----------------------Tab 3--------------------------------------------
    Label(tab3, text="Sprinkler Name").pack(pady=10)
    Label(tab3, text="\u03C6").pack(pady=10)
    Text(tab3, width=46, height=2).pack()
    Label(tab3, text="\u03B8").pack(pady=10)
    Text(tab3, width=14, height=2).pack()
    Button(tab3, command=showWeather, text="On", font="Arial 10",
           bg='lightgreen', fg='black',
           activebackground="teal", padx=5, pady=5).pack(pady=20)
    Text(tab3, width=14, height=2).pack()
    Button(tab3, command=showWeather, text="Off", font="Arial 10",
           bg='#ff4d4d', fg='black',
           activebackground="teal", padx=5, pady=5).pack(pady=20)
    root.mainloop()


#mainPanel('36.849085847891374', '-76.25461881517771')
mainPanel('8.487453605780034','76.95281763282492'),
#mainPanel('28.613066383513306', '77.23226788960606')
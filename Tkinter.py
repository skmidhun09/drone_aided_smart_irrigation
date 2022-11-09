from tkinter import *
import tkinter as tk
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
main = tk.Frame(tabControl)
main.configure(background='white', borderwidth=5)
tab1 = tk.Frame(tabControl)
tab1.configure(background='white')
tab2 = tk.Frame(tabControl)
tab2.configure(background='white')
tab3 = tk.Frame(tabControl)
lbl = TkinterLoadGif(tab1)
header_font = 'arial 12 bold'
internal_font = 'arial 10 bold'


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def showWeather(lat, long):
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
        country = weather_info['sys']['country']
        climate_map["country"] = country
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

    return climate_map


# ------------------------------Frontend part of code - Interface

def update_tab(arg):
    lbl.unload()
    lbl.load('Output/alpha.gif')
    print(arg)


def mainPanel(lat, long):
    tabControl.add(main, text='Main Menu')
    tabControl.add(tab1, text='Irrigation Pattern')
    tabControl.add(tab2, text='Weather')
    tabControl.add(tab3, text='Control & Calibration')
    tabControl.pack(expand=1, fill="both")

    root.geometry("640x540")  # size of the window by default
    root.resizable(0, 0)  # to make the window size fixed
    # title of our window
    root.title("Patch Detection GUI ")

    # ---------------------- Climate Icon initialize--------------------------------------------
    icon_res = (80, 80)
    climateMap = showWeather(lat, long)
    country = climateMap["country"]
    city = climateMap["city_name"]
    temp = climateMap["temp"]
    if temp < 20:
        temp_img = Image.open("tkinter_img/tcold.png")
    else:
        temp_img = Image.open("tkinter_img/thot.png")
    temp_img_main = temp_img.resize(icon_res)
    temp_img_main = ImageTk.PhotoImage(temp_img_main)
    temp_img = ImageTk.PhotoImage(temp_img)

    cloudy = climateMap["cloudy"]
    if (cloudy > 85):
        cloudy_img = Image.open("tkinter_img/rain.png")
        sky_status = "Rainy"
    elif (cloudy > 50):
        cloudy_img = Image.open("tkinter_img/clod.png")
        sky_status = "Partially Cloudy"
    else:
        cloudy_img = Image.open("tkinter_img/sunn.png")
        sky_status = "Sunny"
    cloudy_img_main = cloudy_img.resize(icon_res)
    cloudy_img_main = ImageTk.PhotoImage(cloudy_img_main)
    cloudy_img = ImageTk.PhotoImage(cloudy_img)

    drone_img = Image.open("tkinter_img/drone.png")
    drone_img_main = drone_img.resize(icon_res)
    drone_img_main = ImageTk.PhotoImage(drone_img_main)
    drone_img = ImageTk.PhotoImage(drone_img)

    splr_img = Image.open("tkinter_img/sprk.png")
    splr_img_main = splr_img.resize(icon_res)
    splr_img_main = ImageTk.PhotoImage(splr_img_main)
    splr_img = ImageTk.PhotoImage(splr_img)

    humidity = climateMap["humidity"]
    humidity_img = Image.open("tkinter_img/humi.png")
    humidity_img_main = humidity_img.resize(icon_res)
    humidity_img_main = ImageTk.PhotoImage(humidity_img_main)
    humidity_img = ImageTk.PhotoImage(humidity_img)

    wind_speed = climateMap["wind_speed"]
    wind_speed_img = Image.open("tkinter_img/wind.png")
    wind_speed_img_main = wind_speed_img.resize(icon_res)
    wind_speed_img_main = ImageTk.PhotoImage(wind_speed_img_main)
    wind_speed_img = ImageTk.PhotoImage(wind_speed_img)

    pressure = climateMap["pressure"]
    pressure_img = Image.open("tkinter_img/pres.png")
    pressure_img_main = pressure_img.resize(icon_res)
    pressure_img_main = ImageTk.PhotoImage(pressure_img_main)
    pressure_img = ImageTk.PhotoImage(pressure_img)

    # ----------------------Main Menu--------------------------------------------
    left_frame = tk.Frame(main)
    left_frame.grid(row=0, column=0, sticky="nswe")
    left_top = tk.Frame(left_frame,highlightbackground="white", highlightthickness=4)
    left_top.grid(row=1, column=0, sticky="nswe")
    left_bottom = tk.Frame(left_frame,highlightbackground="white", highlightthickness=4)
    left_bottom.grid(row=2, column=0, sticky="nswe")
    right_frame = tk.Frame(main)
    right_frame.configure(background="white")
    right_frame.grid(row=0, column=1, sticky="nswe")

    # ----------------------Main menu left top--------------------------------------------
    Label(left_top, text="Irrigation Pattern", font=header_font,).grid(row=0, columnspan=2, pady=10, padx=130,
                                                                        sticky='NSWE')
    gif_img = TkinterLoadGif(left_top)
    gif_img.grid(row=1, rowspan=2, column=0, sticky='NSWE')
    gif_img.load("Output/alpha.gif")
    text1 = StringVar()
    text1.set("0.5")
    Label(left_top, text="Alpha:").grid(row=2, column=1, pady=35, padx=10, sticky='WS')
    option = OptionMenu(left_top, text1, 0, 0.5, 1, command=update_tab)
    option.config(width=7)
    option.grid(row=2, column=1, sticky='S')

    Label(left_top, text="Latitude").grid(row=3, ipadx=20, pady=15, column=0, sticky='W')
    latitude = Text(left_top, width=10, height=1, bg="#efeff5")
    latitude.grid(row=3, column=0)
    latitude.insert(INSERT, round(float(lat), 8))
    Label(left_top, text="Longitude").grid(row=3, ipadx=10, column=0, sticky='E')
    longitude = Text(left_top, width=10, height=1, bg="#efeff5")
    longitude.grid(row=3, column=1, padx=10, sticky='W')
    longitude.insert(INSERT, round(float(long), 8))

    Label(left_top, text="Patch Area").grid(row=4, ipadx=20, column=0, sticky='W')
    area = Text(left_top, width=10, height=1, bg="#efeff5")
    area.grid(row=4, column=0)
    area.insert(INSERT, "7.68")
    Label(left_top, text="Irrigation Area").grid(row=4, ipadx=10, column=0, sticky='E')
    iarea = Text(left_top, width=10, height=1, bg="#efeff5")
    iarea.grid(row=4, column=1)
    iarea.insert(INSERT, "8.68")
    Label(left_top, text="").grid(row=5, ipady=2, columnspan=2, sticky='E')

    # ----------------------Main menu right--------------------------------------------
    Label(right_frame, text="Weather Report", font=header_font, bg="white").grid(row=0, columnspan=2, pady=5,
                                                                                   sticky='NSWE')
    Label(right_frame, text=city+",", font='arial 11 bold',foreground="red", pady=5, bg="white").grid(row=1, column=0,
                                                                                               sticky='E')
    Label(right_frame, text=country, font='arial 11 bold', pady=5, bg="white").grid(row=1, column=1,
                                                                                                 sticky='W')

    # Temprature
    Label(right_frame, text="Temprature: " + str(climateMap["temp"]) + "° C", font=internal_font, bg="white",
          compound=BOTTOM, image=temp_img_main).grid(row=2, column=0,padx=5, sticky='NSWE')

    # Clouding
    Label(right_frame, text=sky_status, font=internal_font, bg="white", compound=BOTTOM, image=cloudy_img_main).grid(
        row=2, column=1, sticky='NSWE')

    # wind_speed
    Label(right_frame, text="Wind: " + str(round(wind_speed, 2)) + " Km/h", font=internal_font, bg="white",
          compound=BOTTOM, image=wind_speed_img_main).grid(row=3, column=0, sticky='NSWE')

    # Humidity
    Label(right_frame, text="Humidity: " + str(humidity) + "%", font=internal_font, bg="white", compound=BOTTOM,
          image=humidity_img_main).grid(row=3, column=1, sticky='NSWE')

    # Sprinkler
    Label(right_frame, text="Sprinkler Acc: 85%", font=internal_font, bg="white", compound=BOTTOM,
          image=splr_img_main).grid(row=4, column=0, sticky='NSWE')

    # Drone
    Label(right_frame, text="Flight Eff: 80%", font=internal_font, bg="white", compound=BOTTOM,
          image=drone_img_main).grid(row=4, column=1, sticky='NSWE')

    # pressure
    Label(right_frame, text="Pressure: " + str(pressure) + " hPa", font=internal_font, bg="white", compound=BOTTOM,
          image=pressure_img_main).grid(row=5, column=0, sticky='NSWE')

    # ----------------------Main menu left bottom--------------------------------------------
    Label(left_bottom, text="Manual Override", font=header_font).grid(row=0, columnspan=2, pady=10, padx=130,
                                                                        sticky='NSWE')
    Label(left_bottom, text="Sprinkler \nNo.").grid(row=1, column=0, padx=5, pady=5, sticky='W')
    Text(left_bottom, width=10, height=2).grid(row=1, column=0, padx=(70,5), pady=5, sticky='W')
    Label(left_bottom, text="\u03C6").grid(row=1, column=1, padx=5, pady=5, sticky='W')
    Text(left_bottom, width=6, height=2).grid(row=1, column=1, padx=(25,0), pady=5, sticky='W')
    Label(left_bottom, text="\u03B8").grid(row=1, column=1, padx=(0,60), pady=5, sticky='E')
    Text(left_bottom, width=6, height=2).grid(row=1, column=1, padx=5, pady=5, sticky='E')
    Button(left_bottom, command=showWeather, text="Run", font="Arial 10",
           bg='lightgreen', fg='black',
           activebackground="teal", width=6, padx=6, pady=5).grid(row=2, column=0, padx=(85,0), pady=5, sticky='W')
    Button(left_bottom, command=showWeather, text="Stop", font="Arial 10",
           bg='#ff4d4d', fg='black',
           activebackground="teal", width=6, padx=6, pady=5).grid(row=2, column=1, padx=25, pady=5, sticky='W')

    # ----------------------Tab 1--------------------------------------------
    gif_image = TkinterLoadGif(tab1)
    gif_image.pack()
    gif_image.load('Output/alpha.gif')
    variable = IntVar(tab1)
    variable.set(1)  # default value
    Label(tab1, text="Alpha", bg='white').pack(pady=10)
    w = OptionMenu(tab1, variable, 0, 0.5, 1, command=update_tab)
    w.pack()
    w.place(x=260, y=205)
    Label(tab1, text="Sprinkler GPS", bg='white').pack(pady=10)
    gpsfield = Text(tab1, width=38, height=1, bg="#efeff5")
    gpsfield.pack()
    gpsfield.insert(INSERT, lat + ', ' + long)
    Label(tab1, text="Target Area", bg='white').pack(pady=10)
    area = Text(tab1, width=14, height=1, bg="#efeff5")
    area.pack()
    area.insert(INSERT, "7.68")
    Label(tab1, text="Deviation Area", bg='white').pack(pady=10)

    # ----------------------Tab 2--------------------------------------------
    # Country & Place

    Label(tab2, text="Country Code: " + country, font='arial 12 bold', pady=10, bg="white").grid(row=3, column=1,
                                                                                                 sticky='NSWE')
    Label(tab2, text="City: " + city, font='arial 12 bold', padx=35, pady=10, bg="white").grid(row=3, column=2,
                                                                                               sticky='NSWE')
    # Temprature
    Label(tab2, text="Temprature: " + str(climateMap["temp"]) + "° C", font=internal_font, bg="white", compound=BOTTOM,
          image=temp_img).grid(row=4, column=1, sticky='NSWE')

    # Clouding
    Label(tab2, text=sky_status, font=internal_font, bg="white", compound=BOTTOM,
          image=cloudy_img).grid(row=5, column=1, sticky='NSWE')

    # Drone
    Label(tab2, text="Flight Efficiency: 80%", font=internal_font, bg="white", compound=BOTTOM,
          image=drone_img).grid(row=4, column=3, sticky='NSWE')

    # Sprinkler
    Label(tab2, text="Sprinkler Accuracy: 85%", font=internal_font, bg="white", compound=BOTTOM,
          image=splr_img).grid(row=5, column=3, sticky='NSWE')

    # Humidity
    Label(tab2, text="Humidity: " + str(humidity) + "%", font=internal_font, bg="white", compound=BOTTOM,
          image=humidity_img).grid(row=4, column=2, sticky='NSWE')

    # wind_speed
    Label(tab2, text="Wind: " + str(round(wind_speed, 2)) + " Km/h", font=internal_font, bg="white", compound=BOTTOM,
          image=wind_speed_img).grid(row=5, column=2, sticky='NSWE')

    # pressure
    Label(tab2, text="Pressure: " + str(pressure) + " hPa", font=internal_font, bg="white", compound=BOTTOM,
          image=pressure_img).grid(row=6, column=1, sticky='NSWE')

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


mainPanel('36.849085847891374', '-76.25461881517771')
# mainPanel('8.487453605780034','76.95281763282492'),
# mainPanel('28.613066383513306', '77.23226788960606')

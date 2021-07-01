from tkinter import *
import requests
import json

root = Tk()
root.title("Weather Report")
root.iconbitmap(r'C:\Users\Unknown\python\image.ico')
root.geometry("400x200")


def submit():
    try:
        r = requests.get(
            r"https://api.waqi.info/feed/" + zip_int.get() + "/?token=67854891b90a375064f03fba7**********")

        api = json.loads(r.content)

        city = api['data']['city']['name']
        aqi = api['data']['aqi']
        time = api['data']['time']['s']

        if 0 <= aqi < 51:
            weather_color = "#00e400"
            tag = "Healthy"
        elif 50 < aqi < 101:
            weather_color = "#FFFF00"
            tag = "Moderate"
        elif 100 < aqi < 151:
            weather_color = "#ff7e00"
            tag = "Unhealthy for Sensitive Group"
        elif 150 < aqi < 201:
            weather_color = "#FF0000"
            tag = "Unhealthy"
        elif 200 < aqi < 301:
            weather_color = "#8F3F97"
            tag = "Very Unhealthy"
        elif aqi > 300:
            weather_color = "#7e0023"
            tag = "Hazardous"

        root.configure(background=weather_color)

        myLabel = Label(root, text=city + "\n" + "Air Quality: " + str(aqi) + "\n" + str(tag) + "\n" + str(time),
                        font=("Helvetica", 10),
                        background=weather_color)
        myLabel.grid(row=2, column=0)


    except Exception as e:
        api = "Error..."


country_btn = Button(root, text='Submit', command=lambda: submit())
country_btn.grid(stick=W, row=1, column=0)

zip_int = Entry(root)
zip_int.grid(stick=W, row=0, column=0)

root.mainloop()

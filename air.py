import requests
from bs4 import BeautifulSoup
from tkinter import *


def getdata(url):
    r=requests.get(url)
    return r.text


htmldata = getdata("https://weather.com/en-IN/forecast/air-quality/l/889aed36062cac2fdd772318e14c2fab6d48f5cc8609b1d7fa620faf8da1bb86")
soup = BeautifulSoup(htmldata, 'html.parser')


def airinfo():
    res = soup.find(class_="DonutChart--innerValue--3_iFF AirQuality--extendedDialText--1kqIb").text
    air_data = soup.find_all(class_="DonutChart--innerValue--3_iFF AirQuality--pollutantDialText--2Q5Oh")
    city=soup.find(class_="styles--locationName--1R6PN").text
    print(city)
    air_data=[data.text for data in air_data]
    print("Air Quality :", res)
    print("O3 level :", air_data[0])
    print("CO level :", air_data[1])
    print("NO2 level :", air_data[2])
    print("PM10 level :", air_data[3])
    print("PM2.5 level :", air_data[4])
    print("SO2 level :", air_data[5])
    if res <= '50':
        remark = "Good"
        impact = "Minimal impact"
    elif res <= '100' and res > '51':
        remark = "Satisfactory"
        impact = "Minor breathing discomfort to sensitive people"
    elif res <= '200' and res >= '101':
        remark = "Moderate"
        impact = "Breathing discomfort to the people with lungs, asthma and heart diseases"
    elif res <= '400' and res >= '201':
        remark = "Very Poor"
        impact = "Breathing discomfort to most people on prolonged exposure"
    elif res <= '500' and res >= '401':
        remark = "Severe"
        impact = "Affects healthy people and seriously impacts those with existing diseases"
    print(remark)
    print(impact)
    


master = Tk()
master.geometry('300x350')
 

air_data = StringVar()
ar = StringVar()
o3 = StringVar()
no2 = StringVar()
so2 = StringVar()
pm = StringVar()
pml = StringVar()
co = StringVar()
res_remark = StringVar()
res_imp = StringVar()


Label(master, text="Air Quality : ",).place(x=20,y=20)
Label(master, text="O3 (μg/m3) :").place(x=20,y=60)
Label(master, text="CO (μg/m3) :").place(x=20,y=80)
Label(master, text="NO2 (μg/m3) :").place(x=20,y=100)
Label(master, text="PM10 (μg/m3) :").place(x=20,y=120)
Label(master, text="PM2.5 (μg/m3) :").place(x=20,y=140)
Label(master, text="SO2 (μg/m3) :").place(x=20,y=160)
Label(master, text="Remark :").place(x=20,y=200)
Label(master, text="Possible Health Impacts :").place(x=20,y=240)


Label(master, text="", textvariable=ar).place(x=160,y=20)
Label(master, text="", textvariable=o3).place(x=160, y=60)
Label(master, text="", textvariable=co).place(x=160,y=80)
Label(master, text="", textvariable=no2).place(x=160,y=100)
Label(master, text="", textvariable=pml).place(x=160,y=120)
Label(master, text="", textvariable=pm).place(x=160,y=140)
Label(master, text="", textvariable=so2).place(x=160,y=160)
Label(master, text="", textvariable=res_remark).place(x=160,y=200)
Label(master, text="", textvariable=res_imp).place(x=160,y=240)


b = Button(master, text="Check", command=airinfo, bg="Blue").place(x=160,y=300)

mainloop()
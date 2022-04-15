from tkinter import *
import requests
import json
from TestAPI import city

San_Diego = city[0]
#Main program:
interface =  Tk()
interface.title("Air Quality App")


#define screen here
output = Entry(interface, width = 80, borderwidth=5, bg = "#E4EDEA")
label1 = Label(interface, text = "Enter a zipcode", width = 20)
zipcode = Entry(interface, width =25)
interface.geometry("510x150")
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=92126&distance=25&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B



def button_click(number):
    if number == 1:
        output.delete(0, END)
        output.insert(0, city[0])
    elif number == 2:
        output.delete(0, END)
        output.insert(0, city[1])
    elif number == 3:
        output.delete(0, END)
        output.insert(0, city[2])
    elif number == 4:
        output.delete(0, END)
        output.insert(0, city[3])
    elif number == 5:
        output.delete(0, END)
        output.insert(0, city[4])
    elif number == 6:
        output.delete(0, END)
        output.insert(0, city[5])

def enter_click():
    try:
     api_request6= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=25&API_KEY=A965BFEF-761E-4713-800A-0C166473C53B")
     api6 = json.loads(api_request6.content)
    except Exception as e:
      api6 = "Error..."
    search = f"{api6[1]['ReportingArea']}, {api6[1]['StateCode']}, Air Quality Index: {api6[1]['AQI']},{api6[1]['Category']['Name']} "
    zipcode.delete(0, END)
    output.delete(0, END)
    output.insert(0, search)
    

      


   





enter = Button(interface, text = "Enter", width = 5, command  = enter_click)
city1 = Button(interface, text = "San Diego", width = 20, command = lambda : button_click(1))
city2 = Button(interface, text = "Riverside", width = 20, command = lambda : button_click(4))
city3 = Button(interface, text = "San Francisco", width =20, command = lambda : button_click(3))
city4 = Button(interface, text = "Rayleigh", width = 20, command = lambda : button_click(5))
city5 = Button(interface, text = "Atlanta", width = 20, command = lambda : button_click(2))
city6 = Button(interface, text = "Chicago", width = 20, command = lambda : button_click(6)) 
#put it on the screen
output.delete(0, END)
#output.insert(0, city[0])

output.grid(row = 0, column = 0,columnspan = 3)
label1.grid(row = 1, column = 0)
zipcode.grid(row = 1,column = 1 )
enter.grid(row = 1, column = 2)
city1.grid(row = 2, column = 0, padx = 10, pady = 10)
city2.grid(row = 2, column = 1,padx = 10, pady = 10)
city3.grid(row = 2, column = 2,padx = 10, pady = 10)
city4.grid(row = 3, column = 0, padx = 10, pady = 10)
city5.grid(row = 3, column = 1,padx = 10, pady = 10)
city6.grid(row = 3, column = 2,padx = 10, pady = 10)
interface.mainloop()

print(city[0])
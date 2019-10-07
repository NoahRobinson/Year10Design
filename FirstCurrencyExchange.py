import requests
from tkinter import *

def writeme():
    ofile = open("FirstCurrencyExchange.html","w")
    ofile.write("<p>" + str(e1.get()) + "</p>")
    ofile.close()

myrequest = requests.get("https://api.exchangeratesapi.io/latest?Base=CAD")
datajson = myrequest.json()

window = Tk()
e1 = Entry(window)
e1.grid(row = 0, column = 0)
b1 = Button(window, text = "convert", command = writeme)
b1.grid(row = 1, column = 0)

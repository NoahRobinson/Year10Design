import requests
from tkinter import *

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) 
topframe = Frame(root,bg='#4d419a',height='20')
topframe.pack(fill=X) 
can1 = Canvas(topframe,height='35',width='20',bg="#4d419a",highlightthickness=0)
can1.create_line(5, 10, 30, 10,fill='white')
can1.create_line(5, 15, 30, 15,fill='white')
can1.create_line(5, 20, 30, 20,fill='white')
can1.bind
can1.pack(side=LEFT)

invisoframe = Frame(root,width=200,height=250) 
invisoframe.pack()
titleheight = 100 
titleframe = Frame(invisoframe,width=200,height=titleheight,bg="#0f75bc")
titleframe.pack(fill=X)
titleframe.pack_propagate(0)
title = Label(titleframe,text="Currency Converter",fg="white",bg="#0f75bc")
title.config(font=("Arial", 32))
title.pack(ipady=titleheight/2)
contentheight = 150
contentframe = Frame(invisoframe,width=200,height=50,bg="#13a89e")
contentframe.pack(fill=X)
contentframe.pack_propagate(0)
content = Label(contentframe,text="Input Conversions:",fg="white",bg="#13a89e")
content.pack(fill = X)
contentframe2 = Frame(invisoframe,width=500,height=350,bg="#13a89e")
contentframe2.pack(fill = X)
contentframe2.pack_propagate(False)
optionframe = Frame(contentframe2, width = 100, height = 350, bg="#13a89e")
optionframe.pack()

start = StringVar(root)
start.set("CAD")

StartCurrency = OptionMenu(optionframe, start, "USD", "CAD", "EUR", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "AUD", "RON", "SEK", "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF", "SGD", "PLN", "BGN", "TRY", "CNY", "NOK", "NZD", "ZAR", "MXN", "ILS", "GBP", "KRW", "MYR" )
StartCurrency.grid(row = 0, column = 0, padx = 2)

end= StringVar(root)
end.set("CAD")

EndCurrency = OptionMenu(optionframe, end, "USD", "CAD", "EUR", "HKD", "ISK", "PHP", "DKK", "HUF", "CZK", "AUD", "RON", "SEK", "IDR", "INR", "BRL", "RUB", "HRK", "JPY", "THB", "CHF", "SGD", "PLN", "BGN", "TRY", "CNY", "NOK", "NZD", "ZAR", "MXN", "ILS", "GBP", "KRW", "MYR" )
EndCurrency.grid(row = 0, column = 1, padx = 2)

inputwidget = Entry(optionframe)
inputwidget.grid(row = 1, column = 0, columnspan = 2, pady = 4)

def readfile():
    f = open("exchangeapi.html", "r")
    fdata = f.read()
    f.close()
    fdata = fdata.splitlines()
    return fdata

def writetofile(text):
    f = open("exchangeapi.html", "w+")
    f.write(text)
    f.close()

endrate = 0

def convertval(startval, endval, inputval):
    global endrate
    instr = ("https://api.exchangeratesapi.io/latest?base=" + startval)
    myrequest = requests.get(instr)
    datajson = myrequest.json()
    if (startval == ("EUR")):
        startval = 1
    else:
        startrate = datajson['rates'][startval]
    endrate = datajson['rates'][endval]
    convertedval = inputval * endrate
    return(round(convertedval, 2))
    
def main():
    startval = start.get()
    endval = end.get()
    inputval = inputwidget.get()
    if (str.isdigit(inputval)):
        newval = convertval(startval, endval, float(inputval))
        htmltext = readfile()
        instring = ("1" + startval + ":" + str(round(endrate, 2)) + endval)
        htmltext[16] = instring
        instring = (str(inputval) + startval + " = " + str(newval) + endval)
        htmltext[19] = instring
        writetofile('\n'.join(htmltext))

entrybutton = Button(optionframe, text = "convert", command = main)
entrybutton.grid(row = 2, column = 0, columnspan = 2, pady = 4)

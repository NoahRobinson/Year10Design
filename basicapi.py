import requests

myrequest = requests.get("https://geo-info.co/43,-79")
datajson = myrequest.json()

city = datajson["city"]
nearby = datajson["nearbyCities"]
forterie = nearby[2]["city"]

ofile = open("apitesting.html","w")
ofile.write("<h1>" + city + "</h1>")
ofile.write("<p>" + forterie + "</p>")
ofile.close()

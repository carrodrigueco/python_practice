import urllib.request, urllib.parse, urllib.error
import json

while True:

    url = input("Enter Location:")

    if len(url) < 1:
        break

    print("Retrieving ", url)

    lol = urllib.request.urlopen(url)

    data = lol.read()

    print("Retrieved ", len(data), " caracteres")

    try:
        archivo = json.loads(data)
    except:
        archivo = None

    suma = 0
    contador = 0
    for i in archivo["comments"]:
        suma += i["count"]
        contador += 1

    print("Count :",contador)
    print("Sum :",suma)
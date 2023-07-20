import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_1437035.xml"
#url = input("Enter location: ")
lol = urllib.request.urlopen(url)
data = lol.read()
tree = ET.fromstring(data)

liste = tree.findall("comments/comment")

acumulador = 0
contador = 0
for item in liste:
    acumulador += int(item.find("count").text)
    contador+=1
print("Retrieving ", url)
print("Retrieved", len(data), " characters")
print("Count:",contador)
print("Sum:",acumulador)



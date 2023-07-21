import urllib.request, urllib.parse, urllib.error
import json

urloriginal = "http://py4e-data.dr-chuck.net/json?"

while True:

    address = input("Enter Location: ")

    if len(address) < 1:
        break

    url = urloriginal+urllib.parse.urlencode({"key" : "42", "address": address})

    print("Retrieving ", url)

    lol = urllib.request.urlopen(url)

    data = lol.read().decode()

    print("Retrieved ", len(data), " caracteres")

    try:
        archivo = json.loads(data)
    except:
        archivo = None

    if not archivo or "status" not in archivo or archivo["status"] != "OK":
        print("ERROR EN LA DIRECCION")
        print(data)
        continue

    print("Place id ",archivo["results"][0]["place_id"])


    while True:
        option = input("Do you like to enter other address? [1.No 2.Yes]")

        try:
            option = int(option)
        except:
            input("ERROR INVALID VALUE...[ENTER to continue]")
            continue

        if option != 1 and option != 2:
            input("ERROR INVALID VALUE...[ENTER to continue]")
            continue
        break

    if option == 1:
        break

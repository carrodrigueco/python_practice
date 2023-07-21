import json

data = """
       {
       "name": "Chuck",
       "phone": {"type": "intl", "number": "+1 734 303 4456" },
       "email": {"hide": "yes"}
       }
       
       """

#Basicaly this returns a python dictionary
data = json.loads(data)

print("Name:", data["name"])
print("Phone:", data["phone"]["number"])
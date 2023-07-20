import xml.etree.ElementTree as ET

data = """
        <stuff>
            <users>
                <user x = "1">
                    <id>313</id>
                    <name>Carlos</name>
                    <phone>+57 300 300 3333</phone>
                </user>
                <user x = "7">
                    <id>631</id>
                    <name>Chuck</name>
                    <phone>+1 250 666 124</phone>
                </user>
            </users>
        </stuff>
       """
#Transforma un string en un arbol de elementos de xml
other = ET.fromstring(data)

#Devuelve una lista con los nodos o pequeños arboles
#de cada uno de los user que pertenezcan al nodo users
usuarios = other.findall("users/user")
print()
print(">>>User count: ", len(usuarios))
print()

#Recorre la lista usuarios 
#que tiene de elementos arboles con cada uno de los nodos de los usuarios
for i in usuarios:
    #Busca los tags con cada uno de los nombres y despues extrae el texto dentro de ellos
    print(">>>Nombre: ", i.find("name").text)
    print(">>>Telefono: ", i.find("phone").text)
    print(">>>Id: ", i.find("id").text)
    #Busca un atributo x en el nodo 
    print(">>>Codigo de usuario: ", i.get("x"))
    print()



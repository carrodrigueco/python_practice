import sqlite3

conn = sqlite3.connect("././bases_datos/first_assigment_database.sqlite")
curs = conn.cursor()

curs.execute("""DROP TABLE IF EXISTS Counts""")
curs.execute("""CREATE TABLE Counts (org TEXT, count INTERGER)""")

while True:

    file = input(">>>Enter file name...")

    if len(file) < 1 :
        print(">>>[FATAL ERROR INVALID FILE]<<<")
        input(" "*10+"Enter to continue...")
        continue

    handle = open(file)
    for line in handle:

        if not line.startswith("From:"):
            continue

        parts = line.split()
        email = parts[1]
        org = email[email.find("@")+1:]

        curs.execute("""SELECT count FROM Counts WHERE org = ? """, (org,))
        row = curs.fetchone()

        if row is None:

            curs.execute("""INSERT INTO Counts (org, count) VALUES (?, 1)""", (org,))

        else:
            curs.execute("""UPDATE Counts SET count = count + 1 WHERE org = ?""", (org,))

        conn.commit()
    
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in curs.execute(sqlstr):
        print(str(row[0]), row[1])

    input(" "*10+"Enter to continue...")
    curs.close()
    break



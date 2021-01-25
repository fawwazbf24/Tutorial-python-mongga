import sqlite3

conn = sqlite3.connect("db.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS tab")
c.execute("""CREATE TABLE tab
        (nama text,
        usia INT(255),
        email text)
""")

c.execute("DROP TABLE IF EXISTS gambar")
c.execute("""CREATE TABLE gambar
        (gambar BLOB)
""")
#c.execute("INSERT INTO tab VALUES ('fawwaz',12,'fawwazbyru93@gmail.com')")
listdata = [
    ('alzi',21,'alziarif@gmail.com'),
    ('rifki',22,'rifkikicaw@yahoo.co.id'),
    ('jek',23,'faizjek@google.com'),
    ('gani',24,'ganiniga@hotmail.co.id'),
    ('dio',25,'pri.mi@yahoo.com')
]

c.executemany("INSERT INTO tab VALUES (?,?,?)",listdata)

#c.execute("SELECT rowid,* FROM tab ORDER BY nama DESC")
#order by DESC dari besar ke kecil, order by ASC dari kecil ke besar
#c.execute("SELECT rowid,* FROM tab WHERE nama LIKE '%i' AND email lIKE '%@gmail%'")
#c.execute("SELECT rowid,* FROM tab WHERE usia==22 ORDER BY nama")
c.execute("UPDATE tab SET nama='faiz' WHERE usia==23")
c.execute("DELETE FROM tab WHERE rowid==3")
c.execute("SELECT rowid,* FROM tab")


items = c.fetchall()


for f in items:
    print(f)

#for f in items:
#    print(f[0])

#print(items[2][2])
#print(c.fetchall())

c.execute("DROP TABLE IF EXISTS gambar")
c.execute("""CREATE TABLE gambar
        (gambar BLOB)
""")

gambar = open("foto_UB-removebg-preview (4).png","rb")
gambar2 = gambar.read()
gambarbaru = open("gambarbaru.png","wb")

gambarsimpen = sqlite3.Binary(gambar2)
c.execute("INSERT INTO gambar VALUES (?)",(gambarsimpen,))
c.execute("SELECT * FROM GAMBAR")
gambarbaru.write(c.fetchone()[0])

gambar.close()
gambarbaru.close()
c.close()

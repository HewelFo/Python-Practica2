# problema 3 hewe.ochoa@utp.ac.pa
import psycopg2


conn = psycopg2.connect(database="Chinook", user="postgres", password="1", host="127.0.0.1", port="5432")

fic = open("subgenres.txt", "r")
datos = fic.readlines()
fic.close()


table = conn.cursor()
forn = conn.cursor()
NColum = conn.cursor()
NDatos = conn.cursor()
DInsert = conn.cursor()

# Creando tabla, tabla con llave foranea y la nueva columna
table.execute('CREATE TABLE Subgénero (SubgenreId INT NOT NULL, SubgenreName VARCHAR(255) NOT NULL, SubgenrealtName VARCHAR(255), GenreId INT NOT NULL, CONSTRAINT fk_Subgénero PRIMARY KEY (subgenreid))')
forn.execute('ALTER TABLE "Subgénero" ADD CONSTRAINT "FK_SuggeneroGenero" FOREIGN KEY ("GenreId") REFERENCES "Genre" ("GenreId") ON DELETE NO ACTION ON UPDATE NO ACTION; CREATE INDEX "FK_SuggeneroGenero" ON "Subgénero" ("GenreId");')
NColum.execute('alter table "Track" add subgénero VARCHAR(255);')
x = 0
for data in datos:
    NDatos.execute('INSERT INTO "subgénero" ("subgenreid", "subgenrename", "subgenrealtname","genreid") VALUES (%d, %s, %s, %d);'% ( x+1, "'{}'".format(data), "''", 1))
    x = x +1

# Ingresando las canciones
cansion = ['smell like spirt','sweet childo mine','acid rain','so far away','darck crow']
banda = ['nirvana','guns and rose','avenged sevenflod','avenged sevenfols','man with a mision']
# ciclo for para ingresar las 5 canciones con las 5 bandas compositoras
for son in range(len(banda)):
    DInsert.execute('INSERT INTO "Track" ("TrackId", "Name", "AlbumId", "MediaTypeId","GenreId", "Composer", "Milliseconds", "Bytes", "UnitPrice", "subgénero") VALUES (%d, %s, %d, %d, %d, %s, %d, %d, %d, %s); ' % ( 3504, "'{}'".format(cansion[son]), 344, 1, 1, "'{}'".format(banda[son]), 5400000, 5400000 , 0.99, "'Pop Punk'"))



conn.commit()
conn.close()
#lab3 problema 2.1 hewel.ochoa@utp.ac.pa
import psycopg2

conn = psycopg2.connect(database="Chinook", user="postgres", password="1", host="127.0.0.1", port="5432")

TakeTim = conn.cursor()
TakeProm = conn.cursor()
TakeCom = conn.cursor()
TakeClie = conn.cursor()
TakeProm.execute('SELECT AVG("Bytes") FROM "Track"')
TakeTim.execute('SELECT * FROM "Track" WHERE "Milliseconds" > 5000000')
TakeCom.execute('SELECT * FROM "Track" WHERE "Composer" = NULL')
TakeClie.execute('SELECT * FROM "Customer"')
filast = TakeTim.fetchall()
filasp = TakeProm.fetchall()
filasc = TakeCom.fetchall()
filasC = TakeClie.fetchall()
print("los que tinen tiempo menor a 5000000 milisegundos")
for fila in filast:
	print(fila)
print("El promedio de los Bytes")
print(filasp)
print("tracks con compositores null")
for fil in filasc:
	print(fila)
print("El comando es: SELECT * FROM Track WHERE Composer = NULL")
print("Orden de clientes q piden pistas de cada pais")
print(filasC)
print("orden imberso de los clientes")
filasC.sort(reverse = True)
print(filasC)

conn.commit()
conn.close()

print("all rigth")
#problema 4  hewel.ochoa@utp.ac.pa
import time 
import random
import threading

		
class menu():

	def __init__(self, precioC, precioD, precioS, ordenC, ordenD, ordenS):
		self.precioC = precioC
		self.precioD = precioD
		self.precioS = precioS
		self.ordenC = ordenC
		self.ordenD = ordenD
		self.ordenS = ordenS
	def food(self):
		comida = ["ceviche","flan","arroz","sancocho"]
		dish = random.randint(0,3)
		print("El plato elegido es: ",comida[dish]," con un precio de 3$.")
		self.ordenC = comida[dish]
		self.precioC = 3
	def drinks(self):
		bebidas = ["agua","soda","cerveza nacionales"]
		glas = random.randint(0,2)
		print("la vevida elegida es: ",bebidas[glas]," con un precio de 1$.")
		self.ordenD = bebidas[glas]
		self.precioD = 1
	def final(self):
		especiales = ["cervezas importadas", "tragos"]
		special = random.randint(0,3)
		if special >= 2:
			print("no se ordenaron tragos especiales.")
		else:
			print("su trago es: ", especiales[special]," con un precio de 3$.")
			self.ordenS = especiales[special]
			self.precioS = 3

	def Precio_final(self):
		return self.precioC + self.precioD + self.precioS
	def orden(self):
		print("Su orden es fue: ", self.ordenC,", ",self.ordenD,", ",self.ordenS)
		
		

class steps(menu):
	def __init__(self):
		super().__init__(0,0,0,"","","")
	def paso1(self):
		menu.food(self)
		menu.drinks(self)
		menu.final(self)
		print("Se recive a al cliente y se toma su pedido.")
		time.sleep(5)
	def paso2():
		print("Cocinar el/los platos.")
		time.sleep(5)
	def paso3():
		print("Limpiar los plaos utilizados.")
		time.sleep(5)
	def paso4():
		print("llevar los platos a la mesa.")
	def paso5(self):
		print("Cobrar a al/los clientes y despedirse. Su factura")
		time.sleep(3)
		menu.orden(self)
		print("Su cuenta a pagar es de: ", menu.Precio_final(self))
		


Prose1 = threading.Thread(name="strn1", target=steps.paso2)
Prose2 = threading.Thread(name="strn2", target=steps.paso4)
Prose3 = threading.Thread(name="strn3", target=steps.paso3)

Rsteps = steps()
Rsteps.paso1()
Prose1.start()
Prose2.start()
Prose3.start()
Rsteps.paso5()



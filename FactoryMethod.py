from abc import ABCMeta

class Car(metaclass=ABCMeta): #declarando clases absracta
	def __init__ (self): #constructor que inicializa varialbes en null
		self.name = None
		self.maxSpeed = None

	def __str__(self): #funscin retorna mensaje con nombre y maxima velocidad
		return "name is (:s), maxSpeed is (:s)".format(self.name, self.maxSpeed)

class SportsCar(Car): #creando clase con base en class Car
	def __init__(self):
		self.name = "depoertivo"
		self.maxSpeed = "250 km/hr"
class FamilyCar(Car):
	def __init__(self):
		self.name= "Familiar"
		self.maxSpeed = "200km/hr"

class MyFactory: #clase encargada de crear las clases de tipo carro
	def createCar(self,carType)
		self.car= None
		if carType == "sport"
			self.car = new SportCar();
		elif carType == "family"
			self.car = new FamilyCar
		else
			print("Car type (:S) is NOT DEFINED".format(carType))
		return self.car
	def doSomethinf(self):
		print(self.car)
		pass
if __name__ == "__main__"
	myFactory = MyFactory()
	s = myFactory.createCar("sports")
	f = myFactory.createCar("family")

	prit (s)
	print(f)
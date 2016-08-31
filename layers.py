class PresentationLayer: #declaracin de la capa
	def __init__(self): #constructor
		self.name = "PresentaconLayer"

	def setLowerLayer(self, lowerLayer): #set para utilizar la capa de abajo
		self.lowerLayer = lowerLayer #asignando capa de abajo

	def s3(self, param): #responsabilidades de la capa3
		print("entramos al servicio s3")
		self.lowerLayer.s2(param)
		print("terminamos servicio s3")

class LogicLayer: #declaracin de la capa
	def __init__(self): #constructor
		self.name = "LogicLayer"

	def setLowerLayer(self, lowerLayer): #set para utilizar la capa de abajo
		self.lowerLayer = lowerLayer #asignando capa de abajo

	def s2(self, param): #responsabilidades de la capa3
		print("entramos al servicio s2")
		self.lowerLayer.s1(param)
		print("terminamos servicio s2")

class DataLayer: #declaracin de la capa datos
	def __init__(self): #constructor
		self.name = "DataLayer"
	#al ser la tulimita capa no necesita capa de abajo

	def s1(self, param): #responsabilidades de la capa de datos
		print("entramos al servicio s1")

if __name__ == "__main__":
	ui= PresentaconLayer() #isntaciando capas
	logic = LogicLayer()
	data = DataLayer()

	ui.setLowerLayer(logic) #capa de presentacion toma capa llgica
	logic.setLowerLayer(data)#capa de logica ctoma cpaa data

	ui.s3("exampleParam")
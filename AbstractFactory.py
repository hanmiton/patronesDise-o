from abc import ABCMeta, abstractmethod 
 
class Car(metaclass=ABCMeta): 
    def __init__(self): 
        self.name = None 
        self.maxSpeed = None 
         
    def __str__(self): 
        return "name is {:s}, maxSpeed is {:s}".format(self.name, self.maxSpeed) 
         
class SportsCar(Car): 
    def __init__(self): 
        self.name = "Deportivo" 
        self.maxSpeed = "250 km/hr" 
         
class FamilyCar(Car): 
    def __init__(self): 
        self.name = "Familiar" 
        self.maxSpeed = "150 km/hr" 
         
class AbstractFactory(metaclass=ABCMeta): 
    def __init__(self): 
        self.manufacturer = None 
 
    def __str__(self): 
        return "manufacturer is {:s}".format(self.manufacturer) 
         
    @abstractmethod 
    def createCar(self, carType): pass #metodo esta obligado a implementar metodo de la interface o metodo abstracto
     
    @staticmethod 
    def get_factory(factoryName): #este rebibe el nombre que se desea asociar para la fabricacion 
        if factoryName == "vw": 
            return VWFactory() #devuelve Wvfactory en caso que lo sea
        elif factoryName == "mb": 
            return MBFactory() 
             
        raise TypeError("Unknown Factory") 
         
         
class VWFactory(AbstractFactory): #implmentando el metodo abstracto 
    def __init__(self): 
        self.manufacturer = "VW" 
 
    def createCar(self, carType): 
        self.car = None 
        if carType == "sports": 
            self.car =  SportsCar(); 
        elif carType == "family": 
            self.car =  FamilyCar(); 
        else: 
            print("Car type {:s} is not defined".format(carType)) 
        return self.car  
             
    def doSomething(self): 
        print(self.car) 
             
if __name__ == "__main__": 
    myFactory = AbstractFactory.get_factory("vw") #con esto ya se pueden crear carros
     
    print(myFactory) 
     
    s = myFactory.createCar("sports") 
    f = myFactory.createCar("family") 
     
    print(s) 
    print(f) 
     

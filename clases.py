


class Car:

    marca="toyota"

    modelo = 1970

    color= "negro"


carro1= Car()

print(car(carro1.modelo))


#CREAR CONSTRUCTOR DE CLASE 


class Car:


   def __init__(self,marca, modelo, color  ):
    self.marca=marca
    self.modelo=modelo
    self.color=color



carro2 = Car ("kia",2006,"rojo")

#print (carro2.modelo)


#creacion de metodos para accesos a propiedades

def arrancar (self): 

    print(f"el carro de color{self.color}esta arrancando")


def frenar (self):

    print(f"el auto de modelo {self.modelo}esta frenando ")


carro2 = Car ("kia",2006,"rojo")    

print (carro2.color)
carro2.frenar ()
carro2.arrancar()

#herencia


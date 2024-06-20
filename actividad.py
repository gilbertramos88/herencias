
class fabrica :
   def __init__(self,color, precio):

    self.color=color
    self.precio=precio   
class carro(fabrica):
    def __init__(self, color, precio,llantas=4):
        super().__init__(color,precio)  # Llama al constructor de la clase Padre
        self.llantas=4
class motocicleta(fabrica):
    def __init__(self, color, precio,llantas=2):
        super().__init__(color,precio)  # Llama al constructor de la clase Padre
        self.llantas=llantas
        
mt1=motocicleta("roja",20000)
print(mt1.llantas)        
            
car1=carro("negro",8000)       
print(car1.llantas,car1.color)
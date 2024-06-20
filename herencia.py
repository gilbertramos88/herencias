#herencia

#agregar otras propiedades
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
       self.nombre = nombre
       self.edad = edad
       self.nacionalidad= nacionalidad



class empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,cargo,salario):
        super().__init__(self,nombre,edad,nacionalidad)
        self.cargo=cargo
        self.salario=salario
        
e1=empleado("diana",23,"colombiana","programador",2000)
print (e1.cargo)        
    

d2 = Empleado("marcela",33,"colombia","programador",1000)"""
print(d2.salario)

def multiplica (a,b):
    return a*b
print(multiplica("a",3))
#con error
def multiplica (a,b):
    return a*b
print(multiplica(2,3))

def mi_funcion():
    print(aeiuo)
    print(perro)
    
   x=7 
   """
   
class empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,cargo,salario):
        super().__init__(self,nombre,edad,nacionalidad)
        self.nombre=nombre
        self.nombre=nombre
        self.nombre=nombre
        
e1=empleado("diana",23,"colombiana","programador",2000)
print (e1.nombre)        
   
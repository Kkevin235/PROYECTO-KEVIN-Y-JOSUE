class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def mostrar_persona(self):
        print("Nombre: " + self.nombre + ", Edad: " + str(self.edad))
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    
    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.get_edad()
    

# Crear dos objetos de tipo Persona e imprimirlos
persona1 = Persona("Juan", 25)
persona2 = Persona("Maria", 17)

persona1.mostrar_persona()
persona2.mostrar_persona()

# Comprobar si una persona es mayor de edad
if persona1.es_mayor_de_edad():
    print(persona1.get_nombre() + " es mayor de edad.")
else:
    print(persona1.get_nombre() + " no es mayor de edad.")

if persona2.es_mayor_de_edad():
    print(persona2.get_nombre() + " es mayor de edad.")
else:
    print(persona2.get_nombre() + " no es mayor de edad.")

# Comparar la edad de dos personas
if persona1.es_mayor_que(persona2):
    print(persona1.get_nombre() + " es mayor que " + persona2.get_nombre())
else:
    print(persona2.get_nombre() + " es mayor que " + persona1.get_nombre())
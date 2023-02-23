class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

# Ejemplo de uso
persona1 = Persona("Juan", 20, "12345678A")
persona1.mostrar()
print("¿Es mayor de edad?:", persona1.esMayorDeEdad())
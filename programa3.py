class Divisa:
    def __init__(self):
        self.tasas = {"USD": 0.049, "EUR": 0.041, "JPY": 5.361}

    def convertir_divisa(self, cantidad, divisa):
        tasa = self.tasas[divisa]
        return cantidad * tasa

class ConvertidorDivisas(Divisa):
    def __init__(self):
        super().__init__()

    def convertir(self, cantidad, divisa_destino):
        cantidad_destino = self.convertir_divisa(cantidad, divisa_destino)
        return cantidad_destino

if __name__ == '__main__':
    convertidor = ConvertidorDivisas()

    cantidad = float(input("Ingresa la cantidad de MXN que deseas convertir: "))
    divisa_destino = input("Ingresa la divisa de destino (USD, EUR, JPY): ")

    cantidad_destino = convertidor.convertir(cantidad, divisa_destino)

    print("{} MXN equivale a {:.2f} {}.".format(cantidad, cantidad_destino, divisa_destino))
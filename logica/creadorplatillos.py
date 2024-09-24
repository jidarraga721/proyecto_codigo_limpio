from .platillo import Platillo

class CreadorPlatillos:
    def crear_platillo(self, nombre: str, precio: int) -> Platillo:
        platillo = Platillo(nombre=nombre, precio=precio)
        print(f"Platillo {nombre} creado con un precio de {precio} pesos.")
        return platillo

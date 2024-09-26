class Platillo:
    def __init__(self, nombre: str, precio: int, cantidad: int = 0):
        self.nombre: str = nombre
        self.precio: int = precio
        self.cantidad: int = cantidad

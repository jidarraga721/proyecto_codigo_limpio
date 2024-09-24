from .registro import Registro
from .mesa import Mesa

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre = nombre
        self.propinas: int = 0
        self.mesas_atendidas: int = 0
        self.calificacion: int = 0

    def crear_pedido(self, mesa: Mesa, pedido: list) -> "Factura":
        from .factura import Factura  # Importación dentro de la función para evitar el ciclo
        for platillo, cantidad in pedido:
            for _ in range(cantidad):
                mesa.agregar_pedido(platillo)
        self.mesas_atendidas += 1
        factura = Factura(mesa=mesa, mesero=self, pedido=pedido)
        return factura

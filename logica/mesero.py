from .registro import Registro
from .mesa import Mesa
from .platillo import Platillo
from typing import List

class Mesero(Registro):
    def __init__(self, id: str, contrasena: int, nombre: str):
        super().__init__(id, contrasena)
        self.nombre: str = nombre
        self.propinas: int = 0
        self.mesas_atendidas: int = 0
        self.calificacion: int = 0

    def crear_pedido(self, mesa: Mesa, pedido: List[Platillo]) -> "Factura":
        from .factura import Factura
        for platillo in pedido:
            mesa.agregar_pedido(platillo)
        self.mesas_atendidas += 1
        factura = Factura(mesa=mesa, mesero=self)
        return factura

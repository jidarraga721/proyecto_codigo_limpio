from .platillo import Platillo
from typing import List

class Cocina:
    def verificacion_pedido(self, pedido: List[Platillo]) -> bool:
        if all(pedido):
            print("Pedido verificado: todos los platillos están disponibles.")
            return True
        else:
            print("Pedido verificado: algunos platillos no están disponibles.")
            return False

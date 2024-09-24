from typing import List
from .platillo import Platillo

class Mesa:
    def __init__(self, id: int):
        self.id = id
        self.pedido: List[Platillo] = []

    def agregar_pedido(self, platillo: Platillo):
        self.pedido.append(platillo)
        print(f"Platillo {platillo.nombre} añadido a la mesa {self.id}.")

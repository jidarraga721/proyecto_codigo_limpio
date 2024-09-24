from typing import List
from .platillo import Platillo

class Mesa:
    def __init__(self, id: int):
        self.id = id
        self.pedido: List[Platillo] = []
        self.facturas: List = []  # Lista para almacenar múltiples facturas

    def agregar_pedido(self, platillo: Platillo):
        self.pedido.append(platillo)
        print(f"Platillo {platillo.nombre} añadido a la mesa {self.id}.")

    def agregar_factura(self, factura):
        self.facturas.append(factura)
        print(f"Factura #{factura.id} añadida a la mesa {self.id}.")

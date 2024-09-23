from .platillo import Platillo
from typing import List

class Inventario:
    def __init__(self):
        self.productos: List[Platillo] = []
        self.productos_faltantes: List[Platillo] = []

    def pedido_inventario(self, platillo: Platillo) -> List[Platillo]:
        if platillo not in self.productos:
            self.productos_faltantes.append(platillo)
            print(f"Platillo {platillo.nombre} añadido a la lista de productos faltantes.")
        return self.productos_faltantes

    def anadir_elementos_inventario(self, platillo: Platillo) -> None:
        self.productos.append(platillo)
        if platillo in self.productos_faltantes:
            self.productos_faltantes.remove(platillo)
        print(f"Platillo {platillo.nombre} añadido al inventario.")

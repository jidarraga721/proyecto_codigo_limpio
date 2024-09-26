from .platillo import Platillo

class Mesa:
    def __init__(self, id: int):
        self.id: int = id
        self.pedido: list[Platillo] = []
        self.facturas: list = []

    def agregar_pedido(self, platillo: Platillo):
        self.pedido.append(platillo)
        print(f"Platillo {platillo.nombre} añadido a la mesa {self.id}.")

    def agregar_factura(self, factura):
        self.facturas.append(factura)
        print(f"Factura #{factura.id} añadida a la mesa {self.id}.")

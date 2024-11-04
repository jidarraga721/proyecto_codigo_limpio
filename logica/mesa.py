from .platillo import Platillo


class Mesa:
    def __init__(self, id: int):
        self.id: int = id
        self.pedido: list[tuple[Platillo, int]] = []
        self.facturas: list = []

    def agregar_pedido(self, platillo: Platillo, cantidad: int):
        # Agrega el platillo y la cantidad al pedido
        self.pedido.append((platillo, cantidad))
        print(f"{cantidad} unidades de {platillo.nombre} añadidas a la mesa {self.id}.")

    def agregar_factura(self, factura):
        self.facturas.append(factura)
        print(f"Factura #{factura.id} añadida a la mesa {self.id}.")

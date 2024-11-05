from .mesa import Mesa
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .mesero import Mesero

class Factura:
    _id_counter = 1

    def __init__(self, mesa: Mesa, mesero: "Mesero", pedido: list):
        self.id: int = Factura._id_counter
        Factura._id_counter += 1
        self.mesa: Mesa = mesa
        self.mesero: Mesero = mesero
        self.pedido: list = pedido
        self.total: int = sum([platillo.precio * cantidad for platillo, cantidad in self.pedido])
        self.propina: int = self.calcular_propina()
        print(f"Factura #{self.id} generada para la mesa {self.mesa.id} por el mesero {self.mesero.nombre}.")

    def calcular_propina(self) -> int:
        propina = int(self.total * 0.1)
        self.mesero.propinas += propina
        return propina

    def generar_factura(self) -> str:
        factura_detalles = f"Factura #{self.id} - Mesa: {self.mesa.id}\n"
        factura_detalles += f"Atendido por: {self.mesero.nombre}\n"
        factura_detalles += "Detalle del pedido:\n"
        factura_detalles += f"{'Cantidad':<10}{'Platillo':<20}{'Precio Unitario':<20}{'Subtotal':<10}\n"

        for platillo, cantidad in self.pedido:
            subtotal = platillo.precio * cantidad
            factura_detalles += f"{cantidad:<10}{platillo.nombre:<20}{platillo.precio:<20}{subtotal:<10}\n"

        factura_detalles += f"\n{'Total:':<10}{self.total:<10} pesos\n"
        factura_detalles += f"{'Propina:':<10}{self.propina:<10} pesos\n"
        print(factura_detalles)
        return factura_detalles



from .mesa import Mesa
from typing import TYPE_CHECKING  # Importamos TYPE_CHECKING correctamente

if TYPE_CHECKING:
    from .mesero import Mesero  # Esto solo se importa para verificación de tipos

class Factura:
    _id_counter = 1

    def __init__(self, mesa: Mesa, mesero: 'Mesero'):  # Usamos 'Mesero' entre comillas para evitar la importación circular
        self.id = Factura._id_counter
        Factura._id_counter += 1
        self.mesa: mesa = mesa
        self.mesero: mesero = mesero
        self.pedido = mesa.pedido
        self.total = sum([platillo.precio for platillo in self.pedido])
        self.propina = self.calcular_propina()
        print(f"Factura #{self.id} generada para la mesa {self.mesa.id} por el mesero {self.mesero.nombre}.")

    def calcular_propina(self) -> int:
        propina = int(self.total * 0.1)
        self.mesero.propinas += propina
        return propina

    def generar_factura(self) -> str:
        factura_detalles = f"Factura #{self.id} - Mesa: {self.mesa.id} - Total: {self.total} pesos - Propina: {self.propina} pesos"
        print(factura_detalles)
        return factura_detalles

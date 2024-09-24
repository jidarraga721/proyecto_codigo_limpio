from .platillo import Platillo

class Inventario:
    def __init__(self):
        self.productos: list[Platillo] = []

    def anadir_elementos_inventario(self, platillo: Platillo, cantidad: int):
        for producto in self.productos:
            if producto.nombre == platillo.nombre:
                producto.cantidad += cantidad
                print(f"Cantidad de {platillo.nombre} actualizada a {producto.cantidad}.")
                return
        platillo.cantidad = cantidad
        self.productos.append(platillo)
        print(f"Platillo {platillo.nombre} añadido al inventario con {cantidad} unidades.")

    def verificar_existencia(self, nombre: str, cantidad: int) -> bool:
        for producto in self.productos:
            if producto.nombre == nombre and producto.cantidad >= cantidad:
                return True
        return False

    def restar_cantidad(self, nombre: str, cantidad: int) -> None :
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"Se han restado {cantidad} unidades de {nombre}. Quedan {producto.cantidad} unidades.")
                else:
                    print(f"No hay suficientes unidades de {nombre}.")

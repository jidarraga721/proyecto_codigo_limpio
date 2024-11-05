from .platillo import Platillo

class Inventario:
    def __init__(self):
        self.productos: list[Platillo] = []

    def anadir_elementos_inventario(self, platillo: Platillo, cantidad: int) -> None:
        producto_existente = next((producto for producto in self.productos if producto.nombre == platillo.nombre), None)
        if producto_existente:
            producto_existente.cantidad += cantidad
            print(f"Cantidad de {platillo.nombre} actualizada a {producto_existente.cantidad}.")
        else:
            platillo.cantidad = cantidad
            self.productos.append(platillo)
            print(f"Platillo {platillo.nombre} añadido al inventario con {cantidad} unidades.")

    def verificar_existencia(self, nombre: str, cantidad: int) -> bool:
        producto = next((producto for producto in self.productos if producto.nombre == nombre), None)
        if producto and producto.cantidad >= cantidad:
            return True
        print(f"No hay suficientes unidades de {nombre}.")
        return False

    def gestionar_inventario(self) -> None:
        while True:
            print("\n--- Gestión de Inventario ---")
            print("1. Añadir platillo al inventario")
            print("2. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del platillo: ")
                precio = int(input(f"Ingrese el precio de {nombre}: "))
                cantidad = int(input(f"Ingrese la cantidad de {nombre} a añadir: "))
                platillo = Platillo(nombre=nombre, precio=precio, cantidad=cantidad)
                self.anadir_elementos_inventario(platillo, cantidad)
            elif opcion == "2":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

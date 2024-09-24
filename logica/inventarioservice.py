from .platillo import Platillo

class InventarioService:
    def gestionar_inventario(self, inventario):
        while True:
            print("1. Añadir platillo al inventario")
            print("2. Revisar productos faltantes")
            print("3. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del platillo: ")
                precio = int(input(f"Ingrese el precio de {nombre}: "))
                platillo = Platillo(nombre=nombre, precio=precio)
                inventario.anadir_elementos_inventario(platillo)
            elif opcion == "2":
                if not inventario.productos_faltantes:
                    print("No hay productos faltantes.")
                else:
                    for faltante in inventario.productos_faltantes:
                        print(f"Producto faltante: {faltante.nombre}")
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

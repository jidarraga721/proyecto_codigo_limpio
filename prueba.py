from logica import *


mesero1 = Mesero(id="mesero1", contrasena=1234, nombre="Carlos")
mesero2 = Mesero(id="mesero2", contrasena=5678, nombre="Laura")
admin1 = Administrador(id="admin1", contrasena=4321, nombre="Jefe")


mesero1.registrar_usuario()
mesero2.registrar_usuario()
admin1.registrar_usuario()


bar = Bar()
mesa1 = Mesa(id=1)
mesa2 = Mesa(id=2)
bar.agregar_mesa(mesa1)
bar.agregar_mesa(mesa2)
bar.agregar_mesero(mesero1)
bar.agregar_mesero(mesero2)
bar.agregar_administrador(admin1)


platillo1 = admin1.crear_platillo(nombre="Hamburguesa", precio=15000)
platillo2 = admin1.crear_platillo(nombre="Papas Fritas", precio=5000)
platillo3 = admin1.crear_platillo(nombre="Cerveza", precio=8000)


pedido1 = [platillo1, platillo2]
factura1 = mesero1.crear_pedido(mesa=mesa1, pedido=pedido1)


factura1.generar_factura()


pedido2 = [platillo3, platillo1]
factura2 = mesero2.crear_pedido(mesa=mesa2, pedido=pedido2)


factura2.generar_factura()


admin1.calificar_mesero(mesero1, calificacion=8)
admin1.calificar_mesero(mesero2, calificacion=9)


admin1.obtener_ganancias(mesa1)


admin1.estadisticas_mesero(mesero1)


admin1.estadisticas_mesero(mesero2)


inventario = Inventario()
inventario.anadir_elementos_inventario(platillo1)
inventario.pedido_inventario(platillo2)


cocina = Cocina()
cocina.verificacion_pedido(pedido1)









    


             




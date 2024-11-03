from main import *

if __name__ == "__main__":
    controller = AppController()
    controller.cargar_datos_json()  # Cargar datos automáticamente al iniciar
    controller.menu_inicial()

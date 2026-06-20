# Importamos las clases necesarias
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
# Punto de inicio del programa
if __name__ == "__main__":
    # Creamos la instancia del restaurante
    mi_restaurante = Restaurante("Encuentro Sabor Lojano")
    # Creamos algunos productos
    p1 = Producto("P001", "Humita con cafe", 1.25, "Desayuno")
    p2 = Producto("B001", "Tamale con cafe"), 1.50, "Desayuno tradicional"
    p3 = Producto("D001", "Chesecake", 2.00, "Postre")
    # Agregamos los productos al restaurante
    mi_restaurante . agregar_producto(p1)
    mi_restaurante . agregar_producto(p2)
    mi_restaurante . agregar_prodcuto(p3)
    # Creamos algunos clientes
    c1 = Cliente ("1123569636", "Nicol Ordoñez", "0939071869")
    c2 = Cliente ("1758962324", "Andres Carlosama", "0980668228")
    # Registramos los clientes
    mi_restaurante . resgistrar_clientes(1)
    mi_restaurante . registrar_cleinte(2)
    # Mostramos toda la informacion en la consola
    print("\n" + "="*50)
    print(f"🏪 Sistema de Gestión: {mi_restaurante.nombre}")
    print("="*50)
    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()
# Importamos las clases necesarias desde la carpeta modelos
from modelos.producto import Producto
from modelos.cliente import Cliente

#Clase que gestiona las operaiones principales del restaurante
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        #Lista para almacenar produtos y clientes registrados
        self.lista_productos = [ ]
        self.lista_clientes = [ ]
    # Metodo para agregar un nuevo prodcuto al menu
    def agregar_producto(self, produto: Producto) :
        self.lista_productos.append(producto)
    print(f"✅ Producto '{producto.nombre}' agregado correctamente.")
    # Metodo para registrar un nuevo cliente
    def registrar_cliente(self, cliente:Cliente):
         self.lista_clientes.append(cliente)
    print(f"✅ Cliente '{cliente.nombre}' registrado correctamente.")
    #Metodo para mostrar todos los productos disponibles
    def mostrar_productos(self):
      print("\n📋 Menú del Restaurante:")
      if not self.lista_productos:
            print("No hay prodcutos registrados.")
            return
      for produto in self . lista_productos:
            print(producto)
    # Metodo para mostrar todos los clientes registrados
    def mostrar_clientes(self):
      print("\n👥 Clientes Registrados:")
      if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
      for cliente in self.lista_clientes:
            print(cliente)


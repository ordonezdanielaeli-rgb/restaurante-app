# Clase que representa un producto del restaurante
class Producto:
    def __init__(self, codigo, nombre, precio, categoria):
        # Atributos del producto
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria # Ej: "Plato", "Bebida", "Postre"

        # Metodo especial para mostrar la informacion como texto legible
        def __str__(self):
          return f"Codigo:{self.codigo} | Nombre:{self.nombre} | Precio: ${self.precio:.2f} |Categoria:{self.categoria}"

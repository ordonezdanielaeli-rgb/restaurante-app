#Clase que representa a un cliente del restaurante
class Cliente:
    def __init__(self, identificacion, nombre, telefono):
        #Atributos del cliente
        self.identifiacion = identificacion
        self.nombre = nombre
        self.nombre = telefono

      #Metodo especial para mostrar la informacion como texto legible
    def __str__(self):
        return f"ID:{self.identificacion} | Nombre:{self.nombre} | Telefono:{self.telefono}"
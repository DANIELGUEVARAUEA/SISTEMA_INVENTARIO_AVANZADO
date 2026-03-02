# Clase Producto
# Representa los productos que existe en el inventario

class Producto:

    # Constructor: se ejecuta cuando creamos un producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto        # ID único del producto
        self.__nombre = nombre        # Nombre del producto
        self.__cantidad = cantidad    # Cantidad disponible
        self.__precio = precio        # Precio del producto

    # ===== MÉTODOS GET (OBTENER DATOS) =====

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ===== MÉTODOS SET (MODIFICAR DATOS) =====

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Convierte el objeto en diccionario para guardarlo en archivo JSON
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    # Crea un objeto Producto desde un diccionario
    @staticmethod
    def from_dict(data):
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )
import os
from modelos.producto import Producto


class Inventario:

    def __init__(self):
        self.productos = {}  # Diccionario {ID: Producto}

    # ==============================
    # AÑADIR PRODUCTO
    # ==============================
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # ==============================
    # ACTUALIZAR PRODUCTO
    # ==============================
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if cantidad is not None:
                producto.set_cantidad(cantidad)

            if precio is not None:
                producto.set_precio(precio)

            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # ==============================
    # BUSCAR PRODUCTO
    # ==============================
    def buscar_por_nombre(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

    # ==============================
    # MOSTRAR PRODUCTOS
    # ==============================
    def mostrar_todos(self):
        if not self.productos:
            print("📭 Inventario vacío.")
            return

        for p in self.productos.values():
            print(f"{p.get_id()} | {p.get_nombre()} | "
                  f"{p.get_cantidad()} | ${p.get_precio():.2f}")

    # ==============================
    # GUARDAR EN TXT
    # ==============================
    def guardar_en_archivo(self, archivo="inventario.txt"):

        with open(archivo, "w") as f:
            for p in self.productos.values():

                # Guardamos los datos separados por coma
                linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                f.write(linea)

        print(" Inventario guardado en archivo TXT.")

    # ==============================
    # CARGAR DESDE TXT
    # ==============================
    def cargar_desde_archivo(self, archivo="inventario.txt"):

        if os.path.exists(archivo):

            with open(archivo, "r") as f:
                for linea in f:

                    # Quitamos salto de línea y separamos por coma
                    datos = linea.strip().split(",")

                    id_producto = datos[0]
                    nombre = datos[1]
                    cantidad = int(datos[2])
                    precio = float(datos[3])

                    producto = Producto(id_producto, nombre, cantidad, precio)
                    self.productos[id_producto] = producto

            print("Inventario cargado desde TXT.")
        else:
            print(" No existe archivo previo.")
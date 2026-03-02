# Archivo principal del sistema
# Aquí se ejecuta el menú

from modelos.producto import Producto
from servicios.inventario import Inventario


def menu():

    inventario = Inventario()

    # Cargar datos si ya existen
    inventario.cargar_desde_archivo()

    while True:

        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            for p in resultados:
                print(f"{p.get_id()} | {p.get_nombre()} | "
                      f"{p.get_cantidad()} | ${p.get_precio():.2f}")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Punto de inicio del programa
if __name__ == "__main__":
    menu()
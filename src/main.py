# Importar la funcion del comprobante
from radicado import generar_comprobante


def mostrar_menu():
    print("\nPAWQRS - GESTOR DE PQRS")
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Actualizar estado")
    print("4. Generar estadisticas")
    print("5. Salir")


def registrar_pqrs():

    print("\nREGISTRO DE PQRS")

    datos = {
        "radicado": input("Numero de radicado: "),
        "tipo": input("Tipo de PQRS: "),
        "solicitante": input("Nombre del solicitante: "),
        "mascota": input("Nombre de la mascota: "),
        "campus": input("Campus: "),
        "estado": input("Estado de la PQRS: "),
        "fecha_maxima": input("Fecha maxima de respuesta: ")
    }

    print("\nPQRS registrada correctamente.")

    # Generar el comprobante
    generar_comprobante(datos)


while True:

    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_pqrs()

    elif opcion == "2":
        print("Consulta de PQRS")

    elif opcion == "3":
        print("Actualizacion de estado")

    elif opcion == "4":
        print("Estadisticas")

    elif opcion == "5":
        print("Saliendo de PawQRS...")
        break

    else:
        print("Opcion no valida. Intente nuevamente.")


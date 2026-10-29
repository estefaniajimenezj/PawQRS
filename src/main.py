from radicado import
generar_comprobante
def mostrar_menu():
    print("\nPAWQRS - GESTOR DE PQRS")
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Actualizar estado")
    print("4. Generar estadísticas")
    print("5. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Registro de PQRS")

        datos = {
        "radicado": "PQRS-2026-0001",
        "tipo": "Petición",
        "solicitante": "Juan Pérez",
        "mascota": "Max",
        "campus": "Campus Principal",
        "estado": "Recibida",
        "fecha_maxima": "05/11/2026"
    }
    elif opcion == "2":
        print("Consulta de PQRS")
    elif opcion == "3":
        print("Actualización de estado")
    elif opcion == "4":
        print("Estadísticas")
    elif opcion == "5":
        print("Saliendo de PawQRS...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

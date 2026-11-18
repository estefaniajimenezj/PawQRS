from datetime import datetime, timedelta

def mostrar_menu():
    print("\nPAWQRS - GESTOR DE PQRS")
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Actualizar estado")
    print("4. Generar estadisticas")
    print("5. Salir")


def registrar_pqrs():
    print("\nREGISTRO DE PQRS")

    # Obtener la fecha y hora actual
    ahora = datetime.now()
    fecha_registro = ahora.date()

    # Capturar los datos del solicitante y la solicitud
    datos = {
        "id": None,

        "nombre_completo": input("Nombre completo: "),
        "tipo_documento": input("Tipo de documento (CC, TI, CE, PP, NIT): "),
        "numero_documento": input("Numero de documento: "),
        "tipo_telefono": input("Tipo de telefono: "),
        "telefono_contacto": input("Telefono de contacto: "),
        "correo_electronico": input("Correo electronico: "),
        "direccion": input("Direccion (opcional): "),

        "tipo_solicitud": input(
            "Tipo de solicitud (Peticion, Queja, Reclamo, Sugerencia): "
        ),

        "fecha_radicacion": fecha_registro.strftime("%Y-%m-%d"),

        "canal_recepcion": input("Canal de recepcion: "),
        "asunto_titulo": input("Asunto o titulo: "),
        "descripcion_detallada": input("Descripcion detallada: "),
        "tipo_mascota": input("Tipo de mascota (Perro o Gato): "),
        "campus_relacionado": input("Campus relacionado: "),

        "fecha_maxima_respuesta": (
            fecha_registro + timedelta(days=30)
        ).strftime("%Y-%m-%d"),

        "estado_peticion": "Registrada",
        "hora_radicacion": ahora.strftime("%H:%M:%S"),
        "fecha_solucion": ""
    }

    # Mostrar lo capturado para verificar los datos
    print("\nDATOS CAPTURADOS (PRUEBA)")

    for campo, valor in datos.items():
        print(f"{campo}: {valor}")

    print("\nAVISO: Este registro aun NO se ha guardado.")
    print("Falta conectar validaciones.py y archivos.py.")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_pqrs()

    elif opcion == "2":
        print("Consulta de PQRS - Pendiente de integrar")

    elif opcion == "3":
        print("Actualizacion de estado - Pendiente de integrar")

    elif opcion == "4":
        print("Estadisticas - Pendiente de integrar")

    elif opcion == "5":
        print("Saliendo de PawQRS...")
        break

    else:
        print("Opcion no valida. Intente nuevamente.")

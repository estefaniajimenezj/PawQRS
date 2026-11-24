from datetime import datetime, timedelta
from validaciones import (validar_nombre, validar_tipo_documento, validar_documento, validar_tipo_telefono,
    validar_telefono, validar_correo, validar_direccion,
    validar_tipo_pqrs)

def mostrar_menu():
    print("\nPAWQRS - GESTOR DE PQRS")
    print("1. Registrar PQRS")
    print("2. Consultar PQRS")
    print("3. Actualizar estado")
    print("4. Generar estadisticas")
    print("5. Salir")

def solicitar_nombre():
    while True:
        nombre = input("Nombre completo: ").strip()

        if validar_nombre(nombre):
            return nombre

        print("Nombre incorrecto.")
        print("Debe tener entre 3 y 100 caracteres y no contener numeros.")

def solicitar_tipo_documento():
    while True:
        tipo = input("Tipo de documento (CC, TI, CE, PP, NIT): ").strip().upper()

        if validar_tipo_documento(tipo):
            return tipo

        print("Tipo de documento incorrecto.")
        print("Opciones permitidas: CC, TI, CE, PP, NIT.")

def solicitar_numero_documento():
    while True:
        numero = input("Numero de documento: ").strip()

        if validar_documento(numero):
            return numero

        print("Numero de documento incorrecto.")
        print("Debe contener entre 3 y 15 digitos, sin letras.")

def solicitar_tipo_telefono():
    while True:
        tipo = input(
            "Tipo de telefono (Celular, Fijo, Corporativo, Otro): "
        ).strip().capitalize()

        if validar_tipo_telefono(tipo):
            return tipo

        print("Tipo de telefono incorrecto.")
        print("Opciones: Celular, Fijo, Corporativo u Otro.")

def solicitar_telefono():
    while True:
        telefono = input("Telefono de contacto: ").strip()

        if validar_telefono(telefono):
            return telefono

        print("Telefono incorrecto.")
        print("Debe contener exactamente 10 digitos.")

def solicitar_correo():
    while True:
        correo = input("Correo electronico: ").strip()

        if validar_correo(correo):
            return correo

        print("Correo electronico incorrecto.")
        print("Ejemplo valido: usuario@correo.com")

def solicitar_direccion():
    while True:
        direccion = input("Direccion (opcional): ").strip()

        if validar_direccion(direccion):
            return direccion

        print("Direccion incorrecta.")
        print("Si escribes una direccion, debe tener entre 5 y 200 caracteres.")

def solicitar_tipo_pqrs():
    while True:
        tipo = input(
            "Tipo de solicitud (Peticion, Queja, Reclamo, Sugerencia): "
        ).strip().capitalize()

        if validar_tipo_pqrs(tipo):
            return tipo

        print("Tipo de solicitud incorrecto.")
        print("Opciones: Peticion, Queja, Reclamo o Sugerencia.")

def registrar_pqrs():
    print("\nREGISTRO DE PQRS")

    # Obtener la fecha y hora actual
    ahora = datetime.now()
    fecha_registro = ahora.date()

    # Capturar los datos del solicitante y la solicitud
    datos = {
        "id": None,

        "nombre_completo": solicitar_nombre(),
        "tipo_documento": solicitar_tipo_documento(),
        "numero_documento": solicitar_numero_documento(),
        "tipo_telefono": solicitar_tipo_telefono(),
        "telefono_contacto": solicitar_telefono(),
        "correo_electronico": solicitar_correo(),
        "direccion": solicitar_direccion(),

        "tipo_solicitud": solicitar_tipo_pqrs(),

        "fecha_radicacion": fecha_registro.strftime("%Y-%m-%d"),

        "canal_recepcion": input("Canal de recepcion: "),
        "asunto_titulo": input("Asunto o titulo: ").strip(),
        "descripcion_detallada": input("Descripcion detallada: ").strip(),
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
    print("Falta integrar las demas validaciones y archivos.py.")


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

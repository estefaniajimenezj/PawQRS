from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from archivos import guardar_registro, leer_registros, buscar_por_radicado, actualizar_estado
from radicado import generar_comprobante
from reportes import mostrar_estadisticas
from validaciones import (validar_nombre, validar_tipo_documento, validar_documento, validar_tipo_telefono,
    validar_telefono, validar_correo, validar_direccion,
    validar_tipo_pqrs, validar_canal, validar_titulo, validar_descripcion, validar_mascota, validar_campus)

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
    opciones = {
        "1": "CC",
        "2": "TI",
        "3": "CE",
        "4": "PP",
        "5": "NIT"
    }

    while True:
        print("\nTIPO DE DOCUMENTO")
        print("1. CC")
        print("2. TI")
        print("3. CE")
        print("4. PP")
        print("5. NIT")

        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion in opciones:
            tipo = opciones[opcion]

            if validar_tipo_documento(tipo):
                return tipo

        print("Opcion incorrecta. Selecciona un numero del 1 al 5.")

def solicitar_numero_documento():
    while True:
        numero = input("Numero de documento: ").strip()

        if validar_documento(numero):
            return numero

        print("Numero de documento incorrecto.")
        print("Debe contener entre 3 y 15 digitos, sin letras.")

def solicitar_tipo_telefono():
    opciones = {
        "1": "Celular",
        "2": "Fijo",
        "3": "Corporativo",
        "4": "Otro"
    }

    while True:
        print("\nTIPO DE TELEFONO")
        print("1. Celular")
        print("2. Fijo")
        print("3. Corporativo")
        print("4. Otro")

        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion in opciones:
            tipo = opciones[opcion]

            if validar_tipo_telefono(tipo):
                return tipo

        print("Opcion incorrecta. Selecciona un numero del 1 al 4.")

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
    opciones = {
        "1": "Peticion",
        "2": "Queja",
        "3": "Reclamo",
        "4": "Sugerencia"
    }

    while True:
        print("\nTIPO DE SOLICITUD")
        print("1. Peticion")
        print("2. Queja")
        print("3. Reclamo")
        print("4. Sugerencia")

        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion in opciones:
            tipo = opciones[opcion]

            if validar_tipo_pqrs(tipo):
                return tipo

        print("Opcion incorrecta. Selecciona un numero del 1 al 4.")

def solicitar_canal():
    opciones = {
        "1": "Presencial",
        "2": "Correo electrónico",
        "3": "Página web",
        "4": "Teléfono",
        "5": "Redes sociales",
        "6": "Otro"
    }

    while True:
        print("\nCANAL DE RECEPCION")
        print("1. Presencial")
        print("2. Correo electrónico")
        print("3. Página web")
        print("4. Teléfono")
        print("5. Redes sociales")
        print("6. Otro")

        opcion = input("Seleccione una opcion (1-6): ").strip()

        if opcion in opciones:
            canal = opciones[opcion]

            if validar_canal(canal):
                return canal

        print("Opcion incorrecta. Selecciona un numero del 1 al 6.")

def solicitar_titulo():
    while True:
        titulo = input("Asunto o titulo: ").strip()

        if validar_titulo(titulo):
            return titulo

        print("Asunto o titulo incorrecto.")
        print("Debe contener entre 5 y 150 caracteres.")

def solicitar_descripcion():
    while True:
        descripcion = input("Descripcion detallada: ").strip()

        if validar_descripcion(descripcion):
            return descripcion

        print("Descripcion incorrecta.")
        print("Debe tener entre 20 y 2000 caracteres.")

def solicitar_mascota():
    opciones = {
        "1": "Perro",
        "2": "Gato"
    }

    while True:
        print("\nTIPO DE MASCOTA")
        print("1. Perro")
        print("2. Gato")

        opcion = input("Seleccione una opcion (1-2): ").strip()

        if opcion in opciones:
            mascota = opciones[opcion]

            if validar_mascota(mascota):
                return mascota

        print("Opcion incorrecta. Selecciona 1 o 2.") 

def solicitar_campus():
    campus_validos = [
        "Campus Medellín - Ciudad Universitaria",
        "Campus Medellín - Ciudadela Robledo",
        "Campus en el Área de la Salud",
        "Campus Medellín - Sede de Posgrado",
        "Campus Medellín - Edificio San Ignacio",
        "Campus Medellín - Antigua Escuela de Derecho",
        "Campus Medellín - Edificio Antioquia",
        "Campus Medellín - Casas Patrimoniales",
        "Campus Medellín - Edificio de Extensión"
    ]

    while True:
        print("\nCampus disponibles:")

        for numero, campus in enumerate(campus_validos, start=1):
            print(f"{numero}. {campus}")

        opcion = input("Selecciona un campus (1-9): ").strip()

        if opcion.isdigit():
            numero = int(opcion)

            if 1 <= numero <= 9:
                campus = campus_validos[numero - 1]

                if validar_campus(campus):
                    return campus

        print("Campus incorrecto. Selecciona un numero del 1 al 9.")


def registrar_pqrs():
    print("\nREGISTRO DE PQRS")

    # Obtener la fecha y hora actual
    ahora = datetime.now(ZoneInfo("America/Bogota"))
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

        "canal_recepcion": solicitar_canal(),
        "asunto_titulo": solicitar_titulo(),
        "descripcion_detallada": solicitar_descripcion(),
        "tipo_mascota": solicitar_mascota(),
        "campus_relacionado": solicitar_campus(),

        "fecha_maxima_respuesta": (
            fecha_registro + timedelta(days=30)
        ).strftime("%Y-%m-%d"),

        "estado_peticion": "Registrada",
        "hora_radicacion": ahora.strftime("%H:%M:%S"),
        "fecha_solucion": ""
    }

    if guardar_registro(datos):
        registros = leer_registros(datos["tipo_solicitud"])
        if registros:
            registro = registros[-1]
            print("PQRS registrada:", registro["radicado"])
            try:
                generar_comprobante(registro)
            except (OSError, ValueError, KeyError, TypeError) as error:
                print("PQRS guardada, pero no se pudo generar comprobante:", error)
    else:
        print("No fue posible guardar la PQRS.")


def consultar_pqrs():
    tipo = solicitar_tipo_pqrs()
    radicado = input("Radicado a consultar (ej. QUE-0001): ").strip().upper()
    registro = buscar_por_radicado(tipo, radicado)
    if registro is None:
        print("No se encontro la PQRS.")
        return

    for campo, valor in registro.items():
        if campo == "direccion" and not valor:
            valor = "N/A"

        print(f"{campo}: {valor}")


def cambiar_estado_pqrs():
    tipo = solicitar_tipo_pqrs()
    radicado = input("Radicado a actualizar: ").strip().upper()
    registro = buscar_por_radicado(tipo, radicado)
    if registro is None:
        print("No se encontro la PQRS.")
        return

    transiciones = {"Registrada": "En proceso", "En proceso": "Solucionada"}
    actual = registro.get("estado_peticion", "")
    siguiente = transiciones.get(actual)
    if siguiente is None:
        print("La PQRS ya esta solucionada o tiene un estado no valido.")
        return

    print(f"Estado actual: {actual}. Siguiente estado: {siguiente}.")
    if input("Confirmar cambio (S/N): ").strip().lower() == "s":
        actualizar_estado(tipo, radicado, siguiente)
    else:
        print("Cambio cancelado.")


def iniciar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_pqrs()
        elif opcion == "2":
            consultar_pqrs()
        elif opcion == "3":
            cambiar_estado_pqrs()
        elif opcion == "4":
            mostrar_estadisticas()
        elif opcion == "5":
            print("Saliendo de PawQRS...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    iniciar_programa()

from datetime import date, datetime


# Registros ficticios para probar las estadisticas.
registros_prueba = [
    {
        "id": 1,
        "tipo_solicitud": "Petición",
        "tipo_mascota": "Perro",
        "fecha_radicacion": "2026-11-10",
        "fecha_maxima_respuesta": "2026-12-10",
        "estado_peticion": "Solucionada",
        "fecha_solucion": "2026-11-14"
    },
    {
        "id": 2,
        "tipo_solicitud": "Queja",
        "tipo_mascota": "Gato",
        "fecha_radicacion": "2026-11-12",
        "fecha_maxima_respuesta": "2026-12-12",
        "estado_peticion": "En proceso",
        "fecha_solucion": ""
    },
    {
        "id": 3,
        "tipo_solicitud": "Reclamo",
        "tipo_mascota": "Perro",
        "fecha_radicacion": "2026-11-13",
        "fecha_maxima_respuesta": "2026-12-13",
        "estado_peticion": "Solucionada",
        "fecha_solucion": "2026-11-19"
    },
    {
        "id": 4,
        "tipo_solicitud": "Sugerencia",
        "tipo_mascota": "Gato",
        "fecha_radicacion": "2026-11-15",
        "fecha_maxima_respuesta": "2026-11-21",
        "estado_peticion": "Registrada",
        "fecha_solucion": ""
    }
]

def contar_por_tipo(registros):

    peticiones = 0
    quejas = 0
    reclamos = 0
    sugerencias = 0

    for registro in registros:

        if registro["tipo_solicitud"] == "Petición":
            peticiones += 1

        elif registro["tipo_solicitud"] == "Queja":
            quejas += 1

        elif registro["tipo_solicitud"] == "Reclamo":
            reclamos += 1

        elif registro["tipo_solicitud"] == "Sugerencia":
            sugerencias += 1

    print("Cantidad de Peticiones:", peticiones)
    print("Cantidad de Quejas:", quejas)
    print("Cantidad de Reclamos:", reclamos)
    print("Cantidad de Sugerencias:", sugerencias)

contar_por_tipo(registros_prueba)

def contar_por_mascota(registros):

    perros = 0
    gatos = 0

    for registro in registros:

        if registro["tipo_mascota"] == "Perro":
            perros += 1

        elif registro["tipo_mascota"] == "Gato":
            gatos += 1

    print("Cantidad de Perros:", perros)
    print("Cantidad de Gatos:", gatos)

contar_por_mascota(registros_prueba)

def contar_por_estado(registros):

    registradas = 0
    en_proceso = 0
    solucionadas = 0

    for registro in registros:

        if registro["estado_peticion"] == "Registrada":
            registradas += 1

        elif registro["estado_peticion"] == "En proceso":
            en_proceso += 1

        elif registro["estado_peticion"] == "Solucionada":
            solucionadas += 1

    print("PQRS Registradas:", registradas)
    print("PQRS En proceso:", en_proceso)
    print("PQRS Solucionadas:", solucionadas)

contar_por_estado(registros_prueba)

def calcular_promedio_respuesta(registros):

    total_dias = 0
    cantidad = 0

    for registro in registros:

        if registro["estado_peticion"] == "Solucionada":

            fecha_inicio = datetime.strptime(
                registro["fecha_radicacion"], "%Y-%m-%d"
            )

            fecha_fin = datetime.strptime(
                registro["fecha_solucion"], "%Y-%m-%d"
            )

            dias = (fecha_fin - fecha_inicio).days

            total_dias += dias
            cantidad += 1

    if cantidad > 0:

        promedio = total_dias / cantidad

        print("Promedio de dias de respuesta:", promedio)

    else:
        print("No hay PQRS solucionadas.")


calcular_promedio_respuesta(registros_prueba)

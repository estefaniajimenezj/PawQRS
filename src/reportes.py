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

        if registro["tipo_solicitud"].strip().lower() in ("petición", "peticion"):
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



def calcular_promedio_respuesta(registros):

    total_dias = 0
    cantidad = 0

    for registro in registros:

        if registro["estado_peticion"] == "Solucionada":

            fecha_inicio = datetime.strptime(
                registro["fecha_radicacion"], "%Y-%m-%d"
            )

            fecha_fin = datetime.strptime(
                registro["fecha_solucion"][:10], "%Y-%m-%d"
            )

            dias = (fecha_fin - fecha_inicio).days

            total_dias += dias
            cantidad += 1

    if cantidad > 0:

        promedio = total_dias / cantidad

        print("Promedio de dias de respuesta:", round(promedio))

    else:
        print("No hay PQRS solucionadas.")




def obtener_pqrs_antiguas(registros):

    activas = []

    for registro in registros:

        if registro["estado_peticion"] != "Solucionada":
            activas.append(registro)

    # Ordenar las solicitudes por fecha
    for i in range(len(activas)):

        for j in range(len(activas) - 1):

            if activas[j]["fecha_radicacion"] > activas[j + 1]["fecha_radicacion"]:

                temporal = activas[j]
                activas[j] = activas[j + 1]
                activas[j + 1] = temporal

    print("PQRS activas mas antiguas:")

    contador = 0

    for registro in activas:

        if contador < 5:

            print(
                "Radicado:", registro["radicado"],
                "Fecha:", registro["fecha_radicacion"]
            )

            contador += 1



def clasificar_vencimientos(registros):

    proximas = 0
    vencidas = 0

    for registro in registros:

        if registro["estado_peticion"] != "Solucionada":

            fecha_vencimiento = datetime.strptime(
                registro["fecha_maxima_respuesta"], "%Y-%m-%d"
            ).date()

            dias_restantes = (fecha_vencimiento - date.today()).days

            if dias_restantes < 0:
                vencidas += 1

            elif dias_restantes <= 5:
                proximas += 1

    print("PQRS proximas a vencer:", proximas)
    print("PQRS vencidas:", vencidas)




def cargar_registros_reales():
    from archivos import leer_registros
    registros = []
    for tipo in ("Peticion", "Queja", "Reclamo", "Sugerencia"):
        registros.extend(leer_registros(tipo))
    return registros


def mostrar_estadisticas():
    registros = cargar_registros_reales()
    print("\nESTADISTICAS DE PAWQRS")
    if not registros:
        print("Todavia no hay solicitudes registradas.")
        return
    contar_por_tipo(registros)
    contar_por_mascota(registros)
    contar_por_estado(registros)
    calcular_promedio_respuesta(registros)
    obtener_pqrs_antiguas(registros)
    clasificar_vencimientos(registros)

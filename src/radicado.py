def generar_comprobante(datos):
    """
    Genera un comprobante de radicacion de una PQRS.
    """

    ancho = 50

    # Obtener los datos de la PQRS
    radicado = datos["radicado"]
    tipo = datos["tipo"]
    solicitante = datos["solicitante"]
    mascota = datos["mascota"]
    campus = datos["campus"]
    estado = datos["estado"]
    fecha_maxima = datos["fecha_maxima"]

    # Organizar el comprobante
    print("\n" + "=" * ancho)
    print("COMPROBANTE DE RADICACION".center(ancho))
    print("SISTEMA DE GESTION DE PQRS".center(ancho))
    print("=" * ancho)

    print("RADICADO: " + str(radicado))
    print("-" * ancho)

    print("Tipo: " + tipo)
    print("Solicitante: " + solicitante[:30])
    print("Mascota: " + mascota[:30])
    print("Campus: " + campus[:30])
    print("Estado: " + estado)
    print("Fecha maxima de respuesta: " + fecha_maxima)

    print("=" * ancho)
    print("Gracias por utilizar nuestro sistema".center(ancho))
    print("=" * ancho)


# Datos de prueba
datos_prueba = {
    "radicado": "PQRS-2026-001",
    "tipo": "Peticion",
    "solicitante": "Carlos Rodriguez",
    "mascota": "Max",
    "campus": "Campus Principal",
    "estado": "Registrada",
    "fecha_maxima": "10/11/2026"
}

# Probar la funcion
if __name__ == "__main__":
    generar_comprobante(datos_prueba)

   

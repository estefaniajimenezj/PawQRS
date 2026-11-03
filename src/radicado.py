def generar_comprobante(datos):

    ancho = 50

    print("\n" + "=" * ancho)
    print("COMPROBANTE DE RADICACION".center(ancho))
    print("SISTEMA DE GESTION DE PQRS".center(ancho))
    print("=" * ancho)

    print("RADICADO: " + str(datos["radicado"]))
    print("-" * ancho)

    print("Tipo: " + datos["tipo"][:35])
    print("Solicitante: " + datos["solicitante"][:35])
    print("Mascota: " + datos["mascota"][:35])
    print("Campus: " + datos["campus"][:35])
    print("Estado: " + datos["estado"][:35])
    print("Fecha maxima: " + datos["fecha_maxima"])

    print("=" * ancho)
    print("GRACIAS POR UTILIZAR NUESTRO SISTEMA".center(ancho))
    print("=" * ancho)


   
